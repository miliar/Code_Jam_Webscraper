#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <string>
#include <cmath>
#include <bitset>
#include <stack>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <ctime>
#include <cstring>
#include <list>
//#include <forward_list>
#include <iomanip>
#include <cassert>
#include <functional>	

const double EPS = 0.000001;
const long long mod = 1000000000 + 7;
using namespace std;
#define ll long long
#define ull unsigned long long
#define mk make_pair

//----------------------------

#define cin fin
//
#define cout fout

//----------------------------
#ifdef cin	
ifstream fin("in.in");
#endif
#ifdef cout
ofstream fout("out.out");
#endif



void f(int n){
	vector<string> a;
	vector<string> b;
	string s;
	for (int i = 0; i < n; i++) s.push_back('L');
	for (int i = 0; i < n; i++) a.push_back(s);
	for (int i = 0; i < n; i++) a[i][i] = 'G';
	b = a;
	string gs;
	for (int i = 0; i < n; i++) gs.push_back('G');

	for (int i = 0; i < 7; i++){
		for (int j = 0; j < n; j++){
			cout << a[j] << endl;
		}

		for (int j = 0; j < n; j++){
			string x;
			for (auto c : a[j]){
				if (c == 'G') x += gs + " ";
				else if (c == 'L') x += b[j] + " ";
			}
			a[j] = x;
		}
		cout << endl;
	}


}

ll myPow(ll a, ll n){
	ll res = 1;
	while (n){
		if (n % 2) res *= a;
		n /= 2;
		a *= a;
	}
	return res;
}


int main(){
	ios::sync_with_stdio(0);

	int t, z = 1;
	cin >> t;


	while (t--){
		ll k, c, s;
		cin >> k >> c >> s;
		
		cout << "Case #" << z++ << ": ";
		for (ll i = 1, j = 0; j < s; i += myPow(k, c - 1), j++){
			cout << i << " ";
		}
		cout << endl;
	}

#undef cin
	int ____________;
	cin >> ____________;
	return 0;
}