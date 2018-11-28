#include <fstream>
#include <cstring>
#define MOD 1000000007
using namespace std;
int Ts, n, m, nrmax, nrsol, now, v[10];
char cuv[10][12];

struct Trie
{
	Trie *fiu[26];
	Trie()
	{
		for(int i = 0; i < 26; ++i)
			fiu[i] = NULL;
	}
};
Trie *T[5];

inline void Insert(Trie *nod, char *s)
{
	if(*s == 0)
		return;
	if(nod -> fiu[*s - 'A'] == NULL)
	{
		nod -> fiu[*s - 'A'] = new Trie();
		now++;
	}
	Insert(nod -> fiu[*s - 'A'], s + 1);
}

inline void Erase(Trie *nod)
{
	if(nod == NULL)
	{
		delete nod;
		return;
	}
	int i;
	for(i = 0; i < 26; ++i)
		if(nod -> fiu[i] != NULL)
			Erase(nod -> fiu[i]);
	delete nod;
}

inline void Count()
{
	int i;
	now = 0;
	for(i = 0; i < m; ++i)
		T[i] = NULL;
	for(i = 1; i <= n; ++i)
	{
		if(T[v[i]] == NULL)
		{
			T[v[i]] = new Trie();
			now++;
		}
		Insert(T[v[i]], cuv[i]);
	}
	for(i = 0; i < m; ++i)
		if(T[i] != NULL)
			Erase(T[i]);
}

inline void Back(int pas)
{
	if(pas == n + 1)
	{
		Count();
		if(now > nrmax)
		{
			nrmax = now;
			nrsol = 1;
		}
		else
			if(now == nrmax)
			{
				nrsol++;
				if(nrsol == MOD)
					nrsol = 0;
			}
		return;
	}
	int i;
	for(i = 0; i < m; ++i)
	{
		v[pas] = i;
		Back(pas + 1);
	}
}

int main()
{
	int t, i;
	ifstream fin("D.in");
	ofstream fout("D.out");
	fin >> Ts;
	for(t = 1; t <= Ts; ++t)
	{
		fin >> n >> m;
		for(i = 1; i <= n; ++i)
		{
			memset(cuv[i], 0, sizeof(cuv[i]));
			fin >> cuv[i];
		}
		nrmax = nrsol = now = 0;
		Back(1);
		fout << "Case #" << t << ": " << nrmax << ' ' << nrsol << "\n";
	}
	fin.close();
	fout.close();
	return 0;
}
