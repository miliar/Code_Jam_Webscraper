#include <iostream>
#include <fstream>
#include <algorithm>
#include <cmath>
using namespace std;

int main()
{
  
    std::ifstream cin("input.txt"); 
   
    int n = 0;
    int T;
    double chk2;
    double f, N, L, chk1, newf;
    char c;
    
    
    cin >> T;
    
    for (int i=0; i < T; i++)
    {
        
      cin >> N;
      cin >> c;
      cin >> L;
      
      f = N/L;
      //cout << "\n N is" << N<< "L is "<< L<< " f is "<< f;
      
      for ( int g = 0; g < 40 ; g++)
      {
          
         if( (f*pow(2,g) -1) < 0)
         exit;
         else
         if(   ( (f*pow(2,g) ) -1 >= 0 ) &  
            ( (f*pow(2,g) - 1) * pow(2,40-g)  ) < pow(2,40-g)             
             )
             
             {
                 
                 
              newf = (f*pow(2,g) - 1) * pow(2,40-g);
              chk2 = floor(newf); 
             
              chk1 = newf - chk2; 
             // cout <<"\n new f is "<< newf << "  int part is"<<chk2<<" dec part is "<< chk1;
             // if( chk1 == chk2)
              if ( (chk1 == 0.0f)  )
              cout <<"\nCase #"<<i<<":"<<g;
              else
              cout <<"\nCase #"<<i<<": impossible";
          
             }
      }
      
    }
}
      
        
    
 
  
    