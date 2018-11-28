#include<iostream>
#include<fstream>
using namespace std;

static const bool debug=true;

double findBest(double C, double F, double X){

	double totalTime=-1;
	double best=-1;
	int i=0;
	while(best<0 || best>totalTime){
		best=totalTime;

		double time=0;
		double production=2;
		for(int j=0;j<i;++j){
			time+=C/production;
			production+=F;
		}
		totalTime=time+X/production;
		++i;
	}
	return best;
}

int main(){

	ifstream input;
	ofstream output;
	input.open("2a.in");
	output.open("2a.out");
	output.precision(12);
	cout.precision(12);

	int T;
	input>>T;

	double C;
	double F;
	double X;
	double result;

	for(int i=0;i<T;++i){
		input>>C;
		input>>F;
		input>>X;

		if(debug)
			cout<<C<<" "<<F<<" "<<X<<"\n";

		result=findBest(C,F,X);

		if(debug)
			cout<<"result:\t"<<result<<"\n";

		output<<"Case #"<<(1+i)<<": "<<result<<"\n";
	}

	input.close();
	output.close();
	return 0;


}
