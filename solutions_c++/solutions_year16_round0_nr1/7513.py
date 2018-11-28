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


int used[11];

int main(){
	ll tmp, cnt;
	int n, t;
	scanf ("%d", &t);
	for (int i = 0; i < t; i++){
		for (int j = 0; j < 11; j++)
			used[j] = 0;
		scanf ("%d", &n);
		if (n == 0)
			cout << "Case #" << i + 1 << ": INSOMNIA\n";
		else {
			ll inc = 1;
			while (true){
				tmp = inc * n;
				cnt = tmp;
				inc++;
				while (tmp > 0){
					if (used[tmp % 10] == 0)
						used[tmp % 10] = 1;
					tmp /= 10;	
				}
				bool ok = false;
				for (int k = 0; k < 10; k++){
					if (used[k] == 1)
						ok = 1;
					else {
						ok = 0;
						break;
					}	
				}
				if (ok){
					cout << "Case #" << i + 1 << ": " << cnt << '\n';
					break;
				}
			}
		}	
	}
	return 0;
}