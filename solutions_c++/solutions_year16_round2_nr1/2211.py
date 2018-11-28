#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
#include <queue>
#include <vector>
#include <bitset>
using namespace std;

#define For(i, a, b) for (int i = a; i < b; ++i)
#define FOR(i, v) for (int i = 0; i < v.size(); ++i)
#define sol(i) cout << "Case #" << i+1 << ": ";

typedef long long int lli;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<bool> vb;

int a[26];

int main(){
	int n;
	string s;
	cin >> n;
	For(i, 0, n){
		vector <int> v;
		cin >> s;
		For(j, 0, 26) a[j] = 0;
		FOR(j, s){
			++a[int(s[j] - 'A')];
		}
		For(j, 0, a['Z' - 'A']){
			v.push_back(0);
		}
		For(j, 0, a['W' - 'A']){
			v.push_back(2);
			--a['T' - 'A'];
		}
		For(j, 0, a['X' - 'A']){
			v.push_back(6);
			--a['I' - 'A'];
			--a['S' - 'A'];
		}
		For(j, 0, a['G' - 'A']){
			v.push_back(8);
			--a['I' - 'A'];
			--a['T' - 'A'];
		}
		For(j, 0, a['S' - 'A']){
			v.push_back(7);
			--a['N' - 'A'];
			--a['V' - 'A'];
		}
		For(j, 0, a['V' - 'A']){
			v.push_back(5);
			--a['I' - 'A'];
			--a['F' - 'A'];
		}
		For(j, 0, a['F' - 'A']){
			v.push_back(4);
		}
		For(j, 0, a['T' - 'A']){
			v.push_back(3);
		}
		For(j, 0, a['I' - 'A']){
			v.push_back(9);
			a['N' - 'A']-=2;
		}
		For(j, 0, a['N' - 'A']){
			v.push_back(1);
		}
		sort(v.begin(), v.end());
		sol(i);
		FOR(j, v) cout << v[j];
		cout << "\n";
	}
	return 0;
}