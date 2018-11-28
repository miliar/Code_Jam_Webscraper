#include <iostream>
#include <string>
#include <cstdio>
using namespace std;

int main()
{
  //  freopen("A-large.in","r",stdin);
  //  freopen("A-large.out","w",stdout);
    int T,i,cas,smax,ans, sum;
    string str;
    cin>>T;
    for(cas=1;cas<=T;cas++) {
        cin>>smax>>str;
        ans=0;
        sum=str[0]-'0';
        for(i=1;i<=smax;i++) {
            if(str[i]=='0') continue;
            if(sum<i) {
                if(ans<i-sum) ans=i-sum;
            }
            sum=sum+str[i]-'0';
        }
        cout<<"Case #"<<cas<<": "<<ans<<endl;
    }
    return 0;
}
