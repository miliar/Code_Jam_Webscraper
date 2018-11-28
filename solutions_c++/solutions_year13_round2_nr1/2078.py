#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int T;
int A,N;
vector<int> motes;

int calcRes() {
	int res = N;
	int adds = 0;
	int i = 0;
	for( int k = 0; k < 101; k++) {
		if( i == N ) {
			break;
		}
		if( motes[i] < A ) {
			A += motes[i];
			i++;
			res = min(res, adds + N - i);
		} else {
			adds++;
			if( A == 1 ) {
				return N - i;
			}
			A += (A-1);	
		}
	}
	return res;
}

int main() {
	scanf("%d", &T);
	for( int t = 0; t < T; t++) {
		scanf("%d %d", &A, &N);
		motes.resize(N);
		for( int n = 0; n < N; n++) {
			scanf("%d", &motes[n]);
		}
		sort(motes.begin(), motes.end());
		int res = calcRes();
		cout<<"Case #"<<t+1<<": "<<res<<endl;
	}
}
