#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int zc;
    cin>>zc;
    for(int tc=1;tc<=zc;tc++)
    {
        double C, F, X, timeToWin;
        cin>>C>>F>>X;
        double numFarms, i=0;
        //numFarms = round(((F*X/C)-2)/F)-1;
    numFarms = ceil(X/C - (F+2)/F);
    if(numFarms<0)
    {
        timeToWin = X/2;
            cout<<"Case #"<<tc<<": "<<fixed<<timeToWin<<endl;
        continue;
    }
        timeToWin = X/(2+numFarms*F);
    while(i<numFarms)
    {
        timeToWin += (double)C/(2+F*i);
        i++;
    }
    cout.precision(7);
        cout<<"Case #"<<tc<<": "<<fixed<<timeToWin<<endl;
    }
}
