#include <cstdlib>
#include <iostream>
#include <math.h>
#include "set"

using namespace std;

long long ToLong(string s) {
     long long result = 0;
     int decimalfound = 0;
     int decimaldigit = 0;
     for (int i=0; i< s.length(); i++){
         if (s[i]!= '.') {
            result = result * 10;
            result = result + s[i] - 48;
            if (decimalfound==1) decimaldigit++;
            } else decimalfound =1;
            
     }
         while (decimaldigit<7) {
               decimaldigit++;      
               result = result * 10;
         }
     return result;
     }

int main(int argc, char *argv[])
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int T;
    cin >> T;

	int y;
	long double lC,lF,lX,lS;
	float Curr_T, Next_T, Elap_T, Cost_T; 
	long double lCurr_T,lNext_T,lElap_T,lCost_T, lExp;
	
	int notfound;
    for (int T_i=0; T_i<T;T_i++){
        cin.precision(7);
        cin >> lC >> lF >> lX;
        
        notfound = 1;
        Elap_T=0;
        
        
        
        lS =  2;
        lElap_T = 0;
        while (notfound){
              lCurr_T = (((lX/lS)  )) + lElap_T;
              lCost_T = ((( lC/lS) ));
              lS = lS + lF;
              lNext_T = lCost_T + lElap_T + (( (lX/lS) ));
              lElap_T = lCost_T + lElap_T;
              if (lCurr_T <= lNext_T) notfound = 0;
              }
        
        
        cout.precision(12);
        cout << "Case #" << T_i+1 << ": " << lCurr_T << endl;
    }
    return EXIT_SUCCESS;
}
