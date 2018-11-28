
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

#define l(x) (int)(x.size())
#define s(x) sizeof(x)
//#define for(i,a,b) for (int i = a; i <=b; i++)

const int MOD = 1000002013;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;

ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }
int bc(int n) { return n ? bc((n-1)&n)+1 : 0; }

int countmax (vector<int> v){// number of max elements
	int max = 0;
	for (int i = 0 ; i < v.size(); i++){
		if (max < v[i]) max = v[i];
	}
	int ans = 0;
	for (int i = 0 ; i < v.size(); i++){
		if (v[i] == max) ans ++;
	}
	return ans;

}

vector<int> indexmax(vector<int> v){
	int max = 0;
	for (int i = 0 ; i < v.size(); i++){
		if (max < v[i]) max = v[i];
	}
	vector<int> ans;
	for (int i = 0 ; i < v.size(); i++){
		if (v[i] == max) ans.push_back(i);
	}
	return ans;	
}

int secondmax(vector<int> v, int m){
	int ans = 0;
	for (int i = 0 ; i < v.size(); i++){
		if (v[i] != m && ans < v[i]){
			ans = v[i];
		}
	}
	for (int i = 0; i < v.size(); i++){
		if (ans == v[i]) return i;
	}
	return -1;
}

int main() {
 //freopen("x.in", "r", stdin);

freopen("A-large.in", "r", stdin);
//freopen("C-small-attempt0.out", "w", stdout);

//	freopen("input1.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T; cin >> T;
	for(int cc = 1; cc <= T; cc++){
		int n; cin >> n;
		vector<int> v (n);
		for (int i = 0; i < n; i++){
			cin >> v[i];
		}
		string ans = "";
		int countm = countmax(v);
		//cout << countm <<endl;
		if (countm >= 2){
			vector<int> index = indexmax(v);
			int x = index[0];
			int y = index[1];
			//cout << x<< " "<<y<<endl;
			for (int i = 0 ; i < n; i++){
				if (i != x && i != y){
					for (int j = 0; j < v[i]; j++){
						ans += ('A'+i);
						ans += ' ';
					}
				}
			}
			//cout << ans <<endl;
			for (int i = 0; i < v[y]; i++){
				ans += ('A'+x);
				ans += ('A'+y);
				ans += ' ';
			}
			//cout << ('A'+x)<<endl;
		}else{
			vector<int> index = indexmax(v);
			int x = index[0];
			int y = secondmax(v,v[x]);
			for (int i = 0 ; i < v[x] - v[y]; i++){
				ans += ('A' + x);
				ans += ' ';
			}
			for (int i = 0 ; i < n; i++){
				if (i != x && i != y){
					for (int j = 0; j < v[i]; j++){
						ans += ('A'+i);
						ans +=  ' ';
					}
				}
			}
			for (int i = 0; i < v[y]; i++){
				ans += ('A'+x);
				ans +=('A'+y);
				ans +=' ';
			}
		}
		
		cout << "Case #"<< cc<<": "<<ans.substr(0, ans.length()-1)<<endl;
	}
	return 0;
}

