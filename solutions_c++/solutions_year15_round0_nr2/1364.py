#include<iostream>
#include<string>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<vector>
#include<set>
#define ll long long int
#define mk make_pair
#define pb push_back
using namespace std;


int main()
{
    int t,w=1;
    freopen("input.in","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    while(t--)
    {
        int i,j,k,l,m,n,d,arr[1111]={0};
        cin>>d;
        for(i=1;i<=d;i++)
        {
            cin>>n;
            arr[n]++;
        }
        int ans=1000,co=0;
        for(i=1;i<=1000;i++)
        {
            int temp=i;
            for(j=1;j<=1000;j++)
            {
                if(arr[j]&&j>=i)
                {
                    n=j/i;
                    m=(n*i==j)?n-1:n;
                    m=m*arr[j];
                    temp+=m;
                }
            }
            ans=min(ans,temp);
        }
        cout<<"Case #"<<w<<": "<<ans<<"\n";
        w++;
    }
    return 0;
}
