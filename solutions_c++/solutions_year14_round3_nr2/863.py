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

int sprawdzPoprawnosc(string jakisString)
{
	int znaki[256] = {0};
	znaki[jakisString[0]] = 1;
	
	REPN(i,jakisString.size()-1)
	{
		if((jakisString[i] != jakisString[i-1]) && (znaki[jakisString[i]] != 0)) return 0;
		else znaki[jakisString[i]] = 1;
	}
	return 1;
}

int main()
{
	string wagon[11];
	VI numerki;
	int T, ileWagonow;
	long long int wynik;
	cin>>T;
	
	REPN(i,T)
	{
		wynik = 0;
		numerki.clear();
		cin>>ileWagonow;
		REP(j,ileWagonow) {cin>>wagon[j]; numerki.push_back(j);}
		
		do
		{
			string superString = "";
			REP(x,numerki.size()) superString += wagon[numerki[x]];
			wynik += sprawdzPoprawnosc(superString);
						
		} while(next_permutation(numerki.begin(), numerki.end()));
		
		printf("Case #%d: %lld\n", i, wynik);
		
	}
}
