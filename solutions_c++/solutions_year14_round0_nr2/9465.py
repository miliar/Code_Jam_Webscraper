#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;

int main(){
	ifstream infile("B-small-attempt3.in");
	ofstream ofile("output2.txt");
	double c,f,x,i,time1=1.0000000,time2=0.0000000;
	double total[100];
	int test,t=0,k;
	infile>>test;
	for(k=0;k<test;k++){
		total[k]=0;
		i=2.0000000;
		infile>>c>>f>>x;
		while(time1>time2){
			time1=x/(i);
			time2=(c/(i))+(x/(i+f));
			if(time2<time1){
				total[k]+=(c/(i));	
			}else{
				total[k]+=(x/(i));
				break;
			}	
			i+=f;
		}
		time1=1.0000000;
		time2=0.0000000;	
	}
	ofile.precision(7);	
	ofile.setf(ios::fixed);
	ofile.setf(ios::showpoint);
	for(k=0;k<test;k++){
		ofile<<"Case #"<<(k+1)<<": ";
		ofile << total[k];
		ofile<<"\n";
	}
	return 0;
}
