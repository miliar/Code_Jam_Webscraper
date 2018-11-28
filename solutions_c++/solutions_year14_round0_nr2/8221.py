#include <iostream>
#include <fstream>
using namespace std;

int main()
{
  
    std::ifstream cin("input.txt"); 
   

    int r;
    double F = 0;
    double C = 0;
    double X = 0;
    double ct = 0;
    double cr = 2;
    double cx =0;
    double t1;
    double t2;
 
    cin >> r ;

    for(int l = 0; l<r; l++)
        {
            cin >> C;
            cin >> F; 
            cin >> X; 
            cx = 0;
            ct = 0;
            cr = 2;

            while (cx < X)
            {
                t1 =  ct+(C/cr)+(X/(cr+F)) ;
                t2 =  ct + (X/cr);
               // printf (" t1 with buying is %f \n", t1);
               //printf (" t2 with out buying is %f \n", t2);
                if ( t1 < t2 )
                {
                    ct=ct+(C/cr);
                    cr = cr+F;
                }
                else{
                    ct = ct+X/cr;
                    cx = X;
                    printf ("Case #%d: %f \n", l, ct);
                    
                }
           }
       
   }
   
   return 0;
}