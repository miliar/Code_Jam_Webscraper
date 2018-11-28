#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
#include <cmath>
using namespace std;
typedef long long ll;
int main()
{
	FILE* fin=freopen("B-large.in","rt",stdin);
	FILE* fout=freopen("B-large.out","wt",stdout);
    int t;
    std::cin>>t;
    for(int zz=0;zz<t;zz++)
    {

        double c,f,x;
        scanf("%lf %lf %lf", &c,&f,&x);

        if (c  >= x)
        {
            printf("Case #%d: %0.7lf\n", zz+1, x / 2.0);
            continue;
        }

        double accuTime = 0;
        double preVec = 2.0;
        while(true)
        {
            double t1 = (x-c)/preVec;
            double t2 = x / (preVec + f);
            if (t1 < t2)
            {
                accuTime += (x/preVec);
                break;
            }
            else
            {
                accuTime += (c / preVec);
                preVec += f;
            }
        }

        printf("Case #%d: %0.7lf\n", zz+1, accuTime);

    }
    fclose(fout);
    fclose(fin);
    return 1;
}