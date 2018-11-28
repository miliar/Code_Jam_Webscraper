#include<stdio.h>
#include<iostream>
using namespace std;
int a[11][11];
int rcheck(int,int);
int ccheck(int,int);
main()
{   
    freopen ("B-small-attempt4.in", "r", stdin);
    freopen ("Q2small.in", "w", stdout);   
    int t,cases=1;
    scanf("%d",&t);
  while(t--)
  {
    int m,n,i,j;
    scanf("%d %d",&m,&n);
    for(i=1;i<=m;i++)
    {
    	for(j=1;j<=n;j++)
    	{
    		cin>>a[i][j];
    	}
   }
   int gt=0;
   cout<<"Case #"<<cases<<": ";
   for(i=1;i<=m;i++)
    {   
       if(gt==1)
       break;
    	for(j=1;j<=n;j++)
    	{    
    	    if(i==m&&j==n)
            {cout<<"YES\n";gt=1;break;   }
			else if(a[i][j]==2)
			{continue;}
    	    else if(rcheck(i,n)==1&&ccheck(j,m)==1)
    	    {cout<<"NO\n";gt=1;break;}    	     	    
    	}
    } 
    cases++;
  }
}
int rcheck(int g,int n)
{  int i;
   for(i=1;i<=n;i++)
   {   
       if(a[g][i]==2)
       return 1;
   }
}
int ccheck(int s,int m)
{  int i;
   for(i=1;i<=m;i++)
   {   
       if(a[i][s]==2)
       return 1;
   }
}
