#include <bits/stdc++.h>
using namespace std;

long long f(long long K,long long C,long long S,long long index){
	long long nowK = K;
	long long init_index = index;
	if(C == 1)return index;


	for(int i=1;i<C;i++){
		long long next = (index-1)*K + init_index;
		nowK *= K;
		index = next;
	}
	return index;
}

void solve(long long K,long long C,long long S){
	for(int i=1;i<=K;i++){
		cout << f(K,C,S,i);
		if(i != K)cout << " ";
	}
	cout << endl;
}

int main(void){
	int T;cin >> T;

	for(int i=1;i<=T;i++){
		long long K,C,S;
		cin >> K >> C >> S;

		cout << "Case #" << i << ": ";
		if( K != S )cout << "IMPOSSIBLE" << endl;
		else solve(K,C,S);
	}


	return 0;
}