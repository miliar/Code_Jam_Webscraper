#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
using namespace std;
char buf[555];
long long test=1;
inline bool cc(long long a)
{
	for(;a>1;a/=2)
	{
		if(a%2==1) return false;
	}
	return true;
}
inline long long Euclid(long long a, long long b)
{
	if(a>=b)
	{
		if(a%b==0)
			return b;
		else
			return Euclid(b,a%b);
	}
	else
	{
		if(b%a==0)
			return a;
		else
			return Euclid(a,b%a);
	}
}
void solve()
{
	char* ptr;
	long long n,m;
	long long g;
	string s;
	scanf("%s",buf);
	ptr = strtok(buf,"/");
	s = ptr;
	n = stoll(s);
	ptr = strtok(NULL,"/");
	s = ptr;
	m = stoll(s);
	g = Euclid(n,m);
	n /= g;
	m /= g;
	if( cc(m) == false )
	{
		printf("Case #%d: impossible\n",test);
		test++;
		return;
	}
	long long cnt = 0;
	while( n < m )
	{
		if( m % 2 == 1 ) 
		{
			printf("Case #%lld: impossible\n",test);
			test++;
			return;
		}
		m /= 2;
		cnt++;
	}
	printf("Case #%lld: %lld\n",test,cnt);
	test++;
	return;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	long long t;
	cin >> t;
	while(t--)
	{
		memset(buf,0,sizeof(buf));
		solve();
	}
	return 0;
}