#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

static char s[1000010];
long long nval;

inline int checkv(char t){
    if(t=='a'||t=='e'||t=='i'||t=='o'||t=='u') return 1;
    else return 0;
}

int main()
{
    freopen("in.in", "r", stdin);
    freopen("out.out", "w", stdout);
    ios::sync_with_stdio(0);
    int T; cin >> T;
    for (int t=1; t<=T; ++t){
        int N; nval=0; int temp;
        cin >> s >> N;

        for (int i=0; i<strlen(s); ++i){
            int cons=temp=0;
            for (int j=i; j<strlen(s); ++j){
                if (!checkv(s[j])) cons++;
                else cons=0;
                if (cons>=N) temp=cons;
                if (temp>=N)nval++;
            }
        }
        cout << "Case #" << t << ": " << nval << '\n';
    }
    return 0;
}
