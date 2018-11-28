#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

int main ( )
{
    ifstream input ( "sample1.txt" );
    ofstream output ( "output.txt" );
    
    int test;
    input >> test;
    
    double C , F , X;
    double result1 , result2;
    
    for ( int testcase=1 ; testcase <= test ; ++testcase )
    {
        result1 = 0;
        double time = 0;
        double cookie_per_sec = 2;
        
        input >> C;
        input >> F;
        input >> X;
        
        
            if ( X <= C )
            {
                 result1 = X / cookie_per_sec;
            }
            else
            {
            
            		do {
            			result1=time+X/cookie_per_sec;
            			result2=time+C/cookie_per_sec+(X/(cookie_per_sec+F));
            				
            				time+=C/cookie_per_sec;
            				cookie_per_sec+=F;
            			
            			}while (result2<=result1);
            			
        	}
        
       // cout << "Case #" << testcase << ": " << fixed << setprecision(7) << result1 << endl;
        output << "Case #" << testcase << ": " << fixed << setprecision(7) << result1 << endl;
    }
  //  system("pause");
}
