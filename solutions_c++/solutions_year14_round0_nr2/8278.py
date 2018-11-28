#include <iostream>

using namespace std;

bool debug=false;

int main(){
	int numberOfTestCases;
	
	cin>>numberOfTestCases;
	
	for(int n=1;n<=numberOfTestCases;n++){
		double C,F,X,T;
		double currentTime=0;
		double numberOfCookies=0;
		int numberOfFarms=0;
		cin>>C>>F>>X;
		while(numberOfCookies<X){
			double timeWithoutBuying=(X-numberOfCookies)/(2+numberOfFarms*F);
			double t2=(((C)/(2+numberOfFarms*F))*(2+numberOfFarms*F))/F;
			double t1=C/(2+numberOfFarms*F);
			if(t1+t2>timeWithoutBuying){
				if(debug)
				cout<<currentTime<<" To "<<currentTime+timeWithoutBuying<<endl;
				currentTime+=timeWithoutBuying;
				break;
			} else {
				if(debug)
				cout<<"Farms: "<<numberOfFarms<<" in "<<currentTime<<" To "<<currentTime+t1<<endl;
				currentTime+=t1;
				numberOfFarms++;
				
			}
		}
		cout<<"Case #"<<n<<": "<<std::fixed<<currentTime<<endl;
	}
	
	return 0;
}
