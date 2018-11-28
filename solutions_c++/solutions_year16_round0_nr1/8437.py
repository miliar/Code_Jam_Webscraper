#include <bits/stdc++.h>
using namespace std;

#define sz(v)			(int)(v.size())
#define aint(v)			v.begin(),v.end()
#define mems(a , i)		memset(a , i , sizeof(a))
#define memc(a , b)		memcpy(a , b , sizeof(a))
#define mp(x , y)		make_pair(x , y)
#define pb(x)			push_back(x)
#define ansy			{cout << "-1" << endl;return 0;}
#define ansn			{cout << "No" << endl;return 0;}
#define IOS				ios_base::sync_with_stdio(0) , cin.tie(0) , cout.tie(0);
#define mod				10007
#define PI				3.14159265358979323846
#define fi				first
#define se				second
#define all(v)			v.begin(), v.end()
const double EPS = 1e-8;
bool arr[10];
int co;
void solve(int n){
	while(n){
		co += (!arr[n%10]);
		arr[n%10] = 1;
		n /= 10;
	}
}
int main() {
#ifndef ONLINE_JUDGE
	freopen("A-large.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	IOS;
	int t , n;
	cin >> t;
	for(int tt = 1; tt <= t ; tt++){
		cin >> n;
		if(n == 0){
			cout << "Case #" << tt << ": INSOMNIA\n";
			continue;
		}
		int j = 0;
		co = 0;
		mems(arr , 0);
		while(co < 10){
			j += n;
			solve(j);
		}
		cout << "Case #"<< tt << ": " << j << "\n";
	}

	return 0;
}

