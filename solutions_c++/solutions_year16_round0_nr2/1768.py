#include <bits/stdc++.h>

using namespace std;

int main() {


    int T;
    scanf("%d", &T);
    for(int z=1;z<T+1;++z) {
        string s;
        cin >> s;
        int n =(int)s.size(),ind=0;
        for(int i=n-1;i>=0;--i){
            if(s[i]=='-'){
                ind=i+1;
                break;
            }
        }
        int cnt=0,cur=0;
        for(int i=1;i<ind;++i){
            if(s[i]!=s[cur]){
                cnt++;
                cur=i;
            }
        }
        if(!ind)
            cnt=-1;
        cout << "Case #" << z << ": " << cnt+1 << "\n";
    }
}
