#include <iostream>
#include <cstdio>
#include<string>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <sstream>
#include <vector>
#include <sstream>

using namespace std;
int main()
{   stringstream card;
    double C,F,X;
    double T,r;
	freopen("B-large.in","rt",stdin);
	freopen("B-large-op.out","wt",stdout);
    int N;
    scanf("%d",&N);
    for (int cas = 1; cas <= N; ++cas) {
        T=0.0;r=2;
        scanf("%Lf%Lf%Lf",&C,&F,&X);
        char comp='n';
        while(comp=='n')
        {
            if( ((C/r)+(X/(r+F))) < (X/r) )
            {
                T=T+double(C/r);
                r+=F;
            }
            else
            {T=T+double(X/r);
            comp='y';
            }


        }
        printf("Case #%d: %0.10g\n", cas, T);

    }
    return 0;

}
