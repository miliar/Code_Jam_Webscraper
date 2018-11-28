//  Created by Lyamani Moulay Abdellatif on 13/04/13.
//  Copyright (c) 2013 Lyamani Moulay Abdellatif. All rights reserved.
//

#include <iostream>
#include <iomanip>

using namespace std;

#define LINESZ 1024

double bestTime(double C, double F, double X, int nFermes, double sum, double* result ){
    
    double temp = 0;
    if(nFermes >= 1) sum += C/(2.0 + (nFermes-1)*F );
    
    temp = sum + X/(2.0 + nFermes*F);
    
    while ( temp < *result) {
        nFermes++ ;
        result = &temp;
        *result = bestTime( C, F, X, nFermes, sum, result);
    }
    return  *result;
}

int main(int argc, const char * argv[])
{
    freopen("output.out","w", stdout);
    FILE* in = freopen("input.in","r", stdin);
    int test,cases;
    double C, F, X;
    char str[LINESZ] ;
    
    cases=0;
    scanf("%d",&test);
    fgets (str, LINESZ, in) ;
    while (test){
        test--;
        cases++;
        scanf("%lf", &C) ;
        scanf("%lf", &F) ;
        scanf("%lf", &X) ;
        
        double xo = X/2.0;
        double ro =  bestTime(C, F, X, 1, 0.0, &xo);
        
        std::cout.precision(12);
        cout<<"Case #"<<cases<<": "<<  ro <<endl;
    }

    return 0;
}

