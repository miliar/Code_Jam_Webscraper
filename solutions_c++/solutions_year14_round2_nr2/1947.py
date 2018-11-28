#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int cnt=0;

int main(){
	int t;
	cin >> t;
	while(t--){
		int a, b, k, res=0;	
		cin >> a >> b >> k;
		for(int i=0; i<a; ++i){
			for(int j=0; j<b; ++j){
				int tmp = i&j;
				//cout << tmp << " ";
				if(tmp < k) res++;	
			}	
		}
		printf("Case #%d: %d\n", ++cnt, res);
	}
	return 0;
}
