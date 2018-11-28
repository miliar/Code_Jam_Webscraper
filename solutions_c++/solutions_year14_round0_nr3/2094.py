#include<cstdio>
#include<cstring>
char a[60][60];
int stack[10000];
int top,v,w,x,y,nn,ii,i,j,n,m,s;
bool flag;
void sc()
{ 
	int i,j;
	for (i=1;i<=n;i++)
	{
		for (j=1;j<=m;j++)
			printf("%c",a[i][j]);
		printf("\n");
	}
}
void dfs(int x,int y,int z)
{
	int i;
    if (z==0)
	{
		if (top>1)
		if (stack[1]==stack[2])
				flag=true;
		return;
	}
	if (z<0) return;
	if (x>n) return;
    for (i=y;i>=2;i--)
	{
       top++;stack[top]=i;
	   dfs(x+1,i,z-i);
	   if (flag) return;
	   top--;
	}
}
int main()
{


	scanf("%d",&nn);
	for (ii=1;ii<=nn;ii++)
	{
	   memset(a,0,sizeof(a));
	   scanf("%d%d%d",&n,&m,&s);
	   printf("Case #%d:\n",ii);
       w=n*m-s;
	   x=1;y=1;flag=false;
	   if (w==1)
	   {
		   for (i=1;i<=n;i++)
			   for (j=1;j<=m;j++)
				   a[i][j]='*';
			   a[1][1]='c';
			sc();
			continue;
	   }
       if ((n==1)||(m==1))
	   {
		   if (s>n*m-2)
              printf("Impossible\n");
		   else
		   {
			   for (i=n;i>=1;i--)
				   for (j=m;j>=1;j--)
                   if (s)
				   {
					   a[i][j]='*';s--;
				   }
				   else
					   a[i][j]='.';
		       a[1][1]='c';
			   sc();
		   }
		   continue;
	   }
	  
	  top=0;
      dfs(1,m,w);
	  
	  if (flag==false)
	  {
		  printf("Impossible\n");
		  continue;
	  }
      for (i=1;i<=n;i++)
		  for (j=1;j<=m;j++)
			  a[i][j]='*';
	  for (i=1;i<=top;i++)
		  for (j=1;j<=stack[i];j++)
			  a[i][j]='.';
	  a[1][1]='c';
	  sc();
   	}
}
		
