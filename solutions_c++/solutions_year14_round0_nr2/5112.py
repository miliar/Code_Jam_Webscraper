#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;


int main()
{
	int testcase;
	long double c,f,x;
	
	ifstream input("input1.in",ios::in);
	ofstream output("output.out",ios::out);    //|ios::app
	
	input>>testcase;
	
	for (int i=0;i<testcase;i++) {
	    long double cum_f=2.0;
	    long double cum_timer=0.0;
        
        input>>c>>f>>x;
        
        while(cum_timer+ (c/cum_f) + (x/(cum_f+f)) < cum_timer + (x/cum_f)) {
        /* 
        if i buy a new factory and time required to reach target faster than i just sit there and wait for it to generates
           then buy it. else wait it generates
        */
            cum_timer = cum_timer+c/cum_f;
            cum_f=cum_f+f;
        } 
        cum_timer =  cum_timer + x/cum_f;  

	    output<<"Case #"<<i+1<<": ";
        output<<std::fixed;
        output<<std::setprecision(7);
        output<<cum_timer;
        output<<endl;
    }
	input.close();
	output.close();

}

