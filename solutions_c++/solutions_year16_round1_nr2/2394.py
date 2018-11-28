#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <iomanip>
#include <sstream>
#include <bitset>
#include <fstream>
#include <queue>
#include <math.h>
#include <set>
#include <stdlib.h>
#include <time.h>
#include <list>

#define For(i,a,b) for(int i=(a);i<(b);++i)
#define rep(i,n)  For(i,0,n)

//clear memory
#define CLR(a) memset((a), 0 ,sizeof(a))
#define check(a) rep(i, a.size()) cout << a[i] << endl
#define SORT(c) sort((c).begin(),(c).end())
#define ll long long
#define vi vector<int>
#define all(it,a) for(auto it = a.begin(); it!=a.end(); it++)
using namespace std;

bool ch(vector<vector<int>> l, int num, vector<vector<int>> v, vector<int> table) {
	set<vector<int>> st;
	rep(i, table.size()) {
		if (table[i] == 0)
			st.insert(v[i]);
	}

	bool fst = false;
	bool ok = true;

	rep(i, num) {
		vector<int> vv(num);
		rep(k, num)
			vv[k] = l[k][i];
		if (st.count(vv) == 0) {
			if (!fst)
				fst = true;
			else {
				ok = false;
				break;
			}
		}

	}
	return ok;
}

bool dfs(vector<vector<int>> v, int num, vector<int> table) {
	vector<vector<int>> l(num, vector<int>(num));
	int piv = 0;
	rep(i, table.size()) {
		if (table[i] == 1) {
			l[piv] = v[i];
			piv++;
		}
	}
	
	if (ch(l, num, v, table)) {
		return true;
	}
	return false;
	//return false;

}

int main(void) {
	int n;
	cin >> n;
	rep(idx, n) {
		int num;
		cin >> num;
		vector<vector<int> > v(2 * num - 1, vector<int>(num));
		rep(k, 2 * num - 1)
			rep(i, num)
			cin >> v[k][i];
		SORT(v);



		vector<int> table(2 * num - 1);
		rep(i, table.size()) {
			table[i] = 0;
			if (2* num - 1 -i <= num)
				table[i] = 1;
		}


		do{
			if (dfs(v, num, table)) {

				break;
			}
		} while (next_permutation(table.begin(), table.end()));



		vector<vector<int>> l(num, vector<int>(num));
		int piv = 0;
		rep(i, table.size()) {
			if (table[i] == 1) {
				l[piv] = v[i];
				piv++;
			}
		}
		set<vector<int>> st;
		rep(i, table.size()) {
			if (table[i] == 0)
				st.insert(v[i]);
		}

		
		rep(i, num) {
			vector<int> vv(num);
			rep(k, num)
				vv[k] = l[k][i];
			
		
			if (st.count(vv) == 0) {
				cout << "Case #" << idx + 1 << ": " ;
				rep(lll,num){
					cout << vv[lll] << " ";

				}
				cout << endl;
				break;
			}

		}


	}


	return 0;
}
