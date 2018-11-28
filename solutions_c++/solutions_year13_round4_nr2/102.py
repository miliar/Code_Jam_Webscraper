#include <iostream>

using namespace std;

long long p2[51];

void genP2()
{
	p2[0] = 1;
	for (int i=1; i<=50; i++)
	{
		p2[i] = 2*p2[i-1];
	}
}

long long maxPos(int N, long long k)
{
	long long pos = 0;
	for (int i=0; p2[i] <= k; i++)
	{
		k -= p2[i];
		pos += p2[N-i-1];
	}
	return pos;
}

long long minPos(int N, long long k)
{
	long long n2 = (1L << N);
	return n2 - maxPos(N, n2-k-1) - 1LL;
}

void doCase()
{
	int N;
	long long P;
	
	cin >> N >> P;
	
	long long low = 0, high = (1L << N);
	
	while (high - low > 1)
	{
		long long mid = (high+low)/2;
		if (maxPos(N, mid) >= P)
			high = mid;
		else
			low = mid;
	}
	cout << low << " ";
	
	low = 0;
	high = (1LL << N);
	while (high - low > 1)
	{
		long long mid =  (high + low)/2;
		if (minPos(N, mid) >= P)
			high = mid;
		else
			low = mid;
	}
	cout << low << endl;
}

int main()
{
	genP2();
	int T;
	cin >> T;
	for (int i=1; i<=T; i++)
	{
		cout << "Case #" << i << ": ";
		doCase();
	}
	return 0;
}
