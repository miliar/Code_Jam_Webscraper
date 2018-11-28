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
#define vi(m,a) vector<int> m(a)
#define vti(m,a,i) vector<vector<int>> m(a,vector<int>(i))
#define all(it,a) for(auto it = a.begin(); it!=a.end(); it++)
using namespace std;

vector<string> vs = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };

bool ch(map<char, int> mp, int piv){
	map<char, int> mmp;
	rep(i, vs[piv].length()){
		mmp[vs[piv][i]]++;
	}

	all(it, mmp){
		if (mp[it->first] < it->second){
			return false;
		}
	}
	return true;
}

string dfs(map<char, int> mp, int piv, int nokori,string res){

	if (nokori == 0){
		return res;
	}

	if (piv > 9){
		return "-1";
	}

	if (ch(mp, piv)){
		rep(i, vs[piv].length()){
			mp[vs[piv][i]]--;
		}
		res += to_string(piv);
		nokori -= vs[piv].length();
	}
	if (nokori == 0){
		return res;
	}
	For(i, piv, 10){
		if (!ch(mp, i)){
			continue;
		}
		string t = dfs(mp, i, nokori, res);
		if (t != "-1"){
			return t;
		}
	}
	return "-1";

}

int main(void) {
	int n;
	cin >> n;
	rep(idx, n) {
		string str;
		cin >> str;

		//SORT(str);
		map<char, int> mp;

		rep(i, str.length()){
			mp[str[i]]++;
		}
		string res = dfs(mp, 0, str.length(), "");
		cout << "Case #" << idx + 1 << ": " << res << endl;
	}


	return 0;
}
