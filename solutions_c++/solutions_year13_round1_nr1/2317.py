#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <string>


using namespace std;

int main(int argc, char *argv[])
{
    freopen("A-small-attempt2.in", "r", stdin);
    freopen("A-small-attempt2.out", "w", stdout);
    
    int T;
    cin >> T;
    const int PI = 1;;
    
    for(int i = 0; i < T; i++)
    {
            long long r;
            long long t;
            
            cin >> r >> t;
            
            long long ra = r;
            long long pa = t;
            
            long long Area;
            long long bull = 0;
            while(true)
            {
                Area = (PI*((ra + 1)*(ra+1) )) - (PI*(ra*ra));
                
                if(pa - Area < 0)
                {
                      break;
                }
                else
                {
                    pa = pa - Area;
                    bull++;
                }
                ra = ra+2;
                       
            }
            cout <<"Case #"<<i+1 <<": " << bull << endl;
            
            
            
            
    }
    
    //system("PAUSE");
    return EXIT_SUCCESS;
}
