#include <iostream>
#include <vector>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <queue>
#include <set>
#include <map>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <numeric>

#define mp make_pair
#define mt make_tuple
#define fi first
#define se second
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define for1(i, n) for (int i = 1; i <= (int)(n); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for (int i = (int)(a); i <= (int)(b); ++i)

using namespace std;

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vpi;
typedef vector<vi> vvi;
typedef long long i64;
typedef vector<i64> vi64;
typedef vector<vi64> vvi64;

int vet[30];

int main(void)
{
	int _42;

	cin >> _42;

	for (int _41 = 0; _41 < _42; ++_41)
	{
		
		int n, total = 0;

		cin >> n;

		for (int i = 0; i < n; ++i)
		{
			cin >> vet[i];

			total += vet[i];
		}

		//cout << total << endl;

		cout << "Case #" << _41 + 1 << ": ";

		pii resp;

		bool empty = false;
		while(!empty)
		{
			if(n == 3)
			{
				if(total > 2)
				{
					if((float)vet[1]/ (total - 2) <= 0.5 && (float)vet[2]/ (total - 2) <= 0.5 && vet[0] >= 2)
					{	
						resp.fi = 0;
						resp.se = 0;

						vet[0] -= 2;
						printf("%c%c ", 'A' + resp.fi, 'A' + resp.se);
					}

					else if((float)vet[0]/ (total - 2) <= 0.5 && (float)vet[2]/ (total - 2) <= 0.5 && vet[1] >= 2)
					{	
						resp.fi = 1;
						resp.se = 1;

						vet[1] -= 2;
						printf("%c%c ", 'A' + resp.fi, 'A' + resp.se);

					}

					else if((float)vet[1]/ (total - 2) <= 0.5 && (float)vet[0]/ (total - 2) <= 0.5 && vet[2] >= 2)
					{	
						resp.fi = 2;
						resp.se = 2;

						vet[2] -= 2;
						printf("%c%c ", 'A' + resp.fi, 'A' + resp.se);
					}

					else if((float)vet[2]/ (total - 2) <= 0.5 && vet[0] >= 1 && vet[1] >= 1)
					{	
						resp.fi = 0;
						resp.se = 1;

						vet[0] -= 1;
						vet[1] -= 1;
						printf("%c%c ", 'A' + resp.fi, 'A' + resp.se);
					}

					else if((float)vet[1]/ (total - 2) <= 0.5 && vet[0] >= 1 && vet[2] >= 1)
					{	
						resp.fi = 0;
						resp.se = 2;

						vet[0] -= 1;
						vet[2] -= 1;
						printf("%c%c ", 'A' + resp.fi, 'A' + resp.se);
					}

					else if((float)vet[0]/ (total - 2) <= 0.5 && vet[2] >= 1 && vet[1] >= 1)
					{	
						resp.fi = 1;
						resp.se = 2;

						vet[1] -= 1;
						vet[2] -= 1;
						printf("%c%c ", 'A' + resp.fi, 'A' + resp.se);

					}
					else
					{
						for (int i = 0; i < n; ++i)
						{
							if(vet[i] > 0)
							{
								printf("%c ", 'A' + i);
								vet[i]--;
								break;
							}
						}
					}

					
				}
				else
				{
					for (int i = 0; i < n; ++i)
					{
						if(vet[i] > 0)
						{
							printf("%c", 'A' + i);
							vet[i]--;
						}
					}
				}

					

				total = 0;
				for (int i = 0; i < n; ++i)
				{
					//cout << vet[i] << " ";
					total += vet[i];
				}

				//cout << total << endl;
				if(total <= 0)
					empty = true;
			}
			else
			{
				if((float)vet[1]/ (total - 2) <= 0.5 && vet[0] >= 2)
				{	
					resp.fi = 0;
					resp.se = 0;

					vet[0] -= 2;
					printf("%c%c ", 'A' + resp.fi, 'A' + resp.se);
				}

				else if((float)vet[0]/ (total - 2) <= 0.5 && vet[1] >= 2)
				{	
					resp.fi = 1;
					resp.se = 1;

					vet[1] -= 2;
					printf("%c%c ", 'A' + resp.fi, 'A' + resp.se);

				}

				else if(vet[0] == vet[1])
				{	
					resp.fi = 0;
					resp.se = 1;

					vet[0] -= 1;
					vet[1] -= 1;
					printf("%c%c ", 'A' + resp.fi, 'A' + resp.se);
				}
				else
				{
					for (int i = 0; i < n; ++i)
					{
						if(vet[i] > 0)
						{
							printf("%c ", 'A' + i);
							vet[i]--;
							break;
						}
					}
				}

				total = 0;
				for (int i = 0; i < n; ++i)
				{
					//cout << vet[i] << " ";
					total += vet[i];
				}

				//cout << total << endl;
				if(total <= 0)
					empty = true;
			}
		}

		cout << endl;

		
	}

}