#include <iostream>
#include <cstdio>

using namespace std;

int T,K,L,S,cnt[26],total,maxInst,ans;
char key;
string target;

void getCount(string s){
    int inst = 0;
    for (int i = 0; i <= s.length()-L; i++){
        if (s.substr(i,L) == target){
            inst++;
        }
    }
    if (inst != 0){
        ans += inst;
        maxInst = max(maxInst,inst);
    }
}

void generate(string s){
    if (s.length() == S){
        total++;
        getCount(s);
        return;
    }
    for (int i = 0; i < 26; i++){
        for (int j = 1; j <= cnt[i]; j++){
            generate(s+(char)('A'+i));
        }
    }
}

int main()
{
    freopen("cj15r1cp2small.in","r",stdin);
    freopen("cj15r1cp2small.out","w",stdout);
    cin >> T;
    for (int z = 1; z <= T; z++){
        maxInst = 0; ans = 0; total = 0;
        fill(cnt,cnt+26,0);
        cin >> K >> L >> S;
        for (int i = 0; i < K; i++){
            cin >> key;
            cnt[key-'A']++;
        }
        cin >> target;
        generate("");
        printf("Case #%d: %.8f\n",z,(double)maxInst - (double)ans/(double)total);
    }
    return 0;
}

