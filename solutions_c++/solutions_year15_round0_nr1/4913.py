#include<bits/stdc++.h>
using namespace std;
int main(){
    int T;
    freopen("A-large.in","r",stdin);
    freopen("A-large.txt","w",stdout);
    scanf("%d",&T);
    for(int t=1;t<=T;++t){
        int N;
        string s;
        scanf("%d",&N);
        cin>>s;
        int ans=0,pr=s[0]-'0';
        for(int i=1;i<=N;++i){
            if(pr>=i){
                ;
            }
            else if(s[i]!='0'){
                ans=ans+i-pr;
                pr=i;
            }
            pr=pr+s[i]-'0';
        }
        printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}
