#include<bits/stdc++.h>
using namespace std;
string str;
long long i,n,cnt,t,d,inv;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    cin>>t;
    while(t--){
        inv=0;
        cin>>n>>str;
        cnt=str[0]-'0';
        for(i=1;i<=n;i++)
        {
            if(cnt+inv<i){
                inv+=(i-cnt-inv);
            }
            cnt+=str[i];
            cnt-='0';
        }
        cout<<"Case #"<<++d<<": "<<inv<<endl;
    }
}
