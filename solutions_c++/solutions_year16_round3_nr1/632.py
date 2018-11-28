#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <string>
#include <cstring>
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

const double EPS = 0.00000001;
const long long mod = 1000000000 + 7;
using namespace std;
#define ll long long
#define ull unsigned long long
#define mk make_pair

//----------------------------
//
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

int a[50];
set<pair<int, int>> m;
int main(){
	ios::sync_with_stdio(0);
	int t, z = 1;
	cin >> t;
	while (t--){
		cout << "Case #" << z++ << ": ";
		//--------------------------------------------------------
		int n;
		cin >> n;
		for (int i = 0; i < n; i++) cin >> a[i];
		int tot = 0;
		for (int i = 0; i < n; i++) tot += a[i];
		for (int i = 0; i < n; i++) m.insert(mk(a[i], i));

		while (!m.empty()){
			char c = 'A' + m.rbegin()->second;
			cout << c;
			tot--;
			if (m.rbegin()->first > 1) m.insert(mk(m.rbegin()->first - 1, m.rbegin()->second));
			m.erase(--m.end());
			if (2 * m.rbegin()->first > tot){
				c = 'A' + m.rbegin()->second;
				cout << c << " ";
				tot--;
				if (m.rbegin()->first > 1) m.insert(mk(m.rbegin()->first - 1, m.rbegin()->second));
				m.erase(--m.end());
			}
			else cout << ' ';
			
		}

		cout << '\n';	
		//--------------------------------------------------------
	}
#undef cin
	int ______________;
	cin >> ______________;
	return 0;
}