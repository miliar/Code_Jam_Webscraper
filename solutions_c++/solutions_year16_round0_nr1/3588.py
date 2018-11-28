#include <iostream>
#include <set>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <set>
#include <cstring>
#include <map>
#include <bitset>
#include <random>
#include <stack>
#include <list>
#include <unordered_set>
#include <ctime>
#include <unordered_map>

using namespace std;

#define ll long long
#define ld long double
#define sc second
#define fs first
#define mp make_pair

template<class T> T sqr(T x) { return x*x; }
ld pi = 3.1415926535897932384626433832795;

const int N = 3e5+10, l = 20;
int t;
void solve(int c)
{
	ll a, b;
	cin >> a;
	b = a;
	set<ll> s;
	for (int i = 0; i < 10; i++){
		s.insert(i);
	}
	if (a == 0){
		cout <<"CASE #" << c << ": INSOMNIA" << endl;
		return;
	}
	while (1)
	{
		ll temp = a;
		while (temp != 0){
			s.erase(temp % 10);
			temp /= 10;
		}
		if (s.empty()){
			cout << "CASE #" << c << ": " << a << endl;
			return;
		}
		a += b;
	}
}


int main()
{
	FILE* f, *g;
	freopen_s(&f, "input.in", "r", stdin);
	freopen_s(&g, "output.txt", "w", stdout);
	cin >> t;
	for (int i = 0; i < t; i++)
		solve(i + 1);
	return 0;
}