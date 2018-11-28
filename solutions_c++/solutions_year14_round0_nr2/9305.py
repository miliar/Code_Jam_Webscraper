 
 

#include <iostream>
#include <iomanip>
#include <fstream>
 

int main()
{
	using namespace std;
	cout << setprecision(10);
	
   int T = 1;
   	 
	ofstream myfile;
  myfile.open ("example.in");
  myfile << setprecision(10);
   
  cin >> T;
 for(double iii =1.0000000f; iii<=T; iii++)
 {
	  double y=0.0000000f ;
	  double C=0.0000000f;
	double F=0.0000000f;
	double X=0.0000000f;
      double Cp=2.0000000f;
	 
 	cin >> C ;
	 
 	cin >> F;
	 
 	cin >> X;
  
	 
		while((X/Cp)>((C/Cp)+(X/(Cp+F))))
			{
				y= y + (C/Cp);
				Cp=F+Cp;
			}
			y= y+(X/Cp);

cout << y << endl;
  myfile << "case #" << iii <<": " << y << endl;
  
		 
		
 }
 	myfile.close();
   
	return 0;
}

 
 