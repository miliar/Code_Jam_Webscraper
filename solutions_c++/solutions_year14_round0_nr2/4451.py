#include<iostream>
#include <iomanip>
#include<vector>
#include<set>
#include<map>

using namespace std;


int main()
{
    int T;
    cin >> T;
   
    for(int n =0; n<T; ++n)
    {
       double C,F,X;
       cin >> C;
       cin >> F;
       cin >> X;
       
       double rate = 2;
       double tottime =0;
       
       
       while(1)
       {
           double time = C/rate;
           double timeleftnew = X/(rate+F);
           double timeleftcur = (X-C);
           if(timeleftcur < 0)
           {
              break;
           }
           timeleftcur = timeleftcur/rate;
           
           if(timeleftnew <= timeleftcur)
           {
              rate = rate+F;
              tottime += time;
           }
           else
           {
               break;
           } 
       }
       tottime += X/rate;
       cout.precision(7);
       cout.setf(ios::fixed, ios::floatfield ); 
       cout << "Case #" <<n+1<<": "<< tottime <<"\n"; 
    }
    
}
