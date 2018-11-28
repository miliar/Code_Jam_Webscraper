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

int a[100000000];
bool b[10];
int c;

void check(int n){
	while (n){
		int a = n % 10;
		n /= 10;
		if (!b[a]){
			b[a] = true;
			c--;
		}
	}
}

int main(){
	freopen("A-large.in", "r", stdin); freopen("A-large.out", "w", stdout);
	int T;
	cin >> T;
	for (int _ = 0; _ < T; _++){
    	int n;
		cin >> n;
		int s = 0;
		c = 10;
		for (int i = 0; i < 10; i++) b[i] = false;
		//while (n && n%10 == 0) n /= 10;
		if (n == 0){
			cout << "Case #" << _+1 << ": INSOMNIA" << endl; 
			continue;
		}
		check(n);
		int ans = 1;
		while (c){
			check(n*++ans);
			//cout << n*ans << endl;
		}
		cout << "Case #" << _+1 << ": " << n*ans << endl;
	}
	//system("pause");
    return 0;
}

