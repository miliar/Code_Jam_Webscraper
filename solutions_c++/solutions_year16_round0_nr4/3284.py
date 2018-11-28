#include <iostream>
#include <cmath>
using namespace std;
double x[100] , a , b ,c , dd, g, h,j,u;
double f(double x)
{
    return (1/x - cos(x));
}
int main()
{
    /*x[0] = 4;
    x[1] = 6;
    for(int i = 1 ; i < 11  ;i++)
    {
        x[i + 1] = ((x[i - 1] * f(x[i])) -  x[i] * f(x[i - 1])) / (f(x[i]) - f(x[i- 1]));
        printf("%d : %.6lf\n" ,i, x[i]);
    }*/
    
    
    double a,r;
    while (true) {
        cin>>a;
        r=4.91718592528713-a;
        cout<< r <<" &&&&&&& "  << log(r)<<endl;
    }
 }