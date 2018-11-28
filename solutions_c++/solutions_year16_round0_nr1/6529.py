#include<bits/stdc++.h>
typedef long long int ll;
using namespace std;
ll arr[1000000];
ll  m;
int main()
{
    freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);


    ll x,i;
    ll d,valu,k,rabby=0,j;

    cin>>x;
    for(i=1;i<=x;i++)
    {
    cin>>m;
    if(m==0)
    cout<<"Case #"<<i<<": INSOMNIA"<<endl;
    else
    {

    for(k=0;k<10;k++)
    arr[k]=0;
    for(j=1;;j++)
    {
       valu=m*j;
       rabby=1;
       while(valu!=0)
       {
          d=valu%10;
          ++arr[d];
          valu=valu/10;
       }
       for(k=0;k<10;k++)
       if(arr[k]==0)
       rabby=0;
       if(rabby==1)
       break;
    }
       rabby=0;
       for(k=0;k<10;k++)
       if(arr[k]==0)
       rabby=1;
       if(rabby!=1)
    cout<<"Case #"<<i<<": "<<m*j<<endl;
    }
    }

    return 0;
}
