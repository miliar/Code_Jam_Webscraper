#include<cstdio>

int main()
{
	int t,a,b,con;
	int A[1001]={0};
	A[1]=A[4]=A[9]=A[121]=A[484]=1;
	scanf("%d",&t);
	for(int q=1;q<=t;q++)
	{	
		con=0;
		scanf("%d %d",&a,&b);
		for(int i=a;i<=b;i++)
			if(A[i]==1)
				con++;
		printf("Case #%d: %d\n",q,con);
	}
}
