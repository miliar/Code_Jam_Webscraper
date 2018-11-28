#include<bits/stdc++.h>
using namespace std;
#define inc(i,x) for(int i=0;i<x;i++)
#define onc(i,x) for(int i=1;i<=x;i++)
char s[1005];
int k;
main()
{
    int t;
    cin>>t;
    onc(kase,t){
        cin>>s;
        cin>>k;
        int l=strlen(s);
        int ans=0;
        for(int i=0;i<=l-k;i++){
            if(s[i]=='-'){
                ans++;
                inc(j,k){
                    if(s[i+j]=='-') s[i+j]='+';
                    else s[i+j]='-';
                }
            }
        }
        for(int i=0;i<l;i++) if(s[i]=='-') ans=-1;
        printf("Case #%d: ",kase);
        if(ans<0) cout<<"IMPOSSIBLE\n";
        else cout<<ans<<'\n';
    }
}
