#include<cstdio>
#include<iostream>
using namespace std;

long long N,P;
int T;

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	long long i;
	cin >> T;
	for (int cases=1;cases<=T;cases++)
	{
		cin >> N >> P;
		cout << "Case #"<< cases <<": ";
		if (P == 1LL << N)
		{
			cout << (1LL<<N)-1 << " " << (1LL<<N)-1 << "\n";
			continue;
		}
		long long p = P;
		i = N;
		while (p > 0)
		{
			--i;
			p -= 1LL<<i;
		}
		cout << (1LL << (N-i))-2 << " ";
		long long n = 1LL << N, ans = 1LL << N;
		i = N;
		while (n > P)
		{
			--i;
			n -= 1LL << i;
		}
		ans -= 1 << (N-i);
		cout << ans << "\n";
	}
	return 0;
}
