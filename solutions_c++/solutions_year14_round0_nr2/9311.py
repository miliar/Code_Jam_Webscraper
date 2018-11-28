#include <iostream>
#include <stdio.h>
#include <iomanip>
using namespace std;

int main()
{
    int n;
    cin>>n;
    for (int kali=0; kali<n; kali++)
    {
        float C,F,X,timepassed=0.0,speed=2.0;
        cin>>C>>F>>X;
        while (X/(speed) > X/(F+speed)+(C/speed))
        {
            timepassed += C/speed;
            speed += F;
        }
        printf("Case #%d: %.7f \n", kali+1, (X/speed)+timepassed);
    }
}
