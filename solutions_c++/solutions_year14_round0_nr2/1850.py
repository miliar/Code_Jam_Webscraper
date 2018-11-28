#include <iostream>
#include <cmath>
#include <vector>
#include <cstdio>
using namespace std;
double calculate(double c,double f,double x,double time,double currentrate);
int main()
{
    freopen("in.txt","r+",stdin);
    freopen("out.txt","w+",stdout);
   int t;
   cin >> t;
   for (int c1(0);c1<t;c1++){
    double c,f,x;
    cin >> c >> f >>x;
    double previous;
    previous=(x/(2.00+f))+c/2.00;
    for (double n(1.00);previous+(c/(2.00+(n)*f))-(x/(2.00+(n)*f))+(x/(2.00+(n+1)*f))<=previous;n=n+1.00){
        previous=previous+(c/(2.00+n*f))+(x/(2.00+(n+1)*f))-(x/(2.00+(n)*f));


    }
cout << "Case #" << c1+1 << ": " ;
if (previous<x/2.00)printf("%.7f\n",previous); else printf("%.7f\n",x/2.00);


   }
    return 0;
}

