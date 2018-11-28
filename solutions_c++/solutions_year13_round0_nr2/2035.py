#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
int t;
scanf("%d",&t);
int temp=1;
while(temp<=t)
{
int n,m;
scanf("%d%d",&n,&m);
int ar[n][m];
int set[n][m];
//for(int i=0;i<n;i++)
//r[i]=-1;satr[i]=-1;
//for(int i=0;i<m;i++)
//c[i]=-1;satc[i]=-1;
bool f=true;
int max=0;
int posi=-1;
int posj=-1;
	for(int i=0;i<n;i++)
	for(int j=0;j<m;j++)
	{ scanf("%d",&ar[i][j]);
	  if(max<ar[i][j])
	  {max=ar[i][j];
	   posi=i;
	   posj=j;
	  }
	}
	if(max==1)
	{ cout<<"Case #"<<temp<<": YES"<<endl;
	  
	}
	else
	{
	
	//cout<<"pos "<<posi<<" "<<posj<<endl;
	for(int i=0;i<n;i++)
	for(int j=0;j<m;j++)
	set[i][j]=max;
	/*for(int i=0;i<n;i++)
	for(int j=0;j<m;j++)
	  if(ar[i][j]==max)
		{	
		 r[i]=1;
		 c[j]=1;
		}*/
	for(int i=0;i<n;i++)
	{  if(i !=posi)
	  for(int j=0;j<m;j++)
	   { set[i][j]=min(ar[i][posj],set[i][j] );
	   }	
	}
	for(int j=0;j<m;j++)
	{ if(j!=posj)
	   {
	     for(int i=0;i<n;i++)
	     {
	      set[i][j]=min(ar[posi][j],set[i][j]);
	     }
	   }
	}
	for(int i=0;i<n;i++)
	{for(int j=0;j<m;j++)
	 { if(set[i][j]!=ar[i][j])
	   { f=false;
	     break;
	   }
	 }
	 if(f==false)
	  break;
	}
	if(f==true)
	 cout<<"Case #"<<temp<<": YES"<<endl;
	 else
	 cout<<"Case #"<<temp<<": NO"<<endl;
	 

	}
temp++;
}
}
