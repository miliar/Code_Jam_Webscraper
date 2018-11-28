#include<cstdio>
#include<iostream>
using namespace std;

double liczby[1000005];
double pref[1000005];

int main()
{
	ios_base::sync_with_stdio(0);
	double wynik, C, F, X, pom;
	int testy;
	
	cin >> testy;
	for(int j=1; j<=testy; j++)
	{
		cin >> C >> F >> X;
		liczby[0]=C/2;
		pref[0]=liczby[0];
		for(int i=1; i<=1000000; i++)
		{
			liczby[i]=C/(i*F+2);
			pref[i]=pref[i-1]+liczby[i];
		}
		
		wynik=X/2;
		
		for(int i=1; i<=1000000; i++)
		{
			pom=pref[i-1]+X/(i*F+2);
			if(pom<wynik) wynik=pom;
			else break;
		}
		
		printf("Case #%d: ", j); 
		printf("%.7f\n", wynik);
	}
	
	cin.ignore();
	getchar();
	return 0;
}



