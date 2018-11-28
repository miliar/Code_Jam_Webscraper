
#include <iostream>
#include <iomanip>

using namespace std;

int main() {
	//double w;


	int T;
	cin>>T;
	//cout.precision(5);
	 std::cout << std::fixed;
	    std::cout << std::setprecision(7);
	for(int i=0;i<T;i++){

		long double C,F,X,rate;
		rate=2;
		cin>>C>>F>>X;
		//cout<<C<<" "<<F<<" "<<X<<endl;
		bool canimprove=true;
		long double currenttime=0;
		while(canimprove){

			if(currenttime+C/rate+X/(rate+F)<currenttime+X/rate){
				currenttime=currenttime+C/rate;
				rate+=F;

				//cout<<currenttime<<" "<<rate<<endl;
			}else{
				currenttime=currenttime+X/rate;
				canimprove=false;
			}
		}
		//get size
		cout<<"Case #"<<(i+1)<<": ";
		//<<setprecision(c)
		cout<<currenttime<<endl;
	}
	return 0;
}
