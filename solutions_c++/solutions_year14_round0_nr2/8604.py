#include <iostream>
#include <sstream>
#include <fstream>
using namespace std;
bool check(double bld, double rate,double curr, double cook)
 {     double p=bld/curr;
	double q=rate+curr;
	double r=cook/curr;
	double s=cook/q;
	if((p+s)<r)return false;
	else return true;
}

int main(int argc, char* argv[] ){
	ifstream in(argv[1],ios::in);
	ofstream out("output1",ios::out);
	out.precision(12);
	int cases;
	in>>cases;
	int count=0;
	while(count<cases)
	{  	double cost,F,X;
		in>>cost;in>>F;in>>X;
		double t=0.0;
		double cookies=0.0, crate=2.0;
		
		while(true){
		if(check(cost,F,crate,X)){t+=X/crate;break;}
		else {	t+=cost/crate;
			crate+=F;	
		    }
		}
		count++;double time=t;
	out<<"Case #"<<count<<": "<<time<<endl;
       }	
		
}
		
		
		
