#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <cstdlib>
#define sqr(x) (x) * (x)    
#define F first
#define S second                      
#define pb push_back
#define sz(a) int((a).size())
#define mp make_pair

using namespace std;

const int MAXN = (int)2e5 + 1;
const int mod = (int)1e9 + 7;
typedef long long ll;
typedef vector<int> vi;
typedef vector<long long, long long> vll;
typedef pair<int, int> pii;
typedef pair<long long, long long> pll;


int main(){
	int t;
	cin >> t;
	string s;
	for (int i = 0; i < t; i++){
		cin >> s;
		int cnt = 0;
		while (true){
			int pos = -1;
			for (int j = sz(s) - 1; j >= 0; j--){
				if (s[j] == '-'){
					pos = j;
					break;
				}
			}
			if (pos > -1){
				cnt++;
				for (int j = 0; j <= pos; j++)
					if (s[j] == '-')
						s[j] = '+';
					else
						s[j] = '-';
			}
			bool ok = 1;
			for (int k = 0; k < sz(s); k++)
				if (s[k] == '-'){
					ok = 0;
					break;
				}
			if (ok) {
				cout << "Case #" << i + 1 << ": " << cnt << '\n';
				break;
			}
		}
	}
	return 0;
}