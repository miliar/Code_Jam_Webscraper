#if 1
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;

FILE* pF;

FILE* pAnsF;

void reset();

int  N;

int C;
int ccount[256];
char ss[] = "ZGXUWHSVEI";
int main()
{
	freopen_s(&pF, "Text.txt", "r", stdin);

	freopen_s(&pAnsF, "OA.txt", "w", stdout);

	cin >> C;
	string S;
	string ans;
	for (int c = 1; c <= C; c++)
	{
		cin >> S;
		int size = S.size();
		for (int i = 0; i < size; i++)
		{
			ccount[S[i]]++;
		}
		int i = 0;



		while (1)
		{
			if (ccount[ss[i]] && ccount['Z'] && ccount['E'] && ccount['R'] && ccount['O'])
			{
				ans.push_back('0');
				ccount['E']--;
				ccount['R']--;
				ccount['O']--;
				ccount['Z']--;
			}
			else
			{
				break;
			}
		}
		i++;
		while (1)
		{
			if (ccount[ss[i]] && ccount['E'] && ccount['I'] && ccount['G'] && ccount['H'] && ccount['T'])
			{
				ans.push_back('8');
				ccount['I']--;
				ccount['G']--;
				ccount['E']--;
				ccount['H']--;
				ccount['T']--;
			}
			else
			{
				break;
			}
		}

		i++;
		while (1)
		{
			if (ccount[ss[i]] && ccount['S'] && ccount['I'] && ccount['X'])
			{
				ans.push_back('6');
				ccount['S']--;
				ccount['I']--;
				ccount['X']--;
			}
			else
			{
				break;
			}
		}
		i++;
		while (1)
		{
			if (ccount[ss[i]] && ccount['F'] && ccount['O'] && ccount['U'] && ccount['R'])
			{
				ans.push_back('4');
				ccount['F']--;
				ccount['O']--;
				ccount['U']--;
				ccount['R']--;
			}
			else
			{
				break;
			}
		}

		i++;
		while (1)
		{
			if (ccount[ss[i]] && ccount['T'] && ccount['W'] && ccount['O'])
			{
				ans.push_back('2');
				ccount['T']--;
				ccount['W']--;
				ccount['O']--;				
			}
			else
			{
				break;
			}
		}
		i++;
		while (1)
		{
			if (ccount[ss[i]] && ccount['T'] && ccount['H'] && ccount['R'] && ccount['E'] && ccount['E'])
			{
				ans.push_back('3');
				ccount['T']--;
				ccount['H']--;
				ccount['R']--;
				ccount['E']--;
				ccount['E']--;
			}
			else
			{
				break;
			}
		}
		i++;
		while (1)
		{
			if (ccount[ss[i]] && ccount['S'] && ccount['E'] && ccount['V'] && 	ccount['E'] && 	ccount['N'])
			{
				ans.push_back('7');
				ccount['S']--;
				ccount['E']--;
				ccount['V']--;
				ccount['E']--;
				ccount['N']--;
			}
			else
			{
				break;
			}
		}
		i++;
		while (1)
		{
			if (ccount[ss[i]] && ccount['F'] && ccount['I'] && ccount['V'] && ccount['E'])
			{
				ans.push_back('5');
				ccount['F']--;
				ccount['I']--;
				ccount['V']--;
				ccount['E']--;				
			}
			else
			{
				break;
			}
		}
		i++;
		while (1)
		{
			if (ccount[ss[i]] && ccount['O'] && ccount['N'])
			{
				ans.push_back('1');
				ccount['O']--;
				ccount['N']--;
				ccount['E']--;
			}
			else
			{
				break;
			}
		}
		i++;
		while (1)
		{
			if (ccount[ss[i]] && ccount['N'] && ccount['I'] && ccount['N'] && ccount['E'])			
			{
				ans.push_back('9');
				ccount['N']--;
				ccount['I']--;
				ccount['N']--;
				ccount['E']--;
			}
			else
			{
				break;
			}
		}

		sort(ans.begin(), ans.end());

		cout << "Case #" << c << ": " << ans << endl;
		ans.clear();
		reset();
	}


	return 0;
}
void reset()
{
	for (int i = 0; i <= 255; i++)
	{
		ccount[i] = 0;
	}
}
#endif