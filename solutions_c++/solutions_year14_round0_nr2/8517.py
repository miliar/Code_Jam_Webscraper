#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>


using namespace std;

double timewfarm(double cps, double c){
    return (c/cps);
}

double time2win(double cps, double x){
	return (x/cps);
}


int main(int argc, char* argv[])
{
	ifstream input("B-large.in");
	//ifstream input("test.data");
    ofstream output("output.out");

    
	int cases;
	
	input >> cases;

    for(int i=1;i<=cases;i++){
         output << "Case #"<<i<<": ";

	     double c,f,x;
	     input >> c;
	     input >> f;
	     input >> x;
	     double cps = 2.0;
	     double timer = 0;
         bool flag = false;
         while (flag == false){

             double farm = timewfarm(cps,c);
             double win = time2win(cps,x);
             double newwin = time2win(cps+f,x);
   

             if (farm+newwin > win){
	             //not worth buying
	             timer += win;
	             flag = true; 
		    }
            else
            {
    	         timer += farm;
    	         cps += f;
            }
        }
        output << fixed << setprecision(7) << timer << endl;
 	}

    input.close();
	output.close();


	return 0;
}

