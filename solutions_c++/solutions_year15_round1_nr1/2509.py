#include <bits/stdc++.h>
using namespace std;
bool comp(int a,int b)
{
    return (a>b);
}
int gcd(int a,int b)
{
    if(b==0)
        return a;
    else
        return gcd(b,a%b);
}
int main(void) {
    freopen("in.txt","rt",stdin);
    freopen("test.txt","wt",stdout);
    int t,i,n;
    scanf("%d",&t);
    for(i=1;i<=t;++i)
    {
        cin>>n;
        cout<<"Case #"<<i<<": ";
        int a[n],j,c1=0,m=0,c2=0;
        for(j=0;j<n;++j)
            cin>>a[j];
        for(j=0;j<n-1;++j)
        {
            if(a[j]>a[j+1])
            {
                c1+=a[j]-a[j+1];
                m=max(m,a[j]-a[j+1]);
            }
        }
        for(j=0;j<n-1;++j)
            c2+=min(m,a[j]);
        cout<<c1<<" "<<c2<<"\n";
    }
    return 0;
}
