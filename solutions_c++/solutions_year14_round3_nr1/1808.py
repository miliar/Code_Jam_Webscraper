#include <iostream>
#include <cstdio>

using namespace std;

bool binpower(int b){
	while (b!=1){
		if (b%2!=0) return false;
		b /=2;
	}
	return true;
}

int main(){
	int T; cin >> T;
	for (int tst = 1; tst <= T; tst++){
		long a,b;
		scanf("%d/%d", &a, &b);
		
		if (!binpower(b)){
			cout << "Case #" << tst << ": impossible" << endl;
		} else {
			int cnt = 0;
			while (a < b){
				b /= 2;
				cnt++;
			}
			cout << "Case #" << tst << ": " << cnt << endl;
		}
	}
	return 0;
}