#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define F first
#define S second
using namespace std;
int go(string &a){
	int n = a.length();
	int cnt = 0;
	for(int i=1;i<n;i++) if(a[i] != a[i-1]) cnt++;
	cnt++;
	if(a[n-1] == '+') cnt--;
	return cnt;
}
int main(){
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	int tests; cin >> tests;
	for (int test=1;test<=tests;test++){
		string a; cin >> a;
		cout << "Case #" << test << ": " << go(a) << endl;
	}
	return 0;
}