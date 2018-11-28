#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>
#include <cmath>
#include <list>
#include <map>
#include <set>
using namespace std;

typedef long long int LL;
typedef long double LD;
typedef vector<int> VI;
typedef vector<LL> VLL;
typedef vector<LD> VLD;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

const int INF = 1000000001;
const LD EPS = 10e-9;

#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define VAR(v, n) __typeof(n) v = (n)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define FORE(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define MP make_pair
#define PB push_back
#define ST first
#define ND second
#define abs(a) ((a)<0 ? -(a) : (a))
#define max(a, b) ((a) > (b) ? (a) : (b))
#define min(a, b) ((a) < (b) ? (a) : (b))

int t;
int l, x;

char table[200][200];
int minusTable[200][200];

void initTables()
{
	table['1']['1'] = '1';
	table['1']['i'] = 'i';
	table['1']['j'] = 'j';
	table['1']['k'] = 'k';
	
	table['i']['1'] = 'i';
	table['i']['i'] = '1';
	table['i']['j'] = 'k';
	table['i']['k'] = 'j';
	
	table['j']['1'] = 'j';
	table['j']['i'] = 'k';
	table['j']['j'] = '1';
	table['j']['k'] = 'i';
	
	table['k']['1'] = 'k';
	table['k']['i'] = 'j';
	table['k']['j'] = 'i';
	table['k']['k'] = '1';
	
	for(int i = 0; i < 200; i++)
	{
		for(int j = 0; j < 200; j++)
		{
			minusTable[i][j] = 1;
		}
	}
	
	minusTable['i']['i'] = -1;
	minusTable['j']['j'] = -1;
	minusTable['k']['k'] = -1;
	
	minusTable['i']['k'] = -1;
	minusTable['j']['i'] = -1;
	minusTable['k']['j'] = -1;
}

int main()
{
	initTables();
	
	ios_base::sync_with_stdio(0);
	cin >> t;
	for(int _t = 1; _t <= t; _t++)
	{
		cin >> l >> x;
		
		string s, full;
		cin >> s;
		
		for(int i = 0; i < x; i++)
		{
			full += s;
		}
		
		char suffix[10005] = {0};
		int minusSuffix[10005];
		for(int i = 0; i < 10005; i++)
		{
			minusSuffix[i] = 1;
		}
		
		suffix[full.size()-1] = full[full.size()-1];
		for(int i = full.size()-2; i >= 0; i--)
		{
			suffix[i] = table[full[i]][suffix[i+1]];
			
			if(suffix[i] == 0)
			{
				cout << "duuuuuu[a" << endl;
			}
			
			minusSuffix[i] = minusTable[full[i]][suffix[i+1]] * minusSuffix[i+1];
		}
		
		bool finalOk = false;
		char actResult = '1';
		int actMinus = 1, currentMinus;
		for(int i = 0; i < full.size()-2; i++)
		{
			//cout << full[i] << " => " << actResult << endl;
			actMinus = minusTable[actResult][full[i]] * actMinus;
			actResult = table[actResult][full[i]];
			
			//cout << "i: " << i << ", actMinus: " << actMinus << endl;
			
			if(actResult == 0)
			{
				cout << "aaaa" << endl;
			}
			
			if(actResult == 'i')
			{
				//cout << i << endl;
				
				char secondFragment = '1';
				int secondFragmentMinus = 1;
				
				for(int j = i+1; j < full.size()-1; j++)
				{
					secondFragmentMinus = minusTable[secondFragment][full[j]] * secondFragmentMinus;
					secondFragment = table[secondFragment][full[j]];
					
					if(secondFragment == 0)
					{
						cout << "aaaagfg" << endl;
					}
					
					if(secondFragment == 'j')
					{
						if(suffix[j+1] == 'k')
						{
							if((minusSuffix[j+1] * secondFragmentMinus * actMinus) == 1)
							{
								finalOk = true;
								break;	
							}
						}
					}
				}
				
				if(finalOk)
				{
					break;
				}
			}
		}
		
		cout << "Case #" << _t << ": " << (finalOk ? "YES" : "NO") << endl;
	}
	return 0;
}


