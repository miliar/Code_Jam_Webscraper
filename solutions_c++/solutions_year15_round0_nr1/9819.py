#include <bits/stdc++.h>
#define MAX 1002
using namespace std;

int main() {
	int t, smax, k, i, cur;
	char arr[MAX];
	int cumulativesum, reqd;
	cin>>t;
	
	for(k=1; k<=t; k++){
		cumulativesum=0;
		reqd = 0;
		cin>>smax>>arr;
		
		for(i=0; i<=smax; i++){
			if((i - (cumulativesum + reqd)) > 0){
				cur = i - (cumulativesum + reqd);
				reqd += cur;
			}
			
			cumulativesum += (arr[i]-'0');
			
			//cout<<i<<"   "<<reqd<<"   "<<cumulativesum<<endl;
		}
		
		printf("Case #%d: %d\n", k, reqd);
		
	}
	
	return 0;
}