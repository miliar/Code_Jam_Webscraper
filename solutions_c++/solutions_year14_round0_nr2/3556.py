#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    
    int T;
    cout  << setprecision(7) << fixed;
    
    cin >> T;
    
    for(int i = 1; i <= T; i++)
    {
            cout << "Case #" << i << ": ";
            
            long double C, F, X;
            
            cin >> C >> F >> X;
            
            long double deadline = X/2;
            long double checkpoint = C/2;
            long double n = 0;
            
            while(true)
            {
                long double newDeadline = checkpoint + X / (2 + (long double)(n+1)*F);
                if(newDeadline < deadline)
                {
                      n++;
                      deadline = newDeadline;         
                      checkpoint += C / (2 + (long double)n*F);               
                } else {
                    cout << deadline << endl;
                    break;
                }
            }
            
    }
    
    return 0;
}
