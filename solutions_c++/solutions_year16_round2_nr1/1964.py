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

const int MAX_L = 1000;

int T;
string s;

int main()
{
	ios_base::sync_with_stdio(0);
	cin >> T;
	FOR(t, 1, T)
	{
		cin >> s;
		
		string res;
		int letters[MAX_L] = {0};
		
		FORE(it, s)
		{
			letters[*it]++;
		}
		
		while(letters['Z']--)
		{
			res += '0';
			letters['E']--;
			letters['R']--;
			letters['O']--;
		}
		
		while(letters['W']--)
		{
			res += '2';
			letters['T']--;
			letters['O']--;
		}
		
		while(letters['U']--)
		{
			res += '4';
			letters['F']--;
			letters['O']--;
			letters['R']--;
		}
		
		while(letters['X']--)
		{
			res += '6';
			letters['S']--;
			letters['I']--;
		}
		
		while(letters['G']--)
		{
			res += '8';
			letters['E']--;
			letters['I']--;
			letters['H']--;
			letters['T']--;
		}
		
		while(letters['T']--)
		{
			res += '3';
			letters['H']--;
			letters['R']--;
			letters['E']--;
			letters['E']--;
		}
		
		while(letters['O']--)
		{
			res += '1';
			letters['N']--;
			letters['E']--;
		}
		
		while(letters['F']--)
		{
			res += '5';
			letters['I']--;
			letters['V']--;
			letters['E']--;
		}
		
		while(letters['V']--)
		{
			res += '7';
			letters['S']--;
			letters['E']--;
			letters['E']--;
			letters['N']--;
		}
		
		while(letters['I']--)
		{
			res += '9';
		}
		
		sort(res.begin(), res.end());
		
		cout << "Case #" << t << ": " << res << endl;	
	}
	return 0;
}


