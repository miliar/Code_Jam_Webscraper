#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int main(){
	
	ifstream input;
	input.open("A-small-attempt2.in");
	ofstream output;
	output.open("A-small-output.txt");

	int test_num;
	input>> test_num;
	
	for(int loop=0; loop<test_num; loop++){
		long long int r, t;
		input>>r>>t;

		long long int a = 2*r+1;
		long long int n = 1000000000;
		long long int q = n/2;
		for(int loop2=0; loop2<100; loop2++){
			long long int temp = 2*n*n - 2*n + a*n;
			if(temp > t)
				n -= q;
			else if(temp <= t)
				n += q;
			q /= 2;
		}

		while(1){
			long long int temp = 2*n*n - 2*n + a*n;
			if(temp < t)
				n++;
			else
				break;
		}

		while(1){
			long long int temp = 2*n*n - 2*n + a*n;
			if(temp > t){
				n--;
			}
			else
				break;
		}
		//output<<r<<" "<<t<<endl;
		output<<"Case #"<<loop+1<<": "<<n<<endl;
	}

	input.close();	
	

	return 0;
}