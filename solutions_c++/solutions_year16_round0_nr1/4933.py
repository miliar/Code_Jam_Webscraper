#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
#include <iomanip>
#include <set>
#include <cstdio>
#include <cstring>
#include <stack>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <deque>
#include <algorithm>
#include <cmath>
#include <sstream>
#include <bitset>
#include <ctime>
#include <list>
#include <functional>
using namespace std;
#define mp make_pair
#define ull unsigned long long
#define ll long long
#define mod1 (ll)1000000009
#define mod (ll)1000000007
#define inf (ll)1600000016000000000
#define mpi acos(-1.0)
#define M_E (double)2.71828182846
#pragma comment(linker, "/STACK:1000000000")

static int m1[10];

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	freopen("A-large.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int t, n;
	cin >> t;
	for (int tt = 0; tt < t; ++tt){
		cin >> n;
		cout << "Case #" << tt + 1 << ": ";
		if (n == 0){
			cout << "INSOMNIA\n";
			continue;
		}
		memset(m1, 0, sizeof(m1));
		int b = 0, a, x;
		for (x = n; b < 10; x += n){
			a = x;
			while (a){
				b += m1[a % 10] == 0;
				m1[a % 10] = 1;
				a /= 10;
			}
		}
		cout << x - n << '\n';
	}
	//system("pause");
	return 0;
}