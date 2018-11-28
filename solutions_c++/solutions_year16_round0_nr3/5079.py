#include <cstdio>
#include <cstring>
using namespace std;
char a[17]="1000000000000001";
int cnt;
long long num[11];
long long isprime(long long x)
{
	for(long long i=2;i*i<=x;i++)
	{
		if(x%i==0)return i;
	}
	return -1;
}
void judge()
{
	for(int i=2;i<=10;i++)
	{
		long long int sum=0;
		for(int j=0;j<=15;j++)
		{
			sum*=i;
			sum+=a[j]-'0';
		}
		if(isprime(sum)==-1)return;
		else num[i]=isprime(sum);
	}
	cnt++;
	printf("%s",a);
	for(int i=2;i<=10;i++)printf(" %d",num[i]);
	printf("\n");
	return;
}
void dfs(int po)
{
	if(cnt==50)return;
	if(po==15){
		judge();
		return;
	}
	a[po]='0';dfs(po+1);
	a[po]='1';dfs(po+1);
}
int main()
{
	freopen("sample2.out", "w", stdout);
	printf("Case #1:\n");
	int n=16,j=50;
	cnt=0;
	dfs(1);
	return 0;
}