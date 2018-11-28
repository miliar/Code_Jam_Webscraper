#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <cmath>
#include <sstream>
#include<bitset>
#include <fstream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <queue>	
#include <ctime>
#include <cstring>
using namespace std;
#define ll long long
#define EPS 0.00000001

unordered_map<ll, ll> dp;
ll solve(ll n){
	if (n == 1) return 1;
	if (dp.find(n) != dp.end()) return dp[n];
	stringstream ss;
	ss << n;
	string str = ss.str();
	string s = str;
	ll ans = 99999999999LL;
	if (s[s.size() - 1] == '0') ans = solve(n - 1) + 1;
	else{
		for (int i = 0, j = str.size() - 1; i < j; i++, j--){
			char tmp = str[i];
			str[i] = str[j];
			str[j] = tmp;
		}
		stringstream ss2;
		ss2 << str;
		ll m;
		ss2 >> m;
		if (m < n) ans = min(ans, solve(m) + 1);
		if (s[s.size() - 1] == '1') ans = min(ans, solve(n - 2) + 2);
		else ans = min(ans, solve(n - (s[s.size() - 1] - '1')) + (s[s.size() - 1] - '1'));
		
	}
	dp[n] = ans;
	return ans;
}
int main(){
	int t, z = 1;
	ifstream fin("input.in");
	ofstream fout("output.txt");
	fin >> t;
	
	


	ll n;
	
	while (t--){
		fin >> n;

		//--
		fout << "Case #" << z << ": ";
		z++;
		//--
		fout << solve(n) << endl;
	}





	fin.close();
	fout.close();
	return 0;
}