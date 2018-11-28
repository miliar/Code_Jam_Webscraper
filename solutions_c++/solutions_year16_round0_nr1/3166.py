#include <iostream>
#include <algorithm>
using namespace std;

bool used[20]; int cnt;

void add(int N){
	while(N){
		if(!used[N%10]){
			used[N%10]=1;
			cnt++;
		} N /= 10;
	}
}

int main(){
	int T, N, i, nn;
	const int MAX_ITER=1000;
	cin >> T;
	for( int tt = 1; tt <= T; tt++ ){
		cout << "Case #" << tt << ": ";
		cin >> N;
		fill(used,used+20,false);
		cnt=0;
		for(i=nn=0;i<MAX_ITER;i++){
			nn += N;
			add(nn);
			if(cnt==10)i=1000000;
		}
		if(i>MAX_ITER)cout << nn << endl; ///forse nn - N
		else cout << "INSOMNIA\n";
	}
	return 0;
}
