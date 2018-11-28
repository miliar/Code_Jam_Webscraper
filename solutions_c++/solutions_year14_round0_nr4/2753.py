#include<iostream>
#include<algorithm>
#include<stdio.h>
using namespace std;
int main()
{freopen("D-large.in","r",stdin);
freopen("out.txt","w",stdout);
int b,i,p,nw=0.0,dw=0.0,j,t;
float n[1002],k[1002],n1[1002],k1[1002];
cin>>t;
for(p=0;p<t;p++)
{nw=0.0,dw=0.0;
cin>>b;
for(i=0;i<b;i++)
{cin>>n[i];}
for(i=0;i<b;i++)
{cin>>k[i];}
sort(n,n+b);
sort(k,k+b);
for(i=0;i<b;i++)
{n1[i]=n[i];
 k1[i]=k[i];
}
for(i=0;i<b;i++)
{for(j=0;j<b;j++)
	{if(n[i]<k[j]&&k[j]!=0.0&&n[i]!=0.0)
	  {n[i]=0.0;
	   k[j]=0.0;
	  }
	}
}
for(i=0;i<b;i++)
{if(n[i]!=0.0)
nw++;
}
for(i=0;i<b;i++)
{for(j=0;j<b;j++)
	{if(n1[i]>k1[j]&&k1[j]!=0.0&&n1[i]!=0.0)
	  {n1[i]=0.0;
	   k1[j]=0.0;
	  }
	}
}
for(i=0;i<b;i++)
{if(n1[i]==0.0)
dw++;
}cout<<"Case #"<<p+1<<": "<<dw<<" "<<nw<<"\n";
}
return 0;	
}