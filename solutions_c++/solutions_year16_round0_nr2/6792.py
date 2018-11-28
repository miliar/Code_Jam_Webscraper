#include <bits/stdc++.h>
using namespace std;

# define ll long long int

int main()
{
	// your code goes here
freopen("B-large.in","r",stdin);
freopen("new.out","w",stdout);
ll i,ctr,l,t,f=1;

char str[1000];
cin>>t;
while(t--)
{
cin>>str;
cout<<"Case #"<<f<<": ";
ll sum=0;
l=strlen(str);
ll ar[l];
for(i=0;i<l;i++)
 {
     if(str[i]=='-')
     {
     ar[i]=0;
     }
     else
      {
          ar[i]=1;
      }
      sum+=ar[i];
 }
 ctr=0;
while(sum!=l)
 {i=0;
 sum=0;
 if(ar[i]==0)
  {
    while(ar[i]!=1&&i<l)
     {
     ar[i]=1;
     i++;
     }
  }
  else
    {
     while(ar[i]!=0&&i<l)
     {
     ar[i]=0;
     i++;
     }
    }
    for(i=0;i<l;i++)
    {
     if(ar[i]==1)
     {
     sum++;
     }
    }
    //cout<<sum;
     ctr++;
 }

 cout<<ctr<<endl;
 f++;
}
	return 0;

}
