#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <string>
#include <cstring>

using namespace std;

#define FOR(i,a,b)   	for(int (i)=(a);(i)<(b);(i)++)
#define PB           	push_back
#define INF          	INT_MAX
#define DEBUG(___x)     cout<<#___x<<" = ["<<___x<<"]"<<endl
#define SORT(___a)      sort(___a.begin(),___a.end())
#define RSORT(___a)     sort(___a.rbegin(),___a.rend())
#define PI           	3.141592653589793238
#define MP           	make_pair
#define PII          	pair<int,int>
#define ALL(___v)       (___v).begin(), (___v).end()
#define VS           	vector<string>
#define VI           	vector<int>
#define S            	size()
#define B				begin()
#define E				end()
#define print(___v)     {cout<<"[";if(___v.S)cout<<___v[0];FOR(___i,1,___v.S)cout<<","<<___v[___i];cout<<"]\n";}
#define clr(___x, ___v)	memset(___x, ___v , sizeof ___x);
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)

#define EPS         (1e-8)

int tu(int val) {return (1 << val);}
bool iset(int mask, int id) {if((mask & tu(id) ) != 0)return true;return false;}
void doset(int &mask, int id) {mask |= tu(id);}
void dounset(int &mask, int id) {mask = mask & (~tu(id));}

typedef long long 					bint;
template<typename T> string tos( T a ) 	{ stringstream ss; string ret; ss << a; ss >> ret; return ret;}

double C, F;

inline double grem(double X, double pr) {
    return X / pr;
}

int main() {


	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B_out_small.txt", "w", stdout);
	
	int T;
	double X;
	scanf("%d", &T);
	FOR(t,0,T) {
        
        scanf("%lf %lf %lf", &C, &F, &X);
        
        double res = 0, pr = 2. , ta, tb;
        while(true) {
            ta = grem(X, pr);
            tb = (C / pr) + grem(X, pr + F);
            if(ta + EPS > tb) {
                res += (C / pr);
                pr += F;
            }
            else {
                res += ta;
                break;
            }            
        }
        
        printf("Case #%d: ", t+1);
        printf("%.8lf", res);
        printf("\n");
	}

	return 0;
}

