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


int tu(int val) {return (1 << val);}
bool iset(int mask, int id) {if((mask & tu(id) ) != 0)return true;return false;}
void doset(int &mask, int id) {mask |= tu(id);}
void dounset(int &mask, int id) {mask = mask & (~tu(id));}

typedef long long 					bint;
template<typename T> string tos( T a ) 	{ stringstream ss; string ret; ss << a; ss >> ret; return ret;}

int joor[10009], val[10009], cap, N, T;

int bs(int l, int h, int v) {
    
    while(true) {
        if(h - l < 5) {
            for(int i = h ; i >= l; i--) {
                if(val[i] <= v)return i;
            }
            break;
        }
        int m = (l + h) / 2;
        if(val[m] > v)h = m;
        else l = m;
    }
    return -1;
}

int main() {


	freopen("A-large.in", "r", stdin);
	freopen("A_large_out.txt", "w", stdout);
	
	cin >> T;
	
	FOR(t,0,T) {
        
        cin >> N >> cap;
        clr(joor, -1);
        FOR(i,0,N) {
            cin >> val[i];
        }
        sort(val, val + N);
        
        int l, h; h = N-1;
        FOR(i,0,N) {
            int left = cap - val[i];
            l = i + 1;
            if(l > h)break;
            h = bs(l, h, left);
            if(h >= 0) {
                joor[i] = 1;
                h--;
            }
        }
        
        int res = 0;
        FOR(i,0,N) {
            if(joor[i] < 0)res++;
        }
        
        printf("Case #%d: %d\n", t+1, res);
	}

	return 0;
}

