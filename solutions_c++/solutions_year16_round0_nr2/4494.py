
/*
B name oooo
ID: amin_un1
PROG: ride
LANG: C++

my ID
uva = "sir sbu"
codforsec = "sir_sbu"
topcoder = "sir_sbu"
usaco = "amin_un1"
*/

#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string>
#include <string.h>
#include <sstream>
#include <math.h>
#include <cmath>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <list>
#include <bitset>
#include <complex>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <time.h>
using namespace std;

#define ll long long
#define ld long double

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

const int MAX = 100001;
const long long mod = 1000 * 1000 * 1000 + 7;

#define mp make_pair
#define pb(a) push_back(a)
#define L(s) (int)((s).size())
#define all(c) (c).begin(), (c).end()

#define INF (1e9)
#define EPS (1e-9)
#define E (2.718281828459045)


////////////////////////////////////////////////////code///////////////////////////////////////
int temp;
string name; 

int f(int n)
{
	if (n < 0)return 0;
	if (n == 0 && name[n] == '+')return 0;
	else if (n == 0 && name[n] == '-')return 1;
	if (name[n] == '+')
	{
		return f(n - 1);
	}
	else
	{
		int ans = 0;
		for (int i = 0; i < n; i ++)
		if (name[i] == '-')
			break;
		else{
			name[i] = '-';
			ans = 1;
		}
		string t = name; 
		for (int i = 0; i <= n; i++){
			if (t[i] == '-'){
				name[n - i] = '+';
			}
			else {
				name[n - i] = '-';
			}
		}
		return f(n) + ans + 1;
	}
	return 0 ;
}

int main()
{
	
	ofstream cout ("test1.out");
	ifstream cin ("B-large.in");
	cin >> temp;
	int tc = 0;
	while (temp--){
		cin >> name;
		tc++;
		int ans = f(name.length() - 1);
		cout << "Case #" << tc << ": " << ans << endl;
	}
	return 0;
}