#include <bits/stdc++.h>
using namespace std;

int c[11]={0};

void init(){
	for(int k = 0; k < 10; k++)c[k]=0;
}

int check(){
	for(int k = 0; k<10; k++)if(!c[k])return 0;
	return 1;
}

long long solve(int n){
	int i = 1;
	while(1){
		int ori = i * n;
		int dd = i * n;
		while(dd){
			int d = dd % 10;
			c[d]++;
			dd/=10;
		}

		i++;
		if(check())return ori;
	}
}





int main() {
    freopen ( "in.txt", "r", stdin );
    freopen ( "out.txt", "w", stdout );
	int T,n;

	cin >> T;

	for(int k = 0; k < T; k++){
		init();
		cin >> n;
		if(n == 0){
			printf("Case #%d: INSOMNIA\n",k+1);
		}
		else{
			long long res = solve(n);
			printf("Case #%d: %lld\n",k+1,res);
		}
	}

}
