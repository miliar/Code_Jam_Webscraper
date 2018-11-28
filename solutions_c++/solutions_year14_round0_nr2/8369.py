



#include <iostream>
#include <iomanip>


using namespace std;

int main ()
{
    cout << std::setprecision(7) << std::fixed;
    
    int T;
    
    cin >> T;
    
    for(int i = 1; i <= T; i++)
    {
        double rate = 2.0;
        double time = 0.0;
        
        double c, f, x;
        
        cin >> c >> f >> x;
        
        
        while(1)
        {
            if((x/rate) < ((c/rate) + ( x/(rate + f) )) )
            {
                time += ( x/ rate);
                break;
            }
            else
            {
                time += (c/rate);
                rate += f;
            }
            
        }
        
        
        cout << "Case #" << i << ": " << time << "\n";
    }
    
    return 0;
}


