#include<iostream>
#include<fstream>

using namespace std;
#define LL long long

void convert(LL x, int b){
	LL res = 0;
	LL m = 0;
	int d[50] = {0};
	while(x){
		d[m++]= (x % 2);
		x >>= 1;

	}
	for(int i = m - 1; i >= 0; i--)
		cout << d[i];
}
LL divs(LL x, int b, LL d){
	LL res = 0;
	LL m = 1;
	while(x){
		res += m * (x % 2);
		x >>= 1;
		m *= b;
		m %= d;
		res %= d;

	}
	return res;
}

int main(){
	freopen("C_large.out", "w", stdout);
	int n, J, t;
	cin >> t >> n >> J;
	for(int i = 0; i < t; i++){
		LL m = (1ll << (n - 2));
		int num = 0;
		cout << "Case #" << i + 1 << ":" << endl;
		for(LL k = m; k < (m << 1) && num < J; k++){
			int cnt = 0, d[11] = {0};
			for(int b = 2; b < 11; b++){
				LL x = (k << 1) + 1;
				for(int j = 2; j < 500; j++){
					LL r = divs(x, b, j);
					if(r == 0){
						d[b] = j;
						cnt++;
						break;
					}
				}
			}
		
			if(cnt == 9){
				convert((k << 1) + 1, 10);
				for(int b = 2; b < 11; b++)
					cout << " " << d[b];
				cout << endl;
				num++;
			}
		}
	}
	return 0;
}
