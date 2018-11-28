#include <iostream>
#include <set>
using namespace std;

static int SIZE = 16;
static int LINE = 4;


double solve(double c, double f, double x,double lastTime,int n) {
    int i;
    double thisTime = 0;
    for (int i = 0 ; i < n ; i++) {
        thisTime += (double)c/((double)i*f+2);
    }
    thisTime += (double)x/(double)(n*f+2);
    if(thisTime > lastTime) return lastTime;
    else return solve(c,f,x,thisTime,n+1);
}

int main()
{
   int i,n;
   double c,f,x;
   cin >> n ;
   for (i = 0; i < n; i++ ) {
       cout << "Case #" << i+1 << ": ";
       cin >> c >> f >> x;
       printf("%.7f\n",solve(c,f,x,(double)x/2,1));
   }

   return 0;
}

