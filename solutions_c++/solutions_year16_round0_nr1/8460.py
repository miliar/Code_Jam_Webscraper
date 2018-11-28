#include <bits/stdc++.h>
#define ULL unsigned long long

using namespace std;
bool exist[10];

bool scan(ULL n) {
	int digit;
	while(n > 0) {
		/*cout << "inside 2" << endl;*/
		digit = n%10;
		exist[digit] = true;
		n = n/10;
	}
	bool ok = true;
	for(int i=0;i<10;i++) {
		if(!exist[i]) {
			ok = false; break;
		}
	}
	return ok;
}


int main() {
	int T,N;
	ULL res;
	cin >> T;
	for(int qq=1;qq<=T;qq++) {
		memset(exist,false,sizeof exist);
		cin >> N;
		printf("Case #%d: ",qq);
		if(N==0) {
			printf("INSOMNIA\n");
		} else {
			bool ok = false;
			int k=1;
			while(!ok) {
				/*cout << "inside 1" << endl;*/
				if(scan(k*N)) {
					res = k*N;
					ok = true;
				}
				k++;
			}
			cout << res << endl;
		}
	}
	return 0;
}