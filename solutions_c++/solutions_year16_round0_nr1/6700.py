#include <bits/stdc++.h>
using namespace std;

# define ll unsigned long long int

int main()
{
	// your code goes here
	freopen("A-large.in","r",stdin);
freopen("new.out","w",stdout);
ll n,t,temp,i,temp2,ar[10],ctr,j,f=0;
cin>>t;
while(t--)
{i=1;
f++;
cout<<"Case #"<<f<<": ";
for(j=0;j<10;j++)
 {
     ar[j]=0;
 }
 ctr=0;
    cin>>n;
    if(n==0)
    {
    cout<<"INSOMNIA"<<endl;
    continue;

    }

while(ctr<10)
{
temp=n*i;
temp2=temp;
while(temp!=0)
 {

// cout<<temp<<endl;

 if(ar[temp%10]==0)
  {
    ar[temp%10]++;
    ctr++;
  }

  temp=temp/10;
 }
 i++;
// cout<<ctr<<endl;
}
cout<<temp2<<endl;
}
	return 0;

}
