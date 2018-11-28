#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main() {
	int N; 
	cin>> N ; 

	for(int T = 1 ; T <= N ; T++) {
		int Sm; string s;
		cin>> Sm >> s;
		
		int ret = 0;
		int sum = 0;
		for(int i = 0 ; i <= Sm ; i++){
			int Si = s[i] - '0';
			int need = max(i - sum, 0);
			ret += need;
			sum += (Si + need);
		}

		cout<<"Case #"<<T<<": "<<ret<<endl;
	}
	return 0 ;
}