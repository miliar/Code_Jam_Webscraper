#include <iostream>
#include <string>
#include <iomanip>      // std::setprecision
using namespace std;

int main(){
	int n;
	cin>>n;
	string output[n];
	double output_d[n];
	for (int k=1; k<=n; k++){
		long double C,F,X;
		cin>>C;
		cin>>F;
		cin>>X;
		//cout<<"c: "<<C<<",f: "<<F<<",x: "<<X<<endl;
		int i=2.0;
		double t1 = X/2.0;
		double t2 = C/2.0 + X/(2.0 + F);
		while(t1 > t2){
			t1 = t2;
			t2 = t1 + (X/(2.0 + i*F)) + (C/(2.0 + (i-1)*F)) - (X/(2.0 + (i-1)*F));
			i += 1.0;
		}
		//std::ostringstream strs;
		//strs << t1;
		std::setprecision(9);
		output[k-1] = "Case #" + std::to_string(k) + ": ";
		output_d[k-1] = t1;
	}
	std::cout.setf( std::ios::fixed, std:: ios::floatfield );
	for (int i=0; i<n; i++){
		cout<<output[i]<<std::setprecision(7)<<output_d[i]<<endl;
	}
	return 0;
}