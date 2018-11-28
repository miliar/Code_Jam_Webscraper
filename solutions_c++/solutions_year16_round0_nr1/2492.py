#include <bits/stdc++.h>
using namespace std;

long long res(long long int N){
	bool seen[10] = {false};
	int cnt_seen = 0;
	long long cnt = 0;
	
	while (cnt_seen != 10){
		long long cp = (cnt + 1)* N;
		if (cp < 0){
			cout << "ERR" << endl << endl << endl;
		}
		//cout << "\t" << cp << endl;
		while (cp > 0){
			if (!seen[cp%10]){
				cnt_seen++;
				seen[cp%10] = true;
			}
			cp /= 10;
		}
		cnt++;
	}
	return cnt * N;
}

int main(){
	int T;
	long long int N;
	cin >> T;
	for (int i=1; i<=T; i++){
		cin >> N;
		cout << "Case #" << i << ": ";
		if (N == 0)
			cout << "INSOMNIA" << endl;
		else
			cout << res(N) << endl;
	}
}			
