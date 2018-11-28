#include <bits/stdc++.h>
using namespace std;

int main(){
	ios::sync_with_stdio(false);

	int T;
	cin >> T;

	for(int t = 1; t <= T; t++){
		int n;
		cin >> n;
		if(n == 0){
			cout << "Case #" << t << ": INSOMNIA" << endl; 
			continue;
		}
		set<int> s;
		int k = 1;
		while(s.size() < 10){
			long long a = 1ll*k*n;
			while(a > 0){
				s.insert( (int) (a%10) );
				a /= 10;
			}
			k++;
		}
		cout << "Case #" << t << ": " << 1ll*n*(k-1) << endl; 
	}

	return 0;
}
