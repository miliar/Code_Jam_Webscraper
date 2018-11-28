#include<iostream.h>
#include<sstream>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<fstream.h>
using namespace std;
main()
{
	ifstream in("B-large.in");
    ofstream out("output.txt");
	out.precision(7);
	out.setf(std::ios::fixed, std::ios::floatfield);
	int cases;
	in>>cases;
	for(int i=1;i<=cases;i++)
	{
		double fp;
		double poe,inc=2;
		double tot;
		double time=0;
		double r=0;
		double tem;
		in>>fp;
		in>>poe;
		in>>tot;
		
		if(fp>=tot)
		 time=tot/2;
		 else
		 {
 			time+=fp/inc;
 			
 			
		 while(1)
		 {
		 r=fp;
		 tem=tot-r;
		  double w1=tem/inc;
		  double w2=tot/(inc+poe);
		  if(w1<w2)
		  {
  			time+=w1;
  			
  			break;
  		}
 		else
		 {
 			inc+=poe;
 			r=0;
 			time+=fp/inc;
 		}	
 		}
 		
		 }
	 out<<"Case #"<<i<<": "<<time<<endl;
		}

	
}