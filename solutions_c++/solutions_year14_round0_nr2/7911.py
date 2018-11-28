#include <iostream>
#include <string>
#include <vector>
#include <cstdio>

using namespace std;

int main(){
	int T;
	cin>>T;
	for(int i=0; i<T; i++){
		double C, F, X, t = 0, prod = 2;
		cin>>C>>F>>X;
		
		while(true){
			double timing = X/prod;
			double predict = C/prod + X/(prod+F);
			//cout<<timing<<" "<<predict<<endl;
			if(timing < predict){
				t += timing;
				break;
			} else{
				t += C/prod;
				prod += F;
			}
		}
		printf("Case #%d: %.7f\n", i+1, t);
	}
	return 0;
}