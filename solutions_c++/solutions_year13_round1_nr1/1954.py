#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <cmath>
#include <fstream>

using namespace std;
   int A, B, C, D, E, F, G, H, I;
   ofstream fout;
   ifstream fin;
   
int main()
{
	fout.open("lol.txt");
   fin.open("hello.in");
	 int y;
	 fin >> y;
	 fin.get();
	 for(int i = 0; i < y; i++)
	 {
		 
		  I = 0;
		  fin >> A;
		  fin.get();
		  fin >> B;
		  fin.get();
		  if ( A > B)
			  I = 0;
		  C = 0;
		  F = B;
		  for( A; A <=F; A = A + 2)
		  {
			    
			   D = A + 1;
			   A = A*A;
			   D = D*D;
			   if((C =(D-A)) <= B)
				   {I++;
			   B = B - C;
			   E = I;}
			   else break;
			   A = sqrt(double (A));
			    
			    
		  }
		  fout << "Case #" << (i+1) << ": " << E << endl;
	 }
		  
	while(true);
	return 0;
}