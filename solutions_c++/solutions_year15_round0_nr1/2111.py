#include<cstdio>
#include<iostream>
int f[1010];
using namespace std;

int main()
{
    freopen("al.in","r",stdin);
    freopen("al.out","w",stdout);
    int tt;
    cin>>tt;
    int smax;
    string s;
    for(int ii=1;ii<=tt;ii++)
    {
        cin>>smax>>s;
        for(int i=0;i<s.size();i++)
            f[i]=s[i]-48;
        int cur=0,ans=0;
        for(int i=0;i<=smax;i++)
        {
            if (cur<i){
                ans+=i-cur;
                cur=i;
            }
            cur+=f[i];
        }
        cout<<"Case #"<<ii<<": "<<ans<<endl;
    }
    return 0;
}
        
        
