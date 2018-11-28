#include <fstream>
#include <cstdio>
#include <string>


using namespace std;

int main(int argc, char **argv)
{
    ifstream input("input.txt",ios::in);
    //ofstream output("output.out", ios::out);
	
	//number of test cases
	int t;
	int cas;

	double c,f,x;
	double g=2.0;
	double time;
 
	
    
	input>>t;
	
	for(cas=0; cas<t; ++cas){
		
		input>>c>>f>>x;
	
		double a=(x-c)/x;
		//#farms bought:
		int teeth=max(0,(int)(1/(1-a)-g/f));
		
		if(teeth==0.)
			time=x/g;
		else{
			time=0.;
			for(int i=0; i<teeth; ++i)
				time+=c/(g+i*f);
			time+=(x/(g+teeth*f));
		}
		
		
		printf("Case #%d: %.7f\n",(cas+1),time);
			
		
		
		
	}
	
	return 0;
}
