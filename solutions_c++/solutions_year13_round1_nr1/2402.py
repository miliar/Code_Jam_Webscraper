#include <iostream>
#include <math.h>

using namespace std;

int main () {
    int T;
    cin >> T;
    int counter=0;
    while (counter++ < T)
    {
        long long radius;
        signed long long paint;
        cin >> radius >> paint;
        
        long long rings=0;
        long long sum=0; 
        while (paint >= sum)
        {
             double calculation = ((radius+1) * (radius+1)  ) - (radius * radius ) ;
        //    calculation = floor(calculation+0.8);
//                cout << "calculation is " << calculation << endl;
             sum += calculation;
 //              cout << "paint is " << paint << endl;

             radius=radius+2;
             if (paint >= sum)
                rings++;
              
        }
                
        cout << "Case #" << counter<<": "<< rings << endl;
        
    }

return 0;
}

