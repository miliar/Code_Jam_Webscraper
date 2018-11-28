#include <string>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <complex>
#include <list>
#include <functional>
#include <utility>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <iterator>
#include <iomanip>
using namespace std;

#define READ freopen("input.txt", "r", stdin)
#define WRITE freopen("output.txt", "w", stdout)
#define PI acos(-1)
#define E <<endl

typedef vector<int> vi;

template <class T> inline bool isPwr2(T x){return (x != 0) && ((x & (x - 1)) == 0);}
template <class T> inline double D2R(T x){return (PI*x)/180;}
vector<string> &split(const string &s, char delim, vector<string> &elems) { stringstream ss(s); string item; while (getline(ss, item, delim)){if (!item.empty()) elems.push_back(item);}return elems;}


int main()
{
    READ;
    WRITE;

    double ini_rate=2.00,C,F,X,f[2];
    int n,tc=1;

    cin>>n;

    while(n--)
    {
        cin>>C>>F>>X;
        int i=0;
        f[i]=X/ini_rate;

        i++;
        while(true)
        {
            f[i%2]=f[(i-1)%2] - X/(ini_rate+(i-1)*F) + C/(ini_rate+(i-1)*F) + X/(ini_rate+i*F) ;

            if(f[i%2]>f[(i-1)%2]) break;
            i++;

        }

        printf("Case #%d: %.7f\n",tc++,f[(i-1)%2]);


    }





    return 0;
}
