using namespace std;

#include <iostream>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <climits>
#include <iomanip>
#include <iterator>
#include <sstream>
#include <fstream>
#include <cassert>

// CONSTANTS
#define INF (1<<31)-1
#define PI 3.14159265358979323846264338327950288419716939937510

// FUNCTIONS
#define MAX(x,y) (x)>(y)?(x):(y)
#define MIN(x,y) (x)<(y)?(x):(y)
// gcd(a,b){ return (b==0)?a:gcd(b,a%b); }
// lcm(a,b){ return a*b/gcd(a,b); }

typedef long long LL;
typedef long double LD;
typedef long long unsigned int LLU;

int main()
{
    freopen("in1.txt","r",stdin);
    freopen("out1.txt","w",stdout);
    int t=0;
    double c=0.0,f=0.0,x=0.0;
    double result = 0.0;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        cin >> c >> f >> x;
        double f1 = 2.0,f2=0.0;
        double total1 = x/f1,total2=0.0,prev1=0.0;
        while(1)
        {
                f2 = f1 + f;
                total2 = x/f2;
                if(total1 < ((c/f1)+total2))
                {
                    result = (total1)+ prev1;
                    break;
                }
                else{
                    total1 = total2;
                    prev1 = ((c/f1)+ prev1);
                    f1=f2;
                }
        }
        printf("Case #%d: %.7f\n",i+1,result);
    }
    return 0;
}
