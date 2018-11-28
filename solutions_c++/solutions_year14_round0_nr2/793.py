#include<iostream>
#include<fstream>
#include<sstream>
#include<string>
#include<math.h>
#include<vector>

using namespace std;
int main(){
	ifstream in("B-large.in");
	ofstream out("output.txt");
	out.precision(7);
	out.setf(std::ios::fixed, std::ios::floatfield);
	int testcase;
	in>>testcase;
	for(long t=1;t<=testcase;t++){
		double farmcost,farmproduct,required,total=0.0;
		in>>farmcost;
		in>>farmproduct;
		in>>required;
		double inc=2.0;
		double totaltime=0.0;
		if(required<farmcost)
		     out<<"Case #"<<t<<": "<<required/(2.0)<<endl;
        else{
        	totaltime=farmcost/inc;
        	while(1){
	        	total=farmcost;
        	    double way1,way2;
        	    way1=(required-total)/inc;
        	    way2=required/(inc+farmproduct);
        	    if(way1<way2){
        	    	totaltime=totaltime+way1;
    	        	out<<"Case #"<<t<<": "<<totaltime<<endl;
    	        	break;
    	        }
    	        else{
        	    	inc+=farmproduct;
        	    	total=0;
        	    	totaltime+=(farmcost/inc);
        	    }
	        }
        }
	}
}