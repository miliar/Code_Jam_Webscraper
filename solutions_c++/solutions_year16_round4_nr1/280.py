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
	ll N, P, R, S;
	void wczytaj()
	{
		scanf("%lld%lld%lld%lld", &N, &R, &P, &S);
		////////////////////////////////////////////////////////////to uzupelnic
	}
};

struct Odp
{
	string s;
	void wypisz(int nr)
	{
		printf("Case #%d: ", nr);
		cout << s;
		/////////////////////////////////////////////////////////tu uzupelnić	
		printf("\n");
	}
};

Test* testy;
Odp* odpowiedzi;


string odp(int N, char c)
{
	string s;
	s += c;
	if (N==0)
		return s;
	if (c == 'P')
	{
		string s1 = odp(N-1, 'P');
		string s2 = odp(N-1, 'R');
		if (s1 < s2)
			return s1 + s2;
		else
			return s2 + s1;
	}
	if (c == 'R')
	{
		string s1 = odp(N-1, 'R');
		string s2 = odp(N-1, 'S');
		if (s1 < s2)
			return s1 + s2;
		else
			return s2 + s1;
	}
	if (c == 'S')
	{
		string s1 = odp(N-1, 'S');
		string s2 = odp(N-1, 'P');
		if (s1 < s2)
			return s1 + s2;
		else
			return s2 + s1;
	}
}

void zrob(int nr)
{
	if (nr >= ile_t)
		return;
	Test& in = testy[nr];
	Odp& out = odpowiedzi[nr];
	////////////////////////////////////////////////////////////to uzupelnic
	int N = in.N;
	string P = odp(N, 'P'), R = odp(N, 'R'), S = odp(N, 'S');
	int p = 0, s = 0, r = 0;
	for(int i=0; i<P.size(); i++)
	{
		p += (P[i] == 'P');
		r += (P[i] == 'R');
		s += (P[i] == 'S');
	}
	if (p != in.P or r != in.R or s != in.S)
		P = "Z";
	p = 0, s = 0, r = 0;
	for(int i=0; i<R.size(); i++)
	{
		p += (R[i] == 'P');
		r += (R[i] == 'R');
		s += (R[i] == 'S');
	}
	if (p != in.P or r != in.R or s != in.S)
		R = "Z";
	p = 0, s = 0, r = 0;
	for(int i=0; i<S.size(); i++)
	{
		p += (S[i] == 'P');
		r += (S[i] == 'R');
		s += (S[i] == 'S');
	}
	if (p != in.P or r != in.R or s != in.S)
		S = "Z";
	if (S < P)
		P = S;
	if (R < P)
		P = R;
	if (P == "Z")
		out.s = "IMPOSSIBLE";
	else
		out.s = P;
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
