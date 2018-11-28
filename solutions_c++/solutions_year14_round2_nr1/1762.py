#include <cstdio>
#include <vector>
#include <utility>
#include <cstring>
#include <cstdlib>
#include <map>
#include <iostream>
#include <algorithm>
#include <string>
#include <stack>
#include <queue>
#include <cmath>
#include <set>
#include <assert.h>
#include <bitset>
#include <deque>

using namespace std;
#define pb push_back
#define mp make_pair
#define S second
#define F first
#define INF 0x3f3f3f3f
#define ll long long
#define B 33
#define MAX 100010
#define eps 1e-7
#define pi 3.14159
#define ull unsigned long long
#define MOD 1000000009

typedef vector<int> vi;
typedef pair<int,int>ii;
typedef vector<ii> vii;

int t,n;
string in;
vector<string> v;
int mapa[256];

void apaga(char who, int pos)
{
	for (int j = 0; j < v.size(); ++j)
	{
		if (pos < v[j].size())
		{
			if (v[j][pos] == who)
			{
				v[j].erase(pos,1);
			}
		}
	}
}

int Try(char who, int pos)
{
	int ret = 0;
	for (int j = 0; j < v.size(); ++j)
	{
		if (pos < v[j].size())
		{
			if (v[j][pos] == who && v[j][pos-1] == who)
			{
				ret++;
			}
			else if (v[j][pos] == who)
				return -1;
		}
	}

	return ret;
}

int add(char who, int pos)
{
	int ret = 0;
	for (int j = 0; j < v.size(); ++j)
	{
		if (pos < v[j].size())
		{
			if (v[j][pos] != who && v[j][pos-1] == who)
				ret++;
		}
		if (pos >= v[j].size())
		{
			if (v[j][pos-1] == who)
				ret++;
			else return -1;
		}
	}

	if (ret == 0)
		return -1;
	return ret;
}

void adiciona(char who, int pos)
{
	for (int j = 0; j < v.size(); ++j)
	{
		if (pos < v[j].size())
			if (v[j][pos] != who && v[j][pos-1] == who)
			{
				string str;
				str += who;
				v[j].insert(pos, str);
			}
		if (pos >= v[j].size())
		{
			if (v[j][pos-1] == who)
			{
				string str;
				str += who;
				v[j].insert(pos, str);
			}
		}
	}

}
int main(void)
{
	// ios :: sync_with_stdio(false);

	cin >> t;
	int cases = 0;
	while (t--)
	{
		cin >> n;
		v.clear();
		memset(mapa, 0, sizeof mapa);

		int maior = -INF;

		for (int i = 0; i < n; ++i)
		{
			cin >> in;
			v.pb(in);
			maior = max(maior, (int)in.size());

		}

		for (int j = 0; j < v[0].size(); ++j)
		{
			mapa[v[0][j]]++;
		}

		bool ok = true;
		for (int i = 1; i < v.size(); ++i)
		{
			for (int j = 0; j < v[i].size(); ++j)
			{
				if (mapa[v[i][j]] == 0)
				{
					ok = false;
					break;
				}
			}
			if (!ok)
				break;
		}

		if (!ok)
		{
			cout << "Case #" << ++cases << ": Fegla Won\n";
			continue;
		}

		for (int i = 0; i < v[0].size(); ++i)
		{
			for (int j = 1; j < v.size(); ++j)
			{
				ok = false;
				for (int k = 0; k < v[j].size(); ++k)
				{
					if (v[j][k] == v[0][i])
					{
						ok = true;
						break;
					}
				}
				if (!ok)
				{
					break;
				}
			}

			if (!ok)
			{
				break;
			}
		}

		if (!ok)
		{
			cout << "Case #" << ++cases << ": Fegla Won\n";
			continue;
		}


		memset(mapa, 0, sizeof mapa);

		mapa[v[0][0]]++;
		ok = true;

		for (int i = 1; i < v.size(); ++i)
		{
			if (mapa[v[i][0]] == 0)
			{
				ok = false;
				cout << "Case #" << ++cases << ": Fegla Won\n";
				break;
			}
		}

		int answ = 0;
		if (ok)
		{
			int who[2];
			for (int i = 1; i < maior; ++i)
			{
				int cont = 0;
				memset(mapa, 0, sizeof mapa);
				for (int j = 0; j < v.size(); ++j)
				{
					if (i < v[j].size())
					{
						if (!mapa[v[j][i]])
						{
							mapa[v[j][i]]++;
							if (cont < 2)
								who[cont] = v[j][i];
							cont++;
						}
					}
				}

				// printf("i =  %d cont = %d answ = %d\n",i,cont,answ);
				if (cont == 0)
					break;

				if (cont == 1)
				{
					bool ok2 = true;
					for (int j = 0; j < v.size(); ++j)
					{
						if ( i >= v[j].size() )
							ok2 = false;
						else 
						{
							if (v[j][i] != who[0])
								ok2 = false;
						}
					}

					if (ok2 == false)
					{
						int ret[2];
						ret[0] = add( (char)who[0], i );
						ret[1] = Try( (char)who[0], i );
						
						int menor = INF;

						for (int j = 0; j < 2; ++j)
						{
							if (ret[j] != -1)
								menor = min(menor, ret[j]);
						}

						if ( menor != INF)
						{
							if (menor == ret[0])
							{
								adiciona( (char)who[0], i);
								answ += ret[0];
							}
							else
							{
								adiciona( (char)who[0], i);
								answ += ret[1];
							}
						}
						else
						{
							ok = false;
							cout << "Case #" << ++cases << ": Fegla Won\n";
							break;
						}
					}
					
				}

				else if (cont == 2)
				{
					int opt[4];
					opt[0] = Try((char)who[0], i);
					opt[1] = Try((char)who[1], i);
					opt[2] = add((char)who[0], i);
					opt[3] = add((char)who[1], i);

					int idx = -1;
					int menor = INF;

					for (int j = 0; j < 4; ++j)
					{
						if (opt[j] != -1)
						{
							if (menor > opt[j])
							{
								menor = opt[j];
								idx = j;
							}
						}
					}

					if (idx == -1)
					{
						ok = false;
						cout << "Case #" << ++cases << ": Fegla Won\n";
						break;
					}

					if (idx == 0)
						apaga(who[0],i);

					else if (idx == 1)
						apaga(who[1],i);

					else if (idx == 2)
						adiciona(who[0],i);

					else if (idx == 3)
						adiciona(who[1],i);
					i--;

					answ += opt[idx];
				}
				else
				{
					ok = false;
					cout << "Case #" << ++cases << ": Fegla Won\n";
					break;
				}


				if (!ok)
				{
					break;
				}

				// printf("\n\ni = %d new---\n",i);
				// for (int j = 0; j < v.size(); ++j)
				// {
				// 	cout << v[j] << "\n";
				// }

			}

		}
		if (ok)
			cout << "Case #" << ++cases <<": " << answ << "\n";
	}
	return 0;
}