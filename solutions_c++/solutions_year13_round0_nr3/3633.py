#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <cstring>
#include <string>
#include <math.h>
#include <sstream>
using namespace std;

string doubleToStr(double n){
    ostringstream strs;
    strs << n;
    return strs.str();
}

bool is_fair(double n){
    string num= doubleToStr(n);
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
    int cases;
    double cnt,num1,num2;
    scanf("%i\n",&cases);
    for (int n=0;n<cases;n++){
        cnt = 0;
        scanf("%lf %lf\n",&num1,&num2);
        for (double i=num1;i<=num2;i++)
            if (is_fair(i) && is_fair(sqrt(i)))
                cnt++;
        printf("Case #%i: %g\n",(n+1),cnt);
    }


    return 0;
}
