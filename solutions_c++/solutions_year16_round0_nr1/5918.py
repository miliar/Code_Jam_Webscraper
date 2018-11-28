#include <iostream>
#include <sstream>
#include <string>
#include <math.h>

#define mp(a, b) make_pair(a, b)
typedef long long ll;
using namespace std;



int main(){
	int  in;
	int num;
	cin >> num;
	int digit;//1111111111
	for (int i = 0; i < num; i++){
		cin >> in;
		
		//
		if (in == 0){
			cout <<"Case #"<<i+1<<": "<<"INSOMNIA"<< endl;
			continue;
		}
		//init
		digit = 0;


		//multiplication
		for (int t = 0; t < 1000; t++){
			int in2 = in*(t + 1);
			//cout << in2 << endl;
			//add number
			while (in2 != 0){
				int di = pow(2, in2 % 10);
				//cout << "add:" << in2%10 <<" "<<di<<endl;
				digit = digit| di;
				in2 /= 10;
			}
			if (digit == 1023){
				cout << "Case #" << i + 1 << ": " << in*(t + 1) << endl;
				break;
			}
		}



	}




	return 0;
}