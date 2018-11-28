#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <cstring>
#include <string>
#include <math.h>
#include <sstream>
#include <algorithm>
#include <vector>
using namespace std;

int main(){

   int t,m,b,e=0,x;
    scanf("%d\n",&t);
    for (int i=0;i<t;i++){
        e=b=0;
        scanf("%d ",&m);
        //cout << "nxt case: " << m << endl;
        for (int j=0;j<=m;j++){
            scanf("%1d",&x);
            //cout << "got " << x << endl ;
            if (j>b) {
                e+= j-b;
                b+= j-b;
            }
            b+=x;
            //cout << "now buffer is " << b << " and extra is " << e << endl;
        }
        printf("Case #%d: %d\n",i+1, e);
    }
    return 0;
}
