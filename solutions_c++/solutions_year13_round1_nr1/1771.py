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
#define PI           	acos(-1)
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


int tu(int val) {return (1 << val);}
bool iset(int mask, int id) {if((mask & tu(id) ) != 0)return true;return false;}
void doset(int &mask, int id) {mask |= tu(id);}
void dounset(int &mask, int id) {mask = mask & (~tu(id));}

typedef long long 					bint;
template<typename T> string tos( T a ) 	{ stringstream ss; string ret; ss << a; ss >> ret; return ret;}

long double lagbe(long double ar) {
    
    long double res = ar / (long double)PI;
    return res;
}

long double area(long double r, long double d) {
    
    long double ar = 2. * r * d - (d * d);
    ar = ar * (long double)PI;
    return ar;
}

int main() {


	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A_small_out.txt", "w", stdout);
	
	int T;
	bint r;
	long double t;
	scanf("%d", &T);
	
	FOR(ts,0,T) {
            
       int res = 0;
       cin >> r >> t;
       
       bint vt = r + 1;
       while(true) {
           long double ns = area(vt, 1);
           long double lg = lagbe(ns);
           
           if(t >= lg) {
               
               //DEBUG(lg);
                t -= lg;
                res++;
           }
           else break;
           
           vt += 2;
       }
       
       printf("Case #%d: %d\n", ts+1, res);
    }

	return 0;
}

