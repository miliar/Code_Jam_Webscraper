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
//#define B				begin()
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

string tob(bint par) {
    string ret = "";
    while(par > 0) {
        int vl = par % 2;
        ret += tos(vl);
        par /= 2;
    }
    reverse(ALL(ret));
    while(ret.S < 32)ret = "0" + ret;
    return ret;
}

bint A, B, K, memo[35][2][2][2];
string va, vb, vc;
int L;

bint dp(int ind, int sa, int sb, int sc) {
    
    if(ind >= L) {
        if(sa && sb && sc)return 1;
        return 0;
    }
    //cout << ind << ", " << L << endl;
//    DEBUG(ind);DEBUG(sa);DEBUG(sb);DEBUG(sc);
//    cout << endl;
    
    bint &ret = memo[ind][sa][sb][sc];
    if(-1LL != ret)return ret;
    ret = 0LL;
    
    int la, lb; la = lb = 1;
    if(sa || va[ind]=='1')la = 2;
    if(sb || vb[ind]=='1')lb = 2;    
    
    FOR(i,0,la)FOR(j,0,lb) {
        int v = i & j;
        if(v == 1) {
            if(sc || vc[ind] == '1'){}
            else continue;
        }
        int fa, fb, fc;
        fa = sa | (i == 0 && va[ind] == '1');
        fb = sb | (j == 0 && vb[ind] == '1');
        fc = sc | (v == 0 && vc[ind] == '1');
        
        bint ra = dp(ind + 1, fa, fb, fc);
        ret += ra;
    }
    return ret;
}

int main() {


	freopen("B-large.in", "r", stdin);
	freopen("B_large_out.txt", "w", stdout);
	
	int T;
	cin >> T;
	
	FOR(t,0,T) {
        
        clr(memo, -1);        
        bint res = 0;
        
        cin >> A >> B >> K;
        
        va = tob(A);
        vb = tob(B);
        vc = tob(K);
        L = va.S;     
        
        res = dp(0, 0, 0, 0);
        
        cout << "Case #"<< t + 1<<": "<<res<<"" << endl;
	}

	return 0;
}

