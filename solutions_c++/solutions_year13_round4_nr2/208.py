#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <utility>
#include <cmath>
#include <list>
#include <map>
#include <vector>
#include <stack>
#include <queue>
using namespace std;
long long computeAnswer(long long N, long long P){
	if(P <= (1ll << (N-1))){
		return 0;
	}
	long long k = computeAnswer(N-1, P - (1ll << (N-1)));
	return min(2*k + 2, (1ll << N) - 1);
}
int main(){
	int T;
	cin >> T;
	for(int t=0;t<T;t++){
		long long N, P;
		cin >> N >> P;
		if(P < (1ll<<N)){
			cout << "Case #" << (t+1) << ": "<< computeAnswer(N,P) << " " << (1ll << N) - 2 - computeAnswer(N, (1ll<<N) - P) << endl;
		}
		 else {
		 	cout << "Case #" << (t+1) << ": "<< (1ll << N) - 1 << " " << (1ll << N) - 1 << endl;
		 }
	}
	return 0;
}
