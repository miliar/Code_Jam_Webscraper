#include<iostream>
#include<fstream>
using namespace std;
int t,o;
int i,ans,sum,n;
char c;
int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    cin>>t;
    for (int o=1;o<=t;o++)
    {
        cin>>n;
        sum=0;
        ans=0;
        for (i=0;i<=n;i++)
        {
            if (sum<i){ans+=i-sum;sum=i;}
            cin>>c;
            sum+=c-'0';
        }
        cout<<"Case #"<<o<<": "<<ans<<endl;
    }
}
