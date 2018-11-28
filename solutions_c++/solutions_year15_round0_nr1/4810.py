#include "bits/stdc++.h"
using namespace std;

int main(){
	int t;
	cin >> t;
	int T=0;
	while(t--){
		T++;
		int smax;
		cin >> smax;
		string s;
		cin >> s;
		int array[smax];
		int cum[smax];
		int count = 0;
		for(int i=0; i<s.length(); i++){
			array[i] = int(s[i]-'0');
			if(i == 0){
				cum[i] = array[i];
			} 
			else{
				if(i>cum[i-1]){
					count = count + (i-cum[i-1]);
					cum[i-1] = i;
				}
				cum[i] = cum[i-1] + array[i];
			}
		}
		printf("Case #%d: %d\n",T,count);
	}
}