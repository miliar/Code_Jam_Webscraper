
//{{{
#define DEF
#ifdef DEF
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <functional>
#include <stack>
#include <vector>
#include <list>
#include <map>
#include <cctype>
#include <queue>
#include <cstring>
#include <cmath>
#include <set>
#include <deque>


//-----------------------------------------------------


using namespace std;
typedef unsigned int uint;
typedef long long int llint;
typedef unsigned long long int ullint;

typedef pair<int,int> Pii;
typedef pair<llint,llint> Pll;

#define mrepp(i,n,x)  for(int i = n-1; i >= x; i--)
#define mrep(i,n) mrepp(i,n,0)
#define repp(i,x,n)  for(int i = x; i < n; i++)
#define rep(i,n) repp(i,0,n)
#define pb        push_back
#define all(vec)  (vec).begin(),(vec).end()
#define each(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
//#define reach(i,c) for(__typeof((c).rbegin()) i=(c).rbegin();i!=(c).rend();i++)
#define fst         first
#define scd         second

#define sz(v)     ((llint)(v).size())
//#define bit(n)    (1ll<<(li)(n))
//#define mkP        make_pair

//-----------------------------------------------------
#endif
//}}}

/*
void newton(void)
{
        int count;
        double a,newa;
        count=0;
        for(;;) {
                count++;
                newa=a-f(a)/df(a);
                if(fabs(newa-a)<eps) break;
                a=newa;
                if(count==max) {
                        printf("収束しませんでした。\n");
                        exit(1);
                }
        }
        printf("解の値は %f\n収束するのに %d 回かかりました。\n",
            newa,count);
 
}
 
double f(double x)
{
        return 2*x*x+(2*r-3)*x;
}
 
double df(double x)
{
        return 4*x+2*r-3;
}

llint sq_his[1000];
llint sq(llint x){
	if(x!=0&&sq_his[x]==0)
		return sq_his[x] = x*x;
	else
		return sq_his[x];
}
*/

double sqEqP(double a,double b,double c){
	if( a == 0 ) return 0;
	
	return (-b+sqrt(b*b-4*a*c))/(2*a);
}

double r,t;
int main(){
	int T;cin >> T;
	rep(i,T){
		cin >> r >> t;
		printf("Case #%d: %d\n",i+1,(int)sqEqP(2.0,(2.0*r-1.0),-t));
	}
	return 0;
}
