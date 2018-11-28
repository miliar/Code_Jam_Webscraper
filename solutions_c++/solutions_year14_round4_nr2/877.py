#include <fstream>
#include <algorithm>
using namespace std;
int T, n, v[1010], sol, parte[1010], perm[1010], aib[1010];
struct Element
{
	int val, ind;
	bool operator <(const Element &A) const
	{
		return val < A.val;
	}
};
Element vsort[1010];

inline void Aduna(int poz, int val)
{
	while(poz <= n)
	{
		aib[poz] += val;
		poz += (poz & -poz);
	}
}

inline int Suma(int poz)
{
	int sum = 0;
	while(poz > 0)
	{
		sum += aib[poz];
		poz -= (poz & -poz);
	}
	return sum;
}

inline void Solve()
{
	int i, j, k, now = 0;
	for(i = 1; i <= n; ++i)
	{
		aib[i] = 0;
		perm[i] = 0;
	}
	j = 1;
	k = n;
	for(i = 1; i <= n; ++i)
	{
		if(parte[vsort[i].ind] == 0)
		{
			perm[j] = vsort[i].ind;
			j++;
		}
		else
		{
			perm[k] = vsort[i].ind;
			k--;
		}
	}
	Aduna(perm[1], 1);
	for(i = 2; i <= n; ++i)
    {
		now += (i - 1 - Suma(perm[i]));
        Aduna(perm[i], 1);
    }
	sol = min(sol, now);
}

inline void Back(int pas)
{
	if(pas == n + 1)
	{
		Solve();
		return;
	}
	parte[pas] = 0;
	Back(pas + 1);
	parte[pas] = 1;
	Back(pas + 1);
}

int main()
{
	int t, i;
	ifstream fin("B.in");
	ofstream fout("B.out");
	fin >> T;
	for(t = 1; t <= T; ++t)
	{
		fin >> n;
		for(i = 1; i <= n; ++i)
		{
			fin >> v[i];
			vsort[i].val = v[i];
			vsort[i].ind = i;
		}
		sort(vsort + 1, vsort + n + 1);
		sol = 1000000000;
		Back(1);
		fout << "Case #" << t << ": " << sol << "\n";
	}
	fin.close();
	fout.close();
	return 0;
}
