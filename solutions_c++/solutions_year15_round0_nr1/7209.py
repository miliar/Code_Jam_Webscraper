#include<iostream>
#include<cmath>
#include<string.h>
#include<algorithm>
#include<vector>
#include<queue>
#include<stdlib.h>
#include<set>
#include<ctype.h>
#include<cstdio>
#include<map>
using namespace std;
typedef long long int ll;
ll arr[100000];
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    ll t,a;
    cin>>t;
    for(ll i=1;i<=t;i++)
    {
        cout<<"Case #"<<i<<": ";
        ll sum=0,non=0;
        cin>>a;
        getchar();
        for(ll j=0;j<=a;j++)
        {
            arr[j]=getchar()-48;
            //cout<<arr[j];
            //cin>>arr[j];
        }
        for(ll j=0;j<=a;j++)
        {
            if(sum>=j)
            sum+=arr[j];
            else if(arr[j]!=0)
            {
                non+=(j-sum);
                sum+=(j-sum)+arr[j];
            }
        }
        cout<<non<<endl;
    }
    return 0;
}

