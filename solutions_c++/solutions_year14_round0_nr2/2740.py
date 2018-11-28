#include <iostream>
#include <stdio.h>
#include <string.h>
#include <fstream>
int card[17];
using namespace std;

int main()
{
    int t;
    double c,f,x,ans,rate;
    fstream fs;
    FILE* fso;
    fs.open("C:\\B-large.in");
    fso = fopen("C:\\A-small-attempt0.out","w");
    fs >> t;
    //cin >> t;
    for(int count = 1; count <= t ; count++)
    {
       fs >> c >> f >> x;
        //cin >> c >> f >> x;
        ans = 0.0;
        rate = 2.0;
        while(ans + c/rate + x/(rate+f) < ans + x/(rate) )
        {
            ans += c/rate;
            rate += f;
        }
        ans += x/rate;
        fprintf(fso,"Case #%d: %.7lf\n",count,ans);
        //printf("Case #%d: %.7lf\n",count,ans);
    }
    return 0;
}
