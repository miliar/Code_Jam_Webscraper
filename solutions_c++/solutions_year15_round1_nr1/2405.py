#include<iostream>
#include<cmath>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<map>
#define x first
#define y second
#define intpair pair<int,int>
#define ll long long
using namespace std;
int n,a[10010],ans2;
bool check(int k)
{
    ans2=0;
    for(int i=1;i<n;i++)
        {if(a[i]>a[i+1])
        {
            if(a[i]-a[i+1]>k) return false;
            if(a[i]<k)
                ans2+=a[i];
            else ans2+=k;
        }
        else
        {
            ans2+=min(k,a[i]);
        }
        }
    return true;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("ans1.txt","w",stdout);
    int t,cas=0;
    cin>>t;
    while(t--)
    {
        cin>>n;
        for(int i=1;i<=n;i++)
            scanf("%d",&a[i]);
        int ans1=0;
        for(int i=1;i<n;i++)
            if(a[i]>=a[i+1]) ans1+=a[i]-a[i+1];
        for(int i=0;i<=10000;i++)
            if(check(i))
                break;
        cout<<"Case #"<<++cas<<": "<<ans1<<' '<<ans2<<endl;

    }
}
