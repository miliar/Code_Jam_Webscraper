#include <vector>
#include <utility>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <stack>
#include <queue>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <list>
#include <bitset>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> vI;
typedef vector<string> vS;
typedef pair<int, int> pI;
typedef map<int, int> mI;
typedef map<string, int> mSI;
typedef set<int> sI;
typedef set<pI> spI;
typedef priority_queue<int> qmax;
typedef priority_queue<int, vector<int>, greater<int> >qmin;
typedef map<int, int>::iterator mI_it;
typedef set<int>::iterator sI_it;

#define TWO(k)  (1<<(k))
#define LTWO(k) (((LL)(1)<<(k)))
#define MIN(a,b) ( (a)<(b)?(a):(b) )
#define MAX(a,b) ( (a)>(b)?(a):(b) )
#define LS(x) 	 ((x)<<1)
#define RS(x) 	 (((x)<<1)+1)
#define MP make_pair
#define PB push_back
#define F first
#define S second
#define B begin()
#define E end()
#define F0(i, n) for( int (i) = 0; (i) < (n); (i)++)
#define F1(i, n) for( int (i) = 1; (i) <= (n); (i)++)
#define zero(i) memset((i),0,sizeof((i)))

const double PI = acos(-1.0);
const double EPS = 1e-9;
const int ioo = (~0)-(1<<31);
const LL loo = (~(LL)0)-((LL)1<<63);

int main()
{
    freopen("out.txt","w",stdout);
    freopen("B-large.in","r",stdin);
    int t, test = 0;
    cin>>t; 
    while(t--)
    {
        double C, f, x;
        cin>>C>>f>>x;
        double a, b, c;
        a = x;
        b = x*f-C;
        c = C*f+x*C;
//        double x1 = (-b+sqrt(b*b+4*c*a))/(2*a);
        double ans = 0,  f1 = 2;
        while(1){
            double s1 = ans + x/f1;
            double s2 = ans + C/f1 + x/(f1+f);
            if(s2 - s1 > EPS){
                ans = s1;
                break;
            }
            else{
                ans += C/f1;
                f1 += f;
            }
        }
        cout<<"Case #"<<++test<<": ";
        printf("%.8f\n", ans);
    }
    return(0);
}

