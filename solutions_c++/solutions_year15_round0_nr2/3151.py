#include<iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;
int T,ti;
int n,x[2000];
int l,r,mid;
int ans,tans;
int maxn(int x,int y){return x>y?x:y;}
int minn(int x,int y){return x<y?x:y;}
int main()
{
        freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    cin>>T;
    while(T--)
    {
        ans=0;
        cin>>n;
        for(int i=0;i<n;i++)
        {
            cin>>x[i];
            ans=maxn(ans,x[i]);
        }
        for(int i=1;i<ans;i++)
        {
            tans=0;
            for(int j=0;j<n;j++)
            {
                if(x[j]>i){tans+=(x[j]-1)/i;}
            }
            tans+=i;
            ans=minn(ans,tans);
        }
        cout<<"Case #"<<++ti<<": ";
        cout<<ans<<endl;
    }

}
