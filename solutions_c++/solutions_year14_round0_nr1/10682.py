#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{ int t,a[4][4],b[4][4],j,i,p,q,u,x;
  freopen ("aa.in","r",stdin);
  scanf("%d",&t);
  freopen ("myfile.txt","w",stdout);
  for(int k=1;k<=t;k++)
  {
		scanf("%d",&p);
		p--;
		u=0;
		for(i=0;i<4;i++)
		{
		      for(j=0;j<4;j++)
		      scanf("%d",&a[i][j]);
        }
        scanf("%d",&q);
        q--;
        for(i=0;i<4;i++)
		{
		      for(j=0;j<4;j++)
		      scanf("%d",&b[i][j]);
        }
        for(i=0;i<4;i++)
        {
		      for(j=0;j<4;j++)
		      {
  				  if(a[p][i]==b[q][j])
  				  {
 					  u++;
 					  x=a[p][i];
 				  } 
   			  }
        }
        cout<<"Case #"<<k<<": ";
		if(u==1)
		cout<<x<<"\n";
		else if(u==0)
		cout<<"Volunteer cheated!\n";
		else
		cout<<"Bad magician!\n";
  }
}		 	  
