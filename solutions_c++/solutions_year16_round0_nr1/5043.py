#include <cstdio>
#include <cstdlib>

using namespace std;

int check [10];
int flag=0;
int t=0;
int con;
void f(int x)
{	
	//printf("%d\n",x );
	//int tmp = x;
	if (flag)
		return;
	int cnt=0;
	for (int i = 0; i < 10; ++i)
	{	
		if(check[i])
			cnt++;
	}
	if (cnt==10)
		flag=1;
	if (flag)
	{
		printf("%d\n",x-con );
		return;
	}
	while((x/10)!=0)
	{
		check[x%10]=1;
		x=x/10;
	}
	check[x]=1;
	t++;
	f(t*con);
}
int main()
{
	int n ;
	scanf("%d",&n);
	for (int i = 0; i < n; ++i)
	{
		int x ;
		scanf("%d",&x);
		con=x;
		if (x==0)
			printf("Case #%d: INSOMNIA\n", i+1);
		else
		{	
			flag=0;
			t=1;
			for (int i = 0; i < 10; ++i)
				check[i]=0;
			printf("Case #%d: ", i+1);
			f(x);
		}	
	}
	return 0;
}