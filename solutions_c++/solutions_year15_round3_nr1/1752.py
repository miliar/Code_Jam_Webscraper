#include "bits/stdc++.h"

using namespace std;

int main(){
	int t; cin>>t;
	int j;
	for(j = 1; j <= t; j++){
		printf("Case #%d: ", j);
		int r, c, w; cin>>r>>c>>w;
		if(w*2 >= c){
			cout<<min(c,w+1)<<endl;
		}
		else{
			int i;
			for(i = 0; i < 10; i++){
				if(c-i*w < w*2) break;
			}
			cout<<min(c,i+min(c-i*w,w+1))<<endl;
		}
	}
}
