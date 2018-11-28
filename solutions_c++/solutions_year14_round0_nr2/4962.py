#include<iostream>
#include<string>
#include<fstream>
#include<iomanip>
using namespace std;
ofstream fout("out.txt");
double C,F,X;
double compute(int num){
	double c=C,f=F,x=X;
	double b = 2;
	double cost = 0;
	for(int i=0;i<num;i++){
		cost+=c/b;
		b+=f;
	}
	cost+=x/b;
	return cost;
}

int main(){
	int caseNum;
	cin>>caseNum;
	for(int ll=1;ll<=caseNum;ll++){
		cin>>C>>F>>X;
		double cost = X;
		for(int i=0;i<=(int)(X/C);i++){
			double mi = compute(i);
			if(mi>cost)
				break;
			cost = min(cost,mi);
		}
		fout<<"Case #"<<ll<<": "<<setiosflags(ios::fixed)<<setprecision(7)<<cost<<endl;
	}
}