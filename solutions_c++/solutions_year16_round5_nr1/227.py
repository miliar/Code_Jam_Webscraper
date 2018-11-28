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
	string s;
	void wczytaj()
	{
		cin >> s;
	}
};

struct Odp
{
	int wyn;
	void wypisz(int nr)
	{
		printf("Case #%d: ", nr);
		cout << wyn;
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
	string s = in.s;
	int zapas = 0;
	int odp = 0;
	bool pom = true;
	while(pom && s.size() > 0)
	{
		for(int i=0; pom && i<s.size()-1; i++)
		{
			if (s[i] == s[i+1])
			{
				odp += 10;
				
				s.erase(s.begin() + i);
				s.erase(s.begin() + i);
				break;
			}
			if (i + 2 == s.size())
				pom = false;
		}
	}
	odp += (5 * s.size()/2);
	out.wyn = odp;
	
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
