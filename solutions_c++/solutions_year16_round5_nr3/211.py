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

struct as
{
	ld x, y, z, vx, vy, vz;
};

struct Test
{
	double n, s;
	vector < as > V;
	void wczytaj()
	{
		cin>>n>>s;
		V.resize(n);
		for(auto& el : V)
			cin >> el.x  >> el.y >> el.z >> el.vx >> el.vy >> el.vz;
		////////////////////////////////////////////////////////////to uzupelnic
	}
};

struct Odp
{
	ld dist;
	void wypisz(int nr)
	{
		printf("Case #%d: ", nr);
		cout << setprecision(7) << fixed;
		cout << dist;
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
	
	ld dol = 0.0, gora = 2000.0;
	int ile = 50, n = in.n;
	while(ile--)
	{
		ld srodek = (dol + gora) / 2.0;
		vector < int > V = {0};
		vector < bool > M(n, 0);
		M[0] = 1;
		while(V.size() > 0)
		{
			int akt = V.back();
			V.pop_back();
			for(int i=0; i<n; i++)
			{
				if (M[i])
					continue;
				if ( (in.V[i].x - in.V[akt].x) * (in.V[i].x - in.V[akt].x) + (in.V[i].y - in.V[akt].y) * (in.V[i].y - in.V[akt].y)+ (in.V[i].z - in.V[akt].z) * (in.V[i].z - in.V[akt].z)  > srodek * srodek)
					continue;
				M[i] = true;
				V.push_back(i);
			}
		}
		
		if (M[1])
			gora = srodek;
		else
			dol = srodek;
	}
	out.dist = gora;
}

int main()
{
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
