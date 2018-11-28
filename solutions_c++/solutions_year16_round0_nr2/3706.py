#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t,sz,cnt;
    scanf("%d", &t);
    for(int k=1; k<=t; ++k){
        string s;
        cin>>s;
        sz = s.size();
        cnt = 0;
        for(int i=sz-1; i>=0; --i){
            if(s[i]=='+'){
                continue;
            }
            for(int j=0; j<=i; ++j){
                if(s[j]=='+'){
                    s[j] = '-';
                }
                else {
                    s[j] = '+';
                }
            }
            cnt++;
        }
        printf("Case #%d: %d\n", k, cnt);
    }
    return 0;
}
