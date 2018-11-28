#include <cstdio>
#include <cmath>
#include <cstring>
using namespace std;

bool is_pal(long long n)
{
	char s[20];
	sprintf(s, "%I64d", n);
	int l = strlen(s);
	for(int i=0; i<l/2; i++)
		if(s[i]!=s[l-i-1]) return false;
	return true;
}

bool check(long long n)
{
	if(!is_pal(n)) return false;
	long long sq = (long long)sqrt(n);
	if(sq*sq==n && is_pal(sq)) return true;
	return false;
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int t=1; t<=T; t++)
	{
		long long a, b;
		scanf("%I64d%I64d", &a, &b);
		long long cnt = 0;
		for(long long i=a; i<=b; i++)
			if(check(i)) cnt++;
		printf("Case #%d: %I64d\n", t, cnt);
	}
	return 0;
}
