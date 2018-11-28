#include <bits/stdc++.h>
typedef long long int ll;
using namespace std;
int main()
{
    freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);
    ll t,n,i,j,m,cou;
    char arr[100000];
    cin>>t;
    for(i=1;i<=t;i++)
    {
    cou=0;
    cin>>arr;
    n=strlen(arr);
    if(arr[n-1]=='-')
    m=1;
    else
    m=0;
    for(j=0;j<n-1;j++)
    if(arr[j]!=arr[j+1])
    cou++;
    cou=cou+m;
    cout<<"Case #"<<i<<": "<<cou<<endl;
    }
    return 0;
}
