#include<iostream>
#include<stdlib.h>
#include<string>
using namespace std;
int n,k;
int a = 0;
int r = 0;
string shy;
int main () {
	cin >> n;
	for(int i = 1;i<=n;++i){
		cin >> k;
		cin >> shy;
		for(int j = 1;j<=k;j++){
			a+= atoi (shy.substr(j-1,1).c_str());
			if(a<j){
				r+= j-a;
				a=j;
			}
		}	
		cout << "Case #" << i << ": "<< r <<endl;
		r = 0;
		a = 0;
	}
	return 0;
}
