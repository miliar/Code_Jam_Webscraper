#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <ctime>

using namespace std;

#define ll long long
#define pb push_back
#define mp make_pair
#define pmp(x,y) pb(mp(x,y))
#define X first
#define Y second
#define MOD 1000000007LL
#define mod 111111113LL
#define INFL 100000000000000000LL
#define EPS 1e-9
#define sqr(x) (x)*(x)
#define pp pair<int, int>

bool check(string& s){
	return s.find("-") == string::npos;
}

int main(){
	freopen("B-large.in", "r", stdin); freopen("A-large.out", "w", stdout);
	int T;
	cin >> T;
	for (int _ = 0; _ < T; _++){
    	string s;
		cin >> s;
		int ans = 0;
		while (!check(s)){
			if (s[0] == '+'){
				int n = s.find('-');
				for (int i = 0; i < n; i++){
					s[i] = '-';
				}
			}
			else{
				int n = s.find('+');
				if (n == string::npos) n = s.size();
				for (int i = 0; i < n; i++){
					s[i] = '+';
				}
			}
			ans++;
		}
		cout << "Case #" << _+1 << ": " << ans << endl;
	}
	//system("pause");
    return 0;
}

