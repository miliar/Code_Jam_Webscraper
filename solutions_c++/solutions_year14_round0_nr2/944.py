#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;

double Total(double C, double F, double X){
    double total = 0.0, current = 2.0;
    while( ( (X-C)/current - X/(current + F)) > 0.0) {
        total += C/current;
        current += F;
    }
    total += X/current;
    return total;
}

int main(int argc, const char * argv[])
{
    int T, count = 1;
    double C,F,X;
    cin>>T;

    while(T-- > 0){
        cin>>C>>F>>X;
        printf("Case #%d: %.7f\n", count++, Total(C,F,X));
    }
}