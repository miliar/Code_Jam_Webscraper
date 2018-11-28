#include <iostream>
#include <conio.h>
#include <iomanip>

using namespace std;

void Solve(int k)
{
     double C,F,X;
     cin >> C >> F >> X;
     double time=0, speed=2;
     for (;;)
     {
         double a,b1,b2;
         a=X/speed;
         b1=C/speed;
         b2=X/(speed+F);
         if (a<(b1+b2))
         {
            time+=a;
            break;
         }
         speed+=F;
         time+=b1;
     }
     cout.flags(std::ios::fixed);
     cout << "Case #" << k+1 << ": " << std::setprecision(7) << time << endl;
}
         
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("OUTPUT.txt", "w", stdout);
    int T;
    cin >> T;
    for (int i=0; i<T; i++)
        Solve(i);
    return 0;
}
