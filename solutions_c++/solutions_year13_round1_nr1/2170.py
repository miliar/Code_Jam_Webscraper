#include <stdio.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

int main()
{
  std::ifstream in("in");
  int cases;
  std::string casess;
  getline(in,casess);
  sscanf(casess.c_str(),"%d",&cases);
  

  char c;
//  in >> c;

  char orig []="abcdefghijklmnopqrstuvwxyz";
  char trans[]="yhesocvxduiglbkrztnwjpfmaq";

  const double pi = 3.14159265;
  
  for (int icase=0;icase<cases;icase++)
    {
      long r,t;
      in >> r >> t;

      /*
      double a = -(2.0*r+3)/4.0;
      double b= std::sqrt(a*a-(2.0*r +1.0 - t/pi)/2.0);
      */
      /*
      double a=-(r+1.0)/2.0;
      double b=std::sqrt(a*a-(r+1.0)*(r+1.0)/4.0+r/4.0+t/pi/4.0);
      std:: cout << r << " " << t << " " << a+b << " " << a-b << std::endl;
      
      double n = std::max(a+b,a-b);
      long nn = std::floor(n);
      */

      /*
      double a=-(r)/2.0;
      double b = std::sqrt(a*a-(2.0*r+1-t)/4.0);
      double n = std::max(a+b,a-b);
      long kk = std::floor(n);
      */

      
      
      long val=0.0;
      long rr=r;
      long k=0;

      while (true)
	{
	  val += (2*rr+1);
 	  if (val > t)
	    break;
	  rr+=2;
	  ++k;
     	  
	}
      //std::cout << kk << " " << k << std::endl;
      

      
      
      
      
      std::cout << "Case #" << icase+1 << ": ";
      std::cout << k;

      std::cout << std::endl;

    }
  return 0;
}
