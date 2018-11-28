#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <list>
#include <ctime>
#include <vector>
#include <fstream>
#include <algorithm>
#include <iomanip>
#define  epsilon 1e-7

using namespace std;

void test(int m, int n, int p)
{
    srand(time(0));
    ofstream out("out.txt");
    out << 100000 << endl;
    for(int i = 0; i < 100000; i++)
    {
        double a, b, c;
        a = 1 + rand()%m;
        b = 1 + rand()%n;
        c = 1 + rand()%p;
        int temp = 1 + rand()%5;
        out << fixed << setprecision(temp) << a << " " << b << " " << c << endl;
    }
}

int main()
{
   //test(10000, 100, 100000);
    //return 0;
    ofstream out("out.txt");
    int testcase;
    cin >> testcase;
    long double rez[testcase];
    for(int j = 0; j < testcase; j++)
    {
         double C, F, X;
        scanf("%lf %lf %lf", &C, &F, &X);//cin >> C >> F >> X;

        double k = 0.0;
        long double M = 0.0, N = 0.0;
        long double VAL_SUM = 0.0;

        double RR = C/(2.0 + k*F);
        M = (RR + X/( (2.0)+(k + 1)*F ));
        N = X/(2.0 + k*F);

        while(M < N)
        {
            RR = C/(2.0 + k*F);
            M = (RR + X/( (2.0)+(k + 1)*F ));
            N = X/(2.0 + k*F);
            if(M < N)
            VAL_SUM = VAL_SUM + RR;
            k++;
        }
        if(N > 0.0)
        rez[j] = N + VAL_SUM;
        else
        rez[j] = N + VAL_SUM;
    }
    for(int i = 0; i < testcase; i++)
        out << fixed << setprecision(7) << "Case #" << (i + 1) << ": " << rez[i] << endl;
}

