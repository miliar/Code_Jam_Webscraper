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
	int n, l;
	vector < string > V;
	void wczytaj()
	{
		cin>>n>>l;
		V.resize(n+1);
		for(auto& el : V)
		cin >> el;
		V.pop_back();
		////////////////////////////////////////////////////////////to uzupelnic
	}
};

struct Odp
{
	
	string odp;
	void wypisz(int nr)
	{
		
		printf("Case #%d: ", nr);
		cout << odp;
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
	int max_zer = 0, max_jedynek = 0;
	for(auto& el : in.V)
	{
		int ilezer = 0, ilejedynek = 0;
		for(auto& znak : el)
		{
			ilezer += (znak == '0');
			ilejedynek += (znak == '1');
		}
		max_zer = max(max_zer, ilezer);
		max_jedynek = max(max_jedynek, ilejedynek);
	}
	out.odp = "";
	if (max_jedynek == in.l)
	{
		out.odp = "IMPOSSIBLE";
	}
	else
	{
		if (max_jedynek > 0)
		{
			int pom = in.l;
			for(int i=0; i < max_jedynek; i++)
				out.odp += "1";
			out.odp += " ?";
		}
		else
		{
			out.odp +="? ";
		}
		
		for(int i=0; i < in.l-1; i++)
			out.odp += "0?";
		if (out.odp == "? ")
			out.odp += "0";	
	}
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
