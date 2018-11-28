#include <iostream>
#include <string>
#include <cmath>
using namespace std;
int main() {
	int T,N,digit,n,exp,x;
	bool allFound;
	cin>>T;
	for(int t=1;t<=T;t++){
		bool digits[10]={0,0,0,0,0,0,0,0,0,0};
		cin>>N;
		if(N==0){
			cout<<"Case #"<<t<<": INSOMNIA"<<endl;
			continue;
		}
		allFound=false;
		for(int y=1;!allFound;y++){
			allFound=true;
			n=N*y;
			x=n;
			//cout<<endl<<n;
			for(exp=0;n/pow(10,exp)>=1;exp++);
			for(int i=exp-1;i>=0;i--){
				digit=(int)(n/pow(10,i));
				//cout<<" "<<digit;
				digits[digit]=true;
				n=n-digit*pow(10,i);
			}
			for(int i=0;i<10&&allFound;i++)if(digits[i]==0)allFound=false;
			if(allFound){
				cout<<"Case #"<<t<<": "<<x<<endl;
			}
		}
	}
	return 0;
}
