#include<iostream>
#include<cstdio>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
int t,n;
struct str
{
    int st;
    int idx;
};
str a[32];
vector<string> ans;
bool prov()
{
    for(int i=0;i<n;++i)if(a[i].st>0)return 1;
    return 0;
}
bool cmp(str p,str q)
{
    if(p.st>q.st)return 1;
    return 0;
}
int main()
{
    freopen("senate.out","w",stdout);
    int obsht=0;
    cin>>t;
    for(int k=1;k<=t;++k)
    {
        cin>>n;
        for(int i=0;i<n;++i)
        {
            cin>>a[i].st;
            a[i].idx=i;
            obsht+=a[i].st;
        }
        cout<<"Case #"<<k<<": ";
        while(prov())
        {
            sort(a,a+n,cmp);
            if(obsht==3)
            {
                char c=a[0].idx+'A';
                --a[0].st;
                cout<<c<<" ";
                --obsht;
                continue;
            }
            else
            {
                if(a[1].st>(obsht-2)/2)
                {
                    char c=a[0].idx+'A';
                    char c1=a[1].idx+'A';
                    cout<<c<<c1<<" ";
                    obsht-=2;
                    --a[0].st;
                    --a[1].st;
                }
                else
                {
                    char c=a[0].idx+'A';
                    a[0].st-=2;
                    cout<<c<<c<<" ";
                    obsht-=2;
                }
            }
        }
        cout<<"\n";
    }
    return 0;
}
