#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;
 
int main() {
	
	ofstream fout;
	ifstream fil;
	fil.open("B-large.in",ios::in);
    fout.open("output.txt",ios::out);
    int t;
	fil>>t;
	for(int casea =1;casea<=t;casea++)
	{
            //All we have to see if current time to c + time taken to x with increase in rate after c is greater than to 
            //not buy a farm at this stage, but rather save up till x now
            double f,x,c;
            double rate = 2;
            fil>>setprecision(9)>>c>>setprecision(9)>>f>>setprecision(9)>>x;
            double timeifbuy = 0;
            int a = 0;
            double timetosaveupnow=0;
            double totaltime = 0;
            do
            {
                  timeifbuy = (c/rate)+(x/(rate+f));   //increase rate if buying
                  timetosaveupnow = (x/rate); 
                  if(timeifbuy<=timetosaveupnow)
                  {
 
                   totaltime+=(c/rate);
                   rate+=f;
                  }else
                  {
 
                       a = 1;
                       totaltime+=timetosaveupnow;
                  }
            }while(!a);           
            fout<<"Case #"<<casea<<": "<<setprecision(9)<<totaltime<<endl;
            
    }
   
    fil.close();
    fout.close();
	return 0;
}
