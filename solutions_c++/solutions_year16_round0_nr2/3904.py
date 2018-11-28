#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <deque>
using namespace std;
typedef long long ll;
typedef pair<double, double> dd;
typedef pair<int, int> ii;
typedef pair<int, ii> iii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;
typedef vector<vii> vvii;

int main(){
	int T; cin >> T;
	for(int t=1;t<=T;t++){
		string s; cin >> s;
		string z = ""; z += s[0];
		for(int i=1;i<s.length();i++){
			if(s[i] != s[i-1]){
				z += s[i];
			}
		}
		//cout << z << endl;
		int ans = 0;
		for(int i=0;i<z.length();i++){
			if(z[i] == '-'){
				ans++;
			}else{
				ans++;
			}
		}
		if(z[z.length()-1] == '+') ans--;

		printf("Case #%d: %d\n", t, ans);
	}

}
