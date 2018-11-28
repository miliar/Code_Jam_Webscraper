#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <map>
#include <vector>
#include <queue>
#include <cmath>
#include <set>
#include <sstream>
#define MP make_pair
#define PB push_back

using namespace std;

typedef long long LL;
typedef vector <bool> VB;
typedef vector <VB> VVB;
typedef vector <int> VI;
typedef vector <VI> VVI;
typedef vector <double> VD;
typedef vector <VD> VVD;
typedef pair <int, int> PII;
typedef vector <PII> VPII;
typedef vector <string> VS;

const double eps = 1e-9;
const int INF = 1000000007;
const int MOD = 1000000007;
const int MAXN = 10055;


int main()
{
	freopen ("B.in", "r", stdin);
	freopen ("B.out", "w", stdout);
	
	
	int	T;	cin >> T;
	for (int cas = 1; cas <= T; ++ cas)
	{
		printf ("Case #%d: ", cas);
		
		string s;
		cin >> s;
		string str (1, s[0]);
		for (int i = 1; i < s.size(); ++ i)
			if (s[i] != str[str.size() - 1])
				str += s[i];
		
		cout << str.size() - (str[str.size() - 1] == '+') << endl;
	}
	
	return 0;	
}
