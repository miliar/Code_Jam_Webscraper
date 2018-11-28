 #include <iostream>
 #include <sstream>
 #include <string>
 #include <iomanip>
 
using namespace std;
  
double testcase()
{
      double C, F, X;
      double time = 0;
      double rate = 2; //base rate of cookie aggregation
		 
      cin >> C;
      cin >> F;
      cin >> X;
					        
      double tail=C/rate;
      double currvalue=X/(rate+F)+tail;
      double lastvalue=X/rate;

      rate+=F;
					        
      while (lastvalue > currvalue )
      {
	      lastvalue=currvalue;
	      tail+=C/rate;
	      currvalue=(X/(rate+F))+tail;
	      rate+=F;
      }
					     
						  
      return lastvalue;
							       
}
 
int main()
{
      stringstream output;
		       
      int Testcases;
			    
      cin >> Testcases;
      
      output << std::setprecision(7) << std::fixed;
				 
      for (int i = 0; i < Testcases; i++)
      {
           output << "Case #" << (i+1) << ": " << testcase() << "\n";
      }
		      
      cout << output.str();
					   
}
