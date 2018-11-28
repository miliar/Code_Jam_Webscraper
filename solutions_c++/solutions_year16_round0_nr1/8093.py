#include<bits/stdc++.h>
using namespace std;
#define ll long long
ll m,n,i,j,d,t,z;
int main()
{
    ios_base::sync_with_stdio(0);
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
   cin>>t;
   while(t--)
   {
       cin>>n;
       if(n==0)
       {
           cout<<"Case #"<<++z<<": INSOMNIA\n";
           continue;
       }
       map<ll,ll>mp;
       d=0;j=1;
       while(d<10)
       {
           d=0;
           m=j*n;
           while(m)
           {
               mp[m%10]=1;
               m/=10;
           }
           for(i=0;i<=9;i++)
            if(mp[i]==1)
            d++;
            j++;
       }
       --j;
       cout<<"Case #"<<++z<<": "<<j*n<<endl;
   }
}
