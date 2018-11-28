#include <iostream>
#include <string>
#include <fstream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <algorithm>
using namespace std;
bool cmp(double a,double b)
{
    return a > b;
}
int main()
{
    int t,n;
    double a1[1010],a2[1010];
    //ifstream f_in("C-large.in");
    ifstream f_in("D-large.in");
    ofstream f_out("D_answer.out");
    f_in >> t;
    for(int cas = 1; cas <= t; cas++)
    {
        f_in >> n;
        for(int i = 0; i < n; ++i)
            f_in >> a1[i];
        for(int i = 0; i < n; ++i)
            f_in >> a2[i];
        sort(a1,a1+n,cmp);
        sort(a2,a2+n,cmp);
        int len1 = 0, len2 = 0;
        int i = 0, j = 0;
        while(i < n && j < n)
        {
            if(a1[i] > a2[j])
                len1 += 1, i += 1, j += 1;
            else j += 1;
        }
        i = 0, j = 0;
        while(i < n && j < n)
        {
            if(a2[i] > a1[j])
                len2 += 1, i += 1, j += 1;
            else j += 1;
        }
        f_out <<"Case #"<<cas<<": "<<len1 <<" "<<n-len2<<endl;

    }
    return 0;
}
