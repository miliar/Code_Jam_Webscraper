#include<iostream>
#include<string.h>
#include<algorithm> 
#include<math.h>
using namespace std;
typedef long long int ll;
int main()
{freopen("A-large.in","r",stdin);
 freopen("output.txt","w",stdout);
ll l,t;
cin>>t;
for(l=1;l<=t;l++)
{

ll n,loc,max=0,i,total=0;
cin>>n;
ll party[26];
for(i=0;i<n;i++)
{cin>>party[i];
total=total+party[i];
if(max<party[i])
{max=party[i];
loc=i;
}
}
cout<<"Case #"<<l<<": ";
if(n==2)
{while(total>0)
{cout<<char(65)<<char(66)<<" ";
total=total-2;
}
}
else{
while(total>0)
{
if(total==2)
{for(i=0;i<n;i++)
 {if(party[i]!=0)
  cout<<char(65+i);
 }
 total=0;
}
else{
cout<<char(65+loc)<<" ";
party[loc]--;
max=0;
for(i=0;i<n;i++)
{if(max<party[i])
{max=party[i];
loc=i;
}
}
total--;
}

}
}
cout<<endl;

}
return 0;
}
