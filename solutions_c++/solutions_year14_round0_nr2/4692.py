#include<iostream>
#include<fstream>
#include<algorithm>
using namespace std;
//const double err=1E-8;
const double inf=1E7;
class cookie{
private:
	double C;
	double F;
	double X;
	//double cookieNum;
	//double interval;
	double cmp;
	double DFS(double rate,double& target);
public:
	void set(ifstream& fin);
	double minTimeCost();
};

void cookie::set(ifstream& fin){
	fin>>C>>F>>X;
	//cout<<C<<" "<<F<<" "<<X<<endl;
}

double cookie::DFS(double rate,double& target){
	double res1=target/rate;
	//cout<<"res1: "<<res1<<endl;
	//cout<<"cmp: "<<cmp<<endl;
	if(res1>cmp)
		return cmp;
	else
		cmp=res1;
	//cout<<"cmp: "<<cmp<<endl;
	double interval=C/rate;
	//cout<<"rate: "<<rate<<endl;
	//cout<<"interval: "<<interval<<endl;
	cmp-=interval;
	double res2=interval+DFS(rate+F,target);
	//cmp+=interval;
	//cout<<"res2: "<<res2<<endl;
	return min(res1,res2);
}

double cookie::minTimeCost(){
	cmp=inf;
	//cout<<endl;
	return DFS(2.0,X);
}

void main(){
	ifstream  fin;
	ofstream  fout;
	fin.open("B-small-attempt0.in");
	fout.open("B-small-attempt0.out");
	int T;
	fin>>T;
	cookie solve;
	fout.setf(ios::showpoint);
	fout.precision(7);
	fout.setf(ios::fixed);
	for( int i=1; i<=T; i++){
		solve.set(fin);
		fout<<"Case #"<<i<<": ";
		fout<<solve.minTimeCost()<<endl;
	}
}