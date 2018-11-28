#include <iostream>
#include <vector>
#include <string>
#include <bits/stdc++.h>
using namespace std;


int main(){

	int t;
	cin>>t;
int d=1;
		int numm=0;

	while(t--){
		numm=0;
		string s;
		cin>>s;
		int prev=0;//becomes 1 if last seen was - 
		for(int i=0;i<s.length();i++){
			if(s[i]=='-' && prev==2){
				prev=0;
				numm++;
			}

			if(s[i]=='-' && prev==0){				
				prev=1;
				numm++;
			}

			else if(s[i]=='+' && prev==0 ){

				
				prev=2;
				//numm++;
			}

			else if(s[i]=='+' && prev==1 ){

			
				prev=2;
				//numm++;
			}



			else continue;
		}

		printf("Case #%d: %d\n",d,numm);
		d++;
	}

	return(0);
}