#include<cstdio>
#include<cmath>
#include<iostream>
#include<set>
#include<cstdlib>
#include<vector>
#include<algorithm>
#include<cstring>
#include<map>
#include<iterator>
#include<sstream>
#include<stack>
#include<queue>
#include<limits.h>
#define fi(a, b) for(int i=a; i<b; i++)
#define fj(a, b) for(int j=a; j<b; j++)
#define fk(a, b) for(int k=a; k<b; k++)
#define SZ(x) (int)x.size()
#define pp() pop_back()
#define pb(x) push_back(x)
#define mp make_pair
#define sf scanf
#define pf printf
#define ssf sscanf
#define rsrt(x) sort(x.rbegin(), x.rend())
#define srt(x) sort(x.begin(), x.end())
#define mem(name, value) memset(name, value, sizeof(name))
#define Max 1000
#define oo 1000000000
#define OO 4294967296
//#include<conio.h>
//#define WT getch()


using namespace std;

typedef pair<int, int>ii;
map<string, int>stin;
map<char, int>chin;
map<int, int>inin;
map<string, string>stst;
map<vector<string>, int>vsin;
typedef vector<int>vi;
typedef vector<string>vs;
typedef vector<char>vc;
typedef long long ll;
typedef unsigned long long ull;
typedef double db;
typedef char C;
typedef string S;
//int dx[4] = {+0,-1,+0,+1}, dy[4] = {-1,+0,+1,+0}; /*row and column moves*/
//int dx[8] = {-1,-1,-1,+0,+1,+1,+1,+0}, dy[8] = {-1,0,+1,+1,+1,0,-1,-1};/*8-direction*/
/**
knight moves:
dx[8] = {-1,-2,-2,-1,+1,+2,+2,+1};
dy[8] = {-2,-1,+1,+2,+2,+1,-1,-2};
*/

struct type
{
    type(){}
};

typedef vector<type> vt;
typedef vector<ii> vii;

void read(void)
{
    return ;
}


db c, F, Minimum;
db target;

db rec(double cookies, db rate,  db total)
{
//    pf("cookies = %lf rate = %lf total = %lf\n", cookies, rate, total); WT;
    if(total>Minimum) return OO;
    if(cookies==target)
    {
        Minimum = min(Minimum, total);
        return total;
    }
    db a, b;
    a = rec(target, rate, total+(target/rate));
    b = rec(0, rate+F, total+c/rate);
    return min(a, b);
}

int main()
{
    int test_cases, cases=1;
    sf("%d", &test_cases);
    while(test_cases--)
    {
        sf("%lf %lf %lf", &c, &F, &target);
        Minimum = OO;
        db ans = rec(0, 2, 0);
        pf("Case #%d: %.7lf\n", cases++, ans);
    }
    return 0;
}




















