using namespace std;
#include<cstdio>
#include<cstring>
#include<cmath>
long long pal(long long x)
{
	int f[107];
	memset(f, 0, sizeof(f));
	long long pos = 0;
	while(x)
	{
		f[pos++] = x%10;
		x/=10;
	}
	pos--;
	for(long long i = 0; i <= pos/2; ++i)
		if(f[i] != f[pos-i])
			return 0;
	return 1;
}
int main()
{
	freopen("file.in", "r", stdin);
	freopen("file.out", "w", stdout);
	long long T,  i, j,a,b;
	long long test = 1;
	scanf("%lld", &T);
	while(T--)
	{
		scanf("%lld%lld",&a,&b);
		long long cnt = 0;
		for(long long i = a; i <= b; ++i)
		{
			if(sqrt(i) == (int)sqrt(i))
			{
				if(pal( (int)sqrt(i)) && pal(i)) {
					++cnt;
					//printf("%d %d\n", (int)sqrt(i), i);
				}
			}
		}
		printf("Case #%lld: %lld\n", test, cnt);
		++test;
	}
	return 0;
}