#include<iostream>
#include<fstream>
#include <iomanip>
using namespace std;

int main(){
	int T;
	
	double C,F,X;
	double ret;
	fstream myfile,myin;
	myfile.open("d:\\data.txt",ios::out);
	myin.open("d:\\B-large.in",ios::_Nocreate);

	myin>>T;
	for(int i=1; i<=T; i++){
		ret = 0.0;
		double rate = 2.0;
		myin>>C>>F>>X;
		while(X > C && X/(rate+F) < (X-C)/rate){
			ret += C/rate;
			rate += F;
		}
		ret += X/rate;
		myfile<<setiosflags(ios::fixed);
		myfile<<"Case #"<<i<<": "<<setprecision(7)<<ret<<endl;
	}
	system("puase");
	return 0;
}