#include <bits/stdc++.h>
using namespace std;

int main(){
	int t;
	cin>>t;
	for(int testcase=1; testcase<=t; testcase++){
		int smax;
		cin>>smax;
		string s;
		cin>>s;
		if(smax==0){
			printf("Case #%i: 0 \n", testcase);
			continue;
		}

		//cout<<s<<endl;
		
		int countTillNow = 0;
		int needed = 0;
		for(int i=0; i<smax+1; i++){
			//printf("i is %i, countTillNow is %i \n",i,countTillNow);
			if(countTillNow>=i){
				countTillNow += s[i]-'0';
			}
			else{
				int tempNeeded = i - countTillNow;
				needed += tempNeeded;
				countTillNow += s[i]-'0' +tempNeeded;	
			}
		}
		printf("Case #%i: %i \n", testcase, needed);
		
	}
}