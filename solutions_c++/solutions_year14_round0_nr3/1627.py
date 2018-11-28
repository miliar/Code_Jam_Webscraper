#include<cstdio>
#include<iostream>
#include<vector>
#include <algorithm>
#include<deque>
   using namespace std;
    bool create(int R,int C,int a[51][51],int i,int j,int n,int &count)
{  
   int r,s;
   bool c=false;
    for(r=i-1;r<=i+1;r++)
		     for(s=j-1;s<=j+1;s++)
		     {
		       if(r<0||r>=R||s<0||s>=C)
			 continue;
		       if(a[r][s]==0)
		       {a[r][s]=n;
		        count=count+1;
			c=true;}
		     }
    return c;
}
   void rec(int R,int C,int space,int a[51][51],int n,int &count)
   {
    if(count>space)
    {cout<<count<<" "<<space<<endl;
            return;}
    int i,j,r,s;
    for(i=0;i<R;i++)
	for(j=0;j<C;j++)
	{
	 if((n==1||a[i][j]>0)&&create(R,C,a,i,j,n,count))
	 {
	   rec(R,C,space,a,n+1,count);
	  if(count!=space)
		  for(r=i-1;r<=i+1;r++)
		     for(s=j-1;s<=j+1;s++)
		     {
		       if(r<0||r>=R||s<0||s>=C)
			    continue;
		       if(a[r][s]==n)
		       {a[r][s]=0;
		        count--;}
		     }
	 }
	 {for(r=0;r<R;r++){
		  for(s=0;s<C;s++)
			  printf("%d ",a[r][s]);
		  cout<<endl;}
	 printf("qqq%d %d %d %d\n",i,j,n,count);}
	 if(count==space&&n==1)
	 {a[i][j]=-1;
	  return;}
	 if(count==space)
		 return;
	 /*if(n==10)
	 {for(r=0;r<R;r++){
		  for(s=0;s<C;s++)
			  printf("%d ",a[r][s]);
		  cout<<endl;}
	 printf("%d %d\n",i,j);}*/
	 if(count>space)
           {
		   //cout<<n<<" "<<count<<" ";
		   for(r=i-1;r<=i+1;r++)
		     for(s=j-1;s<=j+1;s++)
		     {
		       if(r<0||r>=R||s<0||s>=C)
			    continue;
		       if(a[r][s]==n)
		       {a[r][s]=0;
		        count--;}
		     }
		   //if(n==1)
	
		   //cout<<count<<endl;
	   }
	}
   }
  int main()
{
	int a[51][51];
	int N,i,tn,t,j,R,C,M,s;
	int n,count;
	scanf("%d",&tn);
	for(int k=1;k<=tn;k++)
	{
	  scanf("%d %d %d",&R,&C,&M);
	  s=R*C-M;
	  for(i=0;i<R;i++)
		  for(j=0;j<C;j++)
			  a[i][j]=0;
	  n=1;count=0;
	  if(s!=1)
	  rec(R,C,s,a,n,count);
          if(s==1)
            {count=1;
            a[0][0]=-1;}
          printf("Case #%d:\n",k);
	  if(count!=s)
            printf("Impossible\n");
          if(count==s)
	   {	  
	   for(i=0;i<R;i++)
		{for(j=0;j<C;j++)
		  {if(a[i][j]==-1)
		   {printf("c");
		   continue;}
	          if(a[i][j]==0)
			  printf("*");
		  else
			  printf(".");
		  }
		  cout<<endl;
		}
	   }
	}
	return 0;
}




