#include <bits/stdc++.h>
using namespace std;

long long solve(long long n){
	long long arr[10]={0}, i, t, f;
	for(i=1;i<=100;i++){
		t = n*i;
		while(t){
			arr[t%10] = 1;
			t /= 10;
		}
		f=1;
		for(t=0;t<10;t++){
			if(!arr[t]){
				f=0;
				break;
			}
		}
		if(f) return n*i;
	}
	return 0;
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	
	long long T, N, i;
	cin >> T;
	for(i=1;i<=T;i++){	
		cin >> N;
		cout << "Case #" << i << ": ";
		if(N==0) cout << "INSOMNIA\n";
		else cout << solve(N) << '\n';
	}
	return 0;
}
