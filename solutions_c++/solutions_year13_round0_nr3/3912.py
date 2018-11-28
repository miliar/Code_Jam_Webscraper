#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <cstring>
#include <string>
#include <math.h>
#include <sstream>
using namespace std;

string dts(double n){
    ostringstream strs;
    strs << n;
    return strs.str();
}

bool fairfair(double n){
    string num= dts(n);
    int p1=0;
    int p2=num.length()-1;
    while(1){
        if (p1>=p2) break;
        if (num[p1]!=num[p2]) return false;
        p1++;
        p2--;
    }
    return true;
}


int main(){
    int eachcase;
    double cnt,num1,num2;
    scanf("%i\n",&eachcase);
    for (int n=0;n<eachcase;n++){
        cnt = 0;
        scanf("%lf %lf\n",&num1,&num2);
        for (double i=num1;i<=num2;i++)
            if (fairfair(i) && fairfair(sqrt(i)))
                cnt++;
        printf("Case #%i: %g\n",(n+1),cnt);
    }


    return 0;
}
