#include <string>
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <sstream>
#include <cmath>

using namespace std;

int dp[10000005];

int main(){

	long long nice[40] = {1,2,3,11,22,101,111,121,202,212,1001,1111,200,10001,10101,10201,11011,11111,11211,20002,20102,100001,101101,110011,111111,200002,1000001,1001001,1002001,1010101,1011101,1012101,1100011,1101011,1102011,1110111,1111111,2000002,2001002,10000001};

	int T;
	cin >> T;
	for(int t=1;t<=T;t++){
		long long A,B;
		cin >> A >> B;

		int idx1 = -1;
		for(int i=0;i<40;i++){
			if(nice[i]*nice[i]>=A){
				idx1 = i;
				break;
			}
		}

		int idx2 = -1;
		for(int i=39;i>=0;i--){
			if(nice[i]*nice[i]<=B){
				idx2 = i;
				break;
			}
		}

		cout<<"Case #"<<t<<": "<<max(0,idx2-idx1+1)<<endl;
	}
}