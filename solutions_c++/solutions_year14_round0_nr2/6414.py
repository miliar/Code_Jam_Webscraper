#include <iostream>
#include <stdio.h>
#include <string>
#include <map>
using namespace std;

int main()
{
    int T;
    int i,j,k;
    double C,F,X;
    double ti = 0;
    double win = 2.0;
    double timeToNextFarm = 0;
    double timeToX = 0;
    double timeToXAfterFarm = 0;

    cin >> T;
    for (i=0;i<T;i++)
    {
        cin >> C;
        cin >> F;
        cin >> X;
        
        ti = 0;
        win = 2;
        
        while (1)
        {
              timeToNextFarm = C/win;
              timeToX = X/win;
              timeToXAfterFarm = X/(win+F)+timeToNextFarm;
              if (timeToXAfterFarm>timeToX)
              {
                 ti += timeToX;
                 break;
              }
              else
              {
                  win += F;
                  ti+=timeToNextFarm;
              }
        }
        
        printf("Case #%d: %.7lf\n",i+1,ti);
    }
}
