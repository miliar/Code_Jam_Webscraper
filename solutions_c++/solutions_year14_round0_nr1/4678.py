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

int ina[6][6], inb[6][6];

int main() {


	freopen("A_input.in", "r", stdin);
	freopen("A_out.txt", "w", stdout);
	
	int T;
	scanf("%d", &T);
	FOR(t,0,T) {
        
        int ra, rb, val[20];
        
        scanf("%d", &ra);ra--;
        FOR(i,0,4)FOR(j,0,4)scanf("%d", &ina[i][j]);
        
        scanf("%d", &rb);rb--;
        FOR(i,0,4)FOR(j,0,4)scanf("%d", &inb[i][j]);
        
        VI res;
        FOR(i,0,4) {
            int va = ina[ra][i];
            FOR(j,0,4) {
                int vb = inb[rb][j];
                if(va == vb)res.PB(va);
            }
        }
        
        printf("Case #%d: ", t+1);
        if(res.S == 1)printf("%d", res[0]);
        else if(res.S == 0)printf("Volunteer cheated!");
        else printf("Bad magician!");
        printf("\n");
	}

	return 0;
}

