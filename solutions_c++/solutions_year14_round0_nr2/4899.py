#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>

using namespace std;
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)

int main ()
{
    int test;
    READ("B-small-attempt0.in");
    WRITE("B-small-attempt0.out");

   scanf("%d", &test);
  //  cin >> test;

    int n = 1;
    while (test != 0 )
    {
        long double c,f,x;
        cin >> c >> f >> x;
        long double C=0;
        long double TT=0;
        long double time=0;
        long double m =2;

       if (x<=c)
            {
                TT= x/m;
                goto amira;
            }
       while (true){

            time =c/m;

            long double temp = x/m;
            long double tempTT = TT+temp;
            long double tempTime = TT+time + (x/(m+f));
//            cout << tempTT << " " << tempTime << endl;

            if (tempTime > tempTT ) {
                TT= tempTT;
            //    cout << "BOOOOOM \n" ;
                goto amira;

            }
                    TT+=time;
                    m+=f;

       }
        amira:
        cout << "Case #" << n << ": " <<  TT <<endl;
        cout.precision(9);
       // cout.setf( std::ios::fixed, std:: ios::floatfield );

    ++n;
    --test;
    }


//    file.close();


return 0;
}
