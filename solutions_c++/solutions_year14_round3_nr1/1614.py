#include <iostream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

int main(){

	int NSteps;
	cin >> NSteps;

	for(int t=1; t<=NSteps; t++){
		cout << "Case #" << t << ": ";

		long long int P, Q;
		char c;
		cin >> P >> c >> Q;
		while(P%2 == 0 && Q%2==0){
			P/=2;
			Q/=2;
		}
		for(int i=3; i<sqrt(Q); i++){
			while(P%i==0 && Q%i==0){
				P/=i;
				Q/=i;
			}
		}
		long long int b=1;
		bool valid = false;
		while(b<=Q){
			if(Q==b)
				valid=true;
			b*=2;
		}
		if(!valid)
			cout << "impossible" << endl;
		else if(Q==1 && P==1)
			cout << 0 << endl;
		else{
			bool finished=false;
			int sol, n=1;
			while(!finished){
				if(P>=Q/2){
					finished=true;
					sol=n;
				}
				else{
					P*=2;
					n++;
				}
			}
			cout << n << endl;
		}

	}
}
