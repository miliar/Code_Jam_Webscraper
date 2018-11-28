#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<cmath>
#include<algorithm>
using namespace std;


typedef long long ll;


int main(){
    freopen("large.in","r",stdin);
    freopen("lout.out","w",stdout);
    int t,smx,n,ans,i,j;
    string s;
    cin>>t;
    for(j=1;j<=t;j++){
            cin>>smx;
            cin>>s;
            ans=0;
            n=0;
            for(i=0;i<=smx;i++){
                if(s[i]!='0' && n<i){
                    ans+=i-n;
                    n=i;
                }
                n+=s[i]-'0';

                /*if(s[i]=='0' && n<=i){
                    n++;ans++;
                }
                else
                    n+=s[i]-'0';
                */
            }
            cout<<"Case #"<<j<<": "<<ans<<"\n";
    }


    return 0;
}
