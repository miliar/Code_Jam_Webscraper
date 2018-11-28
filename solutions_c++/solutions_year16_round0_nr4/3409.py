#include <bits/stdc++.h>
using namespace std;

int t,k,c,s;

int main(){
	ios::sync_with_stdio(0); cin.tie(0);
	freopen("fractiles.in","r",stdin);
	freopen("fractiles.out","w",stdout);
	cin >> t;
	for (int tc=1;tc<=t;tc++){
		cout << "Case #" << tc << ": ";
		cin >> k >> c >> s;
		for (int i=1;i<=s;i++) cout << i << (i==s ? "\n" : " ");
	}
}
