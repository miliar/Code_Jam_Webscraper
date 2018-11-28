#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<climits>
#define ll long long
using namespace std;
ll arr[15000][15000],p[4000],brr[4000];
int main()
{
    ll t,y=1,n;
    freopen("it.in","r",stdin);
    freopen("ot.out","w",stdout);
    cin>>t;
    while(t--)
    {
        memset(brr,0,sizeof(brr));
        cin>>n;
        for(int i=0;i<((2*n)-1);i++)
        {
            for(int j=0;j<n;j++)
            {
                cin>>arr[i][j];
                //cout<<"element is:"<<arr[i][j];
                brr[arr[i][j]]++;
            }
        }
        int j=0;
        //for(int i=0;i<2500;i++)
          //  cout<<brr[i]<<endl;
        for(int i=0;i<2500;i++)
        {
            if(brr[i]%2!=0)
                p[j++]=i;
        }
        cout<<"Case #"<<y<<": ";
        for(int i=0;i<j;i++)
            cout<<p[i]<<" ";
        cout<<endl;
        y++;
    }
return 0;
}
