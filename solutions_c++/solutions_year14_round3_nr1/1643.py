#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<cstring>
#include<array>
#include<list>
#define REP(I,N) for(int I = 0; I < N; ++I)
#define REPN(I,N) for(int I = 1; I <= N; ++I)
using namespace std;
typedef vector<int> VI;

long long int potegi[45];

long long int nwd(long long int a, long long int b)
{
  if (a==0) return b;
  return nwd(b%a, a);
}

int main()
{
	potegi[0] = 1;
	REPN(i, 44) potegi[i] = potegi[i-1]*2;
	
	int T, placeholder, kejs = 1;
	long long int licznik, mianownik;
	scanf("%d", &T);
	
	while(T--)
	{
		int i;
		scanf("%lld %c %lld", &licznik, &placeholder, &mianownik);
		int dzielnik = nwd(licznik, mianownik);
		licznik /= dzielnik;
		mianownik /= dzielnik;
		
		if(binary_search(potegi, potegi+44, mianownik))
		{
			for(i = 1; i <= 41; ++i)
			{
				if(licznik >= mianownik/2) break;
				mianownik /= 2;
			}
			
			if(i < 41) printf("Case #%d: %d\n", kejs++, i);
			else printf("Case #%d: impossible\n", kejs++);
		}	
		else printf("Case #%d: impossible\n", kejs++);
	}	
}
