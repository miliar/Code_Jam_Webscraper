#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <iomanip>
using namespace std;

int main () {
	string line;
	int noOfCase;
    double C,F,X,time,speed;
	  
	ifstream myfile ("B-large.in");
	if (myfile.is_open())
	{  
		ofstream myfileOut;
		myfileOut.open("output.out");
		getline(myfile,line);
		
		istringstream(line) >> noOfCase;
		
		for(int k=0;k<noOfCase;k++)
		{			
            getline(myfile,line);
            istringstream(line) >> C>>F>>X;
            
            time=0;
            speed=2;
            
            
            while(X/speed>C/speed + X/(speed+F))
            {
                time+=C/speed;
                speed+=F;
            }
            time+=X/speed;
            
            
            cout<<"Case #"<<k+1<<": "<<fixed << setprecision(8)<<time<<endl;			
            myfileOut<<"Case #"<<k+1<<": "<<fixed << setprecision(8)<<time<<endl;
        }
		
		myfileOut.close();				
		myfile.close();
	}
	else cout << "Unable to open file";
	
	return 0;
}