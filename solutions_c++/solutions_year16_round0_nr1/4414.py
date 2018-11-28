
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
ll number; 
bool arr[20]; 
void res(ll num)
{
	while (num)
	{
		int a = num % 10; 
		arr[a] = 1; 
		num /= 10;
	}
}
bool check()
{
	for (int i = 0; i < 10; i ++)
	if (arr[i] == false)
		return false; 
	return true;
}


int main()
{
	
	ofstream cout ("test.out");
	ifstream cin ("A-large.in");
	cin >> temp;
	int tc = 0;
	while (temp--)
	{
		ll ans = -1; 
		tc++;
		memset(arr, 0, sizeof arr);
		cin >> number;
		for (int i = 1; i < 1000; i++)
		{
			res(number * (ll)(i));
			if (check())
			{
				ans = (ll)(i);
				break;
			}
		}
		if (ans != -1)
			cout << "Case #" << tc << ": " << (ll)ans*number << endl;
		else
			cout << "Case #" << tc << ": INSOMNIA" << endl;
	}
	return 0;

}