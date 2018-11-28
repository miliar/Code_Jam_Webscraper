#include<bits/stdc++.h>
#define LL long long int
using namespace std;

int main(){
	int t;
	cin >> t;
	for(int z = 1; z <= t; z++){
		printf("Case #%d:\n", z);
		int N, Q;
		cin >> N >> Q;
		
		for(LL i = 0; i < 1<<(N-2) && Q > 0; i++){
			vector<LL> bases(11, -1);
			bool flag = true;
			for(int base = 2; base <= 10; base++){
				LL num = 1;
				for(int j = N-3; j >= 0; j--){
					num = (num*base + ((i&(1<<j))>>j));
				}
				num = num*base + 1;
				for(LL j = 2; j*j <= num; j++){
						if(num%j == 0){
							bases[base] = j;
							break;
						}
				}
				if(bases[base] == -1){
					flag = false;
					break;
				}
			}
			if(flag){
				printf("1");
				for(int j = N-3; j >= 0; j--){
					cout << (i&(1<<j) ? "1":"0");
				}
				cout << "1" << " ";
				for(int base = 2; base <= 10; base++){
					cout << bases[base] << " ";
				}
				cout << "\n";
				Q--;
			}
		}
	}
	return 0;
}