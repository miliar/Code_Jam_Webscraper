#include <bits/stdc++.h>
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define ft first
#define sd second
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef unsigned int uint;

using namespace std;

int ile_t;

struct Test
{
	int n, k;
	vector < double > V;
	void wczytaj()
	{
		cin>>n>>k;
		V.resize(n);
		for(auto& el : V)
			cin>>el;
		sort(V.begin(), V.end());
		////////////////////////////////////////////////////////////to uzupelnic
	}
};

struct Odp
{
	double p;
	Odp(){p = 0.0;}
	void wypisz(int nr)
	{
		printf("Case #%d: ", nr);
		cout << p;
		/////////////////////////////////////////////////////////tu uzupelnić	
		printf("\n");
	}
};

Test* testy;
Odp* odpowiedzi;

void zrob(int nr)
{
	if (nr >= ile_t)
		return;
	Test& in = testy[nr];
	Odp& out = odpowiedzi[nr];
	////////////////////////////////////////////////////////////to uzupelnic
	int n = in.n, k = in.k;
	vector < double >& PR = in.V;

	for(int i=0; i<=k; i++)
	{	
		vector < bool > czy(n, 0);
		for(int j=0; j<i; j++)
			czy[j] = 1;
		for(int j=0; j<k-i; j++)
			czy[n-j-1] = 1;

		vector < double > V(220, 0);
		V[110] = 1;
		
		for(int j=0; j<n; j++)
		{
			if ( czy[j] == 0)
				continue;
			vector < double > Pom(220, 0);
			for(int k=1; k<218; k++)
				Pom[k] = V[k-1] * PR[j] + V[k+1] * (1.0 - PR[j]);
			V = Pom;
		}
		out.p = max(out.p, V[110]);
	}
}

int main()
{
	cout << setprecision(10) << fixed;
	const int ile_watkow = 10;
	cin>>ile_t;
	testy = new Test[ile_t];
	odpowiedzi = new Odp[ile_t];
	for(int i=0; i<ile_t; i++)
		testy[i].wczytaj();
	for(int i=0; i*ile_watkow<ile_t; i++)
	{
		vector < thread > V;
		for(int j=0; j<ile_watkow; j++)
			V.push_back( thread(zrob, i*ile_watkow + j) );
		for(auto& el : V)
			el.join();
	}
	for(int i=0; i<ile_t; i++)
		odpowiedzi[i].wypisz(i+1);
	
	
	delete[] testy;
	delete[] odpowiedzi;
}
