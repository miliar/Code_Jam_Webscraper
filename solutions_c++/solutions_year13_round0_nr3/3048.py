#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int p[110];
bool palind(int n)
{
	int k;
	for(k=0;n;n/=10) p[k++]=n%10;
	for(int i=0;i+i<k;i++)
		if(p[i]!=p[k-i-1]) return false;
	return true;
}

int work(int n)
{
	int cnt=0;
	for(int i=1;i*i<=n;i++)
		if(palind(i) && palind(i*i)) cnt++;
	return cnt;
}

int main()
{
	int t,a,b;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		scanf("%d%d",&a,&b);
		printf("Case #%d: %d\n",i+1,work(b)-work(a-1));
	}
	return 0;
}
