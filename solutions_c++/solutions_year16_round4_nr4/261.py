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
	int n;
	int mas;
	void wczytaj()
	{
		cin>>n;
		mas = 0;
		for(int i=0; i<n; i++)
		{
			string s;
			cin>>s;
			for(int j=0; j<n; j++)
				if (s[j] == '1')
					mas |= (1 << (i*n +j) );
		}
		////////////////////////////////////////////////////////////to uzupelnic
	}
};

struct Odp
{
	int koszt;
	void wypisz(int nr)
	{
		printf("Case #%d: ", nr);
		cout << koszt;
		/////////////////////////////////////////////////////////tu uzupelnić	
		printf("\n");
	}
};

Test* testy;
Odp* odpowiedzi;

bool da_sie(int n, int maska)
{
	if (n == 1)
	{
		if (maska == 1)
			return true;
		return false;
	}
	if (n==2)
	{
		if (maska == 9 || maska == 6 || maska == 15)
			return true;
		return false;
	}
	if (n==3)
	{
		vector < int > V = {84, 98, 118, 140, 161, 173, 220, 227, 266, 273, 283, 341, 362, 398, 433, 511};
		for(auto el : V)
			if (el == maska)
				return true;
		return false;
	}
	if (n==4)
	{
		vector < int > V = {4680, 4740, 4812, 5160, 5250, 5290, 5736, 5766, 6180, 6210, 6246, 6730, 6820, 7212, 7362, 7918, 8520, 8580, 8652, 9240, 9345, 9369, 9560, 9605, 10260, 10305, 10325, 10569, 10644, 11292, 11457, 11741, 13128, 13188, 13260, 13368, 13443, 14388, 14403, 15420, 15555, 16680, 16770, 16810, 16920, 17025, 17049, 17208, 17283, 18450, 18465, 18483, 18729, 18834, 18970, 19105, 19387, 21080, 21125, 21800, 21890, 21930, 22565, 22610, 23130, 23205, 24936, 24966, 26136, 26241, 26265, 26646, 26721, 26985, 27030, 30584, 30599, 30839, 33060, 33090, 33126, 33300, 33345, 33365, 33588, 33603, 33810, 33825, 33843, 34085, 34130, 34326, 34401, 34679, 37449, 37524, 37929, 38034, 38505, 38550, 39204, 39234, 39270, 41290, 41380, 42010, 42145, 42330, 42405, 43540, 43585, 43605, 46267, 47947, 48052, 49452, 49602, 49692, 49857, 49980, 50115, 52242, 52257, 52275, 53981, 56621, 56786, 57838, 60958, 61153, 65535};
		for(auto el : V)
			if (el == maska)
				return true;
		return false;
	}
}

void zrob(int nr)
{
	if (nr >= ile_t)
		return;
	Test& in = testy[nr];
	Odp& out = odpowiedzi[nr];
	////////////////////////////////////////////////////////////to uzupelnic
	int mini = 16, n = in.n;
	for(int i=0; i< (1<<(n*n)); i++)
	{
		if (i & in.mas)
			continue;
		if (!da_sie(n, i | in.mas))
			continue;
		mini = min(mini, __builtin_popcount(i));
	}
	out.koszt = mini;
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
