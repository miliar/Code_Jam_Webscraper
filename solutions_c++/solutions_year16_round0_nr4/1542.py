#include <bits/stdc++.h>
using namespace std;

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	
	long long T, K, C, S, cas, i;
	cin >> T;
	for(cas=1;cas<=T;cas++){
		cin >> K >> C >> S;
		cout << "Case #" << cas << ": ";
		for(i=1;i<=K;i++) cout << i << ' ';
		cout << '\n';
	}
	return 0;
}
