#include <iostream>
#include <fstream>
#include<iomanip>
using namespace std;

int main () {
  ofstream myfile;
  ifstream input;
  input.open("file.in");
   myfile.open ("example.txt");
 
   int n;
	input>>n;
	for(int i=1; i<=n; i++){
		double c, f, x;
		input>>c>>f>>x;
		double fk=0;
		double time = 0;
		double totaltime=x/2;
		int n0 = (f*x-2*c)/c*f;
		if(n0<0)n0=0;	
	
		for(int j=0; j<n0; j++){
			fk+=c/(2+j*f);
			time=x/(2+(j+1)*f);
			if(fk>totaltime)break;
			if(fk+time<totaltime){
				totaltime=fk+time;
			}
		}
		myfile<<"Case #"<<i<<": ";	
		myfile << fixed << setprecision(7) << showpoint <<totaltime<<endl;
	}
   
   
  myfile.close();
  input.close();
  return 0;
}
