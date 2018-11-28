#include<cstdio>
#include<iostream>
#include<queue>
#include<cmath>
using namespace std;
int n;
int s[100010];
const int cc[4][4]={{1,2,3,4},{2,-1,4,-3},{3,-4,-1,2},{4,3,-2,-1}};
int f[100010];

int cal(int x,int y)
{
    int flag=1-((x>0)^(y>0))*2;
    return cc[abs(x)-1][abs(y)-1]*flag;
        
}

int main()
{
    freopen("cs.in","r",stdin);
    freopen("cs.out","w",stdout);
    int tt;
    cin>>tt;
    for(int ii=1;ii<=tt;ii++)
    {
        int t;
        string ss;
        cin>>n>>t>>ss;
        for(int i=0;i<n*t;i++)
            s[i]=ss[i%n]-'i'+2;
        n*=t;
        f[n-1]=s[n-1];
        for(int i=n-2;i>=0;i--)
            f[i]=cal(s[i],f[i+1]);
        int cur=s[0];
        bool flag=false;
        for(int i=0;i<n-2;i++)
        {
            if (cur==2){
                int cc=s[i+1];
                for(int j=i+1;j<n-1;j++)
                {
                    if (cc==3 && f[j+1]==4){
                        flag=true;
                        break;
                    }
                    cc=cal(cc,s[j+1]);
                }
            }
            if (flag)break;
            cur=cal(cur,s[i+1]);
        }
        cout<<"Case #"<<ii<<": ";
        if (flag)cout<<"YES\n";else cout<<"NO\n";
            
    }
    return 0;
}
