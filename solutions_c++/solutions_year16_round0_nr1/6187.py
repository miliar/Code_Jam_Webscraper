#include<cstdio>
#include<iostream>
#include<string>
#include<cstring>
#include<cmath>
using namespace std;
int check[10];
bool acheck() {
	for (int i = 0; i < 10; i++)
		if (check[i] == 0)
			return false;
	return true;
}
int main() {
	int n, kase = 0; cin >> n;
	while (n--) {
		memset(check, 0, sizeof(check));
		int k,d;
		cin >> k;
		if (k == 0) { printf("Case #%d: INSOMNIA\n", ++kase); continue; }
		int z = k;
		for (int i = 1;i<50000;i++) {
			k =i*z;
			int q = 0,tk=k;
			while (tk > 0) {
				int as = tk%10;
				//cout << as << ' ';
				check[as] = 1;
				tk /= 10;
			}
			if (acheck()) {
				printf("Case #%d: %d\n", ++kase,k);
				break;
			}
			if(i==49999){printf("Case #%d: INSOMNIA\n", ++kase);}
		}
		
	}
	//system("PAUSE");
	return 0;
}