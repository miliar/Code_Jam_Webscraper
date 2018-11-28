#include<cstdio>
#include<cmath>
#include<iostream>
#include<string>

using namespace std;

#define MAXD 1024

int P[MAXD];

int main(){
	int T;
	cin >> T;
	for(int k=0; k<T; k++){
		int D;
		cin >> D;
		int mres=0;
		for(int i=0; i<D; i++){
			cin >> P[i];
			mres=max(mres,P[i]);
		}
		int res=mres;
		for(int i=1; i<mres; i++){
			int t=i;
			for(int j=0; j<D; j++)
				t+=(P[j]-1)/i;
			res=min(res,t);
		}
		
		cout << "Case #" << (k+1) << ": " << res << "\n";
	}
}
