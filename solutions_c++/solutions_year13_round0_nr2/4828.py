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

int in[200][200], R, C, row[200], col[200];


int main() {


	freopen("B-large.in", "r", stdin);
	freopen("B_large_out.out", "w", stdout);
	
	int T;
	scanf("%d", &T);
	
	FOR(t,0,T) {
        
        clr(row, 0);
        clr(col, 0);
        
        scanf("%d %d", &R, &C);
        FOR(r,0,R)FOR(c,0,C) {
            scanf("%d", &in[r][c]);
        }
        
        FOR(r,0,R) {
            
            int boro = 0;
            FOR(c,0,C)boro = max(boro, in[r][c]);
            row[r] = boro;
        }
        
        FOR(c,0,C) {
            
            int boro = 0;
            FOR(r,0,R)boro = max(boro, in[r][c]);
            col[c] = boro;
        }
        
        int ok = 1;
        FOR(r,0,R)FOR(c,0,C) {
            
            if(in[r][c] >= row[r] || in[r][c] >= col[c]) {}
            else ok = 0;
        }
        
        printf("Case #%d: ", t+1);
        if(ok)printf("YES");
        else printf("NO");
        printf("\n");
	}

	return 0;
}

