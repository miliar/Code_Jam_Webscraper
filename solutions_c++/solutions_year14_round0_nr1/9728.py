#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <iomanip>
#include <math.h>
#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <string.h>
#include <sstream>
#include <cstring>
#include <fstream>
#include <functional>
#include <cstdio>
#include <stack>
#include <utility> 
#include <list>
#include <queue>
#include <bitset>
using namespace std;
#define all(con) con.begin(), con.end()
#define sz(datast) datast.size()
#define mk make_pair
#define pb push_back
#define sp setprecision
#define p_dis(x1, y1, x2, y2) sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
#define getmax(x, y) x>y?x:y
#define getmin(x, y) x<y?x:y
#define rep(i, j) for (int i = 0; i < j; i++)
#define rep_(i, j, k) for (int i = j; i < k; i++)
#define rep__(i, j, k, p) for (int i = j; i < k; i+=p)
#define rep_sp(i, j, number) for (int i = 1; j < number; i++)
#define rev_rep(i, size) for (int i = size - 1; i > -1; i--)
#define rep_map(def, my_map) for (def::iterator it = my_map.begin(); it != my_map.end(); it++)
#define pi 3.1415926535897932384626433832795
typedef stringstream ss;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<int> vi;
typedef vector<bool> vb;
typedef vector<double> vd;
typedef vector<string> vs;
typedef map<int, int> mii;
typedef map<char, int> mci;
typedef map<string, int> msi;
typedef map<int, string> mis;
typedef map<string, bool> msb;
typedef map<char, bool> mcb;
typedef map<char, string> mcs;
typedef map<int, bool> mib;
int main(){
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int size, ch, array[4], counter = 0, number;
	mib array1, array2;
	cin >> size;
	rep(q, size){
		cin >> ch;
		rep(z, 4){
			if (z + 1 == ch) rep(i, 4) cin >> array[i], array1[array[i]] = true;
			else rep(i, 4) cin >> array[i];
		}
		cin >> ch;
		rep(z, 4){
			if (z + 1 == ch) rep(i, 4) cin >> array[i], array2[array[i]] = true;
			else rep(i, 4) cin >> array[i];
		}
		rep_map(mib, array1) if (array2[it->first]) counter++, number = it->first;
		if (!counter) cout << "Case #" << q + 1 << ": Volunteer cheated!" << endl;
		else if (!(counter - 1)) cout << "Case #" << q + 1 << ": " << number << endl;
		else cout << "Case #" << q + 1 << ": Bad magician!" << endl;
		number = counter = 0, array1.clear(), array2.clear();
	}
	return 0;
}