#include <iostream>

using namespace std;

int main(){
	int T;

	cin>>T;

	for(int TCN = 1; TCN<=T; TCN++){
		double Dep, Ep, Fp;
		cin>>Dep>>Ep>>Fp;

		int max = Fp/Dep;
		double Curp=2;
		double FiTime = Fp/Curp;
		double FaTime=0;
		for(int i =0; i<max; i++){
			FaTime = FaTime + Dep/Curp;
			Curp+=Ep;
			if(FiTime > FaTime + Fp/Curp)
				FiTime = FaTime + Fp/Curp;

		}
		cout.setf(ios::fixed);
		cout.precision(7);
		cout<<"Case #"<<TCN<<": "<<FiTime<<endl;
	}




	return 0;
}