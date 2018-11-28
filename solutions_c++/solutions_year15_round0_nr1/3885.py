/*	Try wygrać except trudno
 *	Stanisław Dobrowolski, Katarzyna Jabłonowska, Arkadiusz Wróbel
 *
 *	Zadanie: 
 *	Konkurs: 
 */
#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;
typedef long long LL;
typedef pair<int, int> PII;
typedef vector<int> VI;
#define REP(I, N) for(int I=0; I<(N); ++I)
#define FOR(I, M, N) for(int I=(M); I<=(N); ++I)
#define FORD(I, M, N) for(int I=(M); I>=(N); --I)
#define FOREACH(IT, CON) for(__typeof(CON.begin()) IT=CON.begin(); IT!=CON.end(); ++IT)
#define ST first
#define ND second
#define MP make_pair
#define PB push_back
#define SIZE(CON) ((int)CON.size())
const int INF=1000000000;
const LL INFLL=1000000000000000000LL;
int t, n;
string s;

int main()
{
	cin>>t;
	for(int z=0; z<t; z++)
	{
		cin>>n>>s;
		int ile = 0;
		int wyn = 0;
		for (int i=0; i<=n; i++)
		{
			if(s[i]>'0'&&i>ile)
			{
				wyn+=i-ile;
				ile = i+s[i]-'0';
			}
			else
			{
				ile+=s[i]-'0';	
			}
		}
		cout<<"Case #"<<z+1<<": "<<wyn<<"\n";
	}
	return 0;
}

