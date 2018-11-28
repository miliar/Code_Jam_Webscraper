#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
using namespace std;
double a[1005];
double b[1005];
int n;
void solve1()
{
    sort(a,a+n);
    sort(b,b+n);
    int amin=0;
    int amax=n-1;
    int bmin=0;
    int bmax=n-1;
    int ans1=0;
    while(amin<=amax)
    {
        if(a[amax]>b[bmax])
        {
            ans1++;
            amax--;
            bmax--;
        }
        else if(a[amin]>b[bmin])
        {
            ans1++;
            amin++;
            bmin++;
        }
        else
        {
            if(a[amin]<b[bmax])
            {
                amin++;
                bmax--;
            }
        }
    }
    cout<<ans1;
}
void solve2()
{
    sort(a,a+n);
    sort(b,b+n);
    int amin=0;
    int amax=n-1;
    int bmin=0;
    int bmax=n-1;
    int ans2=0;
    while(bmin<=bmax)
    {
        if(b[bmax]>a[amax])
        {
            ans2++;
            bmax--;
            amax--;
        }
        else if(b[bmin]>a[amin])
        {
            ans2++;
            bmin++;
            amin++;
        }
        else
        {
            if(b[bmin]<a[amax])
            {
                bmin++;
                amax--;
            }
        }
    }
    cout<<n-ans2;
}
int main()
{
    int T;
    freopen("D-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>T;
    for(int tt=1;tt<=T;tt++)
    {
        cin>>n;
        for(int i=0;i<n;i++)
        {
            cin>>a[i];
        }
        for(int i=0;i<n;i++)
        {
            cin>>b[i];
        }
        cout<<"Case #"<<tt<<": ";
        solve1();
        cout<<" ";
        solve2();
        cout<<endl;
    }
    return 0;
}
