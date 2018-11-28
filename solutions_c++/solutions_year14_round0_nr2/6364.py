#include<iostream>
#include<cstdio>
#include<fstream>
#include<iomanip>
using namespace std;

double c, f, x, a;
int panduan()
{
    double remain = (c/a) + (x/(a+f));
    if(x/a > remain)
        return 1;
    else
        return 0;
}
int main()
{
    ifstream fin("B-large.in");
    freopen("B-small-attempt0.out","w",stdout);
    int k;
    fin>>k;


    for(int js = 1; js <= k; js++)
    {
        a= 2.0;
        double tt = 0;
        fin>>c>>f>>x;
        while(panduan())
        {
            tt += c/a;
            a += f;
        }
        tt += x/a;

       printf("Case #%d: %.7lf\n",js,tt);

    }
    return 0;
}
