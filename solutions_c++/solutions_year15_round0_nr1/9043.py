#include <bits/stdc++.h>
using namespace std;

int main(){
	int tc; cin>>tc;
	for(int z=1;z<=tc;z++){
		printf("Case #%d: ",z);
		int smax = 0; cin>>smax;
		string shy = ""; cin>>shy;
		int clapping = 0;
		int extras = 0;
		for(int i=0; i<shy.size(); i++){
			if(clapping < i){
				extras += (i-clapping);
				clapping += (i-clapping);
			}
			clapping += (shy[i] - '0');
		}
		printf("%d\n",extras);
	}
	return 0;
}