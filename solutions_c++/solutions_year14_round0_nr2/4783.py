#include <stdio.h>
#include <algorithm>
#include <cstring>
#include <stdlib.h>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <functional>
#include <numeric>
#include <utility>
#include <deque>
#include <stack>
#include <bitset>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <queue>
#include <limits>
#include <fstream>
#include <list>
#include <sstream>
#include <iostream>
#include <iomanip>

using namespace std;

double solve(double C , double F , double X , double P ){
    double future = C/P + X/(P + F);
    double mini = 1LL<<60;
    if( future < X/P ){
        mini = min( X/P , C/P + solve( C , F , X , P + F ) );
    }else
        mini = X/P;
    return mini;
}

int main(){
    int t, q , i,  j;
    //freopen( "input.txt", "r", stdin );
	//freopen( "output.txt", "w", stdout );
    scanf("%d" , &t );
    double C , F , X , ans;
    for( q = 1 ; q <= t && scanf("%lf %lf %lf" , &C , &F , &X ) ; ++q ){
        printf("Case #%d: %.7lf\n" , q , solve( C , F , X , 2.0 ) );
    }
    return 0;
}
