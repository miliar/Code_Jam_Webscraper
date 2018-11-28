/*
 * =====================================================================================
 *
 * Nazwa pliku:  	C.cpp
 * Autor:		Szymon Stankiewicz (Daku)
 * Kontakt:		dakurels@gmail.com
 * Stworzony:		13.04.2013 21:31:18
 *
 * =====================================================================================
 */
#include<cstdio>
#include<vector>
#include<algorithm>

using namespace std;

const long long MAX_N=10000000LL;

long long reverse(long long x)
{
	long long out=0;
	while(x>0)
	{
		out*=10;
		out+=x%10;
		x/=10;
	}
	return out;
}

vector<long long> pali;

long long P, K;

int licz()
{
	int ile=0;
	scanf("%lld %lld", &P, &K);
	for(vector<long long>::iterator it=pali.begin(); it!=pali.end(); it++)
		if(P <= *it && *it <= K)
			ile++;
	return ile;
}

int N;

int main()
{
	for(long long i = 1; i<=MAX_N; i++)
		if(i==reverse(i) && i*i==reverse(i*i))
			pali.push_back(i*i);
	scanf("%d", &N);
	for(int i = 1; i<= N; i++)
		printf("Case #%d: %d\n", i, licz());
	return 0;
}
