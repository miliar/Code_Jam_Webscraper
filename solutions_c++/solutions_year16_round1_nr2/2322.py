#include<bits/stdc++.h>
#include<algorithm>
#define ll long long int
using namespace std;
int main()
{
    ll t,i,j,k,p,n;
    cin>>t;
    int a[3000];
    vector<int> v;
    vector<int>::iterator it;
    for(j=1;j<=t;j++)
    {
        memset(a,0,sizeof(int)*3000);
        scanf("%lld",&n);
        for(i=0;i<2*n-1;i++)
        {
            for(k=0;k<n;k++)
            {
                scanf("%lld",&p);
                a[p]++;
            }
        }
        for(i=1;i<2600;i++)
        {
            if(a[i]%2!=0)
                v.push_back(i);
        }
        sort(v.begin(),v.end());
        cout<<"Case #"<<j<<": ";
        for(it=v.begin();it!=v.end();it++)
            cout<<*it<<" ";
        v.clear();
        cout<<endl;
    }
    return 0;
}
