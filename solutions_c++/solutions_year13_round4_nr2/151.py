#include <cstdio>
#include <algorithm>

using namespace std;

long long all;
long long p;
long long n;

void read()
{
	scanf("%lld%lld", &n, &p);
	all = (1LL << n);
}
bool isAbleToWin(long long k, long long left, long long prizes)
{
	if(k != 0 && prizes <= left/2) return false;
	if(k == 0) return true;
	return isAbleToWin((k-1)/2, left/2, prizes - left/2);
}
bool isAbleToWin2(long long k, long long left, long long prizes)
{
	//printf("computing isAbleToWin2 %lld %lld %lld\n", k, left, prizes);
	if(prizes == left) return true;
	if(k == left-1) return false;
	return isAbleToWin2(left/2-(left-k-2)/2 -1,left/2, min(prizes, left/2));
}
long long binSearch()
{
	long long q = 0, w = all-1;
	while(w-q > 1)
	{
		long long s = (w+q)/2;
		if(isAbleToWin(s, all, p))
			q = s;
		else
			w = s;
	}
	if(isAbleToWin(w, all, p))
		return w;
	return q;
}
long long binSearch2()
{
	long long q = 0, w = all-1;
	while(w-q > 1)
	{
		long long s = (w+q)/2;
		//printf("%lld:isAbleToWin2: %d\n", s, isAbleToWin2(s,all,p));
		//printf("%lld %lld\n", all, p);
		if(isAbleToWin2(s, all, p))
			q = s;
		else
			w = s;
	}
	if(isAbleToWin2(w, all, p))
		return w;
	return q;
}
void solve(int tc)
{
	long long first = binSearch();
	long long second = binSearch2();
	printf("Case #%d: %lld %lld\n", tc, first, second);
}
int main()
{
	int Z;
	scanf("%d", &Z);
	for(int i = 1;i<=Z;i++)
	{
		read();
		solve(i);
	}
	return 0;
}
