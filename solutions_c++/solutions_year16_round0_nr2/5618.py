#include<iostream>
#include<map>
#include<string>
#include<fstream>
#include<vector>
#include<queue>
#include<set>
#include<algorithm>
#include<stdio.h>
#include<math.h>
#include<cmath>
#include<string>

using namespace std;

int main(){

	int t;
	cin>>t;
	string s;
	int in = 0;
	while(t--){
		in++;
		cin>>s;
		int is = 1;
		int r = 0;
		for(int i=s.size()-1;i>=0;i--){
			if( (is == 1 && s[i]=='+') || (is == -1 && s[i]=='-')){
				continue;
			}
			if(s[0] == s[i]){
				r++;
				string p = s;
				for(int j=0;j<=i;j++){
					s[j] = p[i-j];
					if(s[j] == '-'){
						s[j] = '+';
					}
					else{
						s[j] = '-';
					}
				}
			}
			else{
				r++;
				is *= -1;
			}
		}
		
		cout<<"Case #"<<in<<": "<<r<<endl;
	}
	
	
	return 0;
}
