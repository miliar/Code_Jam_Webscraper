
#include<iostream>
#include<fstream>
#include<iomanip>
#include<string>
using namespace std;
int main(){
	ifstream ifile;ofstream ofile;ifile.open("cookie.in");ofile.open("cookie.txt");
	int cases;
	double farm,extra,goal,time1,time2,inc,finc,fut,curr;
	ifile>>cases;
	for(int z=0;z<cases;z++){
		curr=time1=time2=0;inc=2;
		ifile>>farm>>extra>>goal;
		while(1){
			fixed;setprecision(10);
			time1=curr+goal/inc;
			finc=inc+extra;
			time2=curr+(farm/inc);
			fut=(goal/finc);
			fixed;setprecision(10);
			time2=time2+fut;
			if(time2>time1){
				curr=time1;break;}
			curr=curr+farm/inc;
			inc=finc;
		}
		ofile<<"Case #"<<z+1<<": "<<fixed<<setprecision(10)<<curr<<endl;
	}
	return 0;
}