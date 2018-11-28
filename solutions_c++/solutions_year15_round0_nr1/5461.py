/*
Prashant Gupta(GHOST_YO)
IIITA
*/
/*
start of libraries to be included in the program
*/
#include <cmath>
#include <algorithm>
#include <vector>
#include <iostream>
#include <cstdio>
#include <set>
#include <queue>
#include <map>
#include <string>
#include <cstring>
#include <ctime>
#include <stack>
#include <sstream>
#include<fstream>
#include <limits.h>
/*
end of libraries to be included in the program
*/
using namespace std;
/*
start of MACRO definition
*/
#define For(i,a,b) for(i=a;i<=b;i++)
#define Ford(i,a,b) for(i=a;i>=b;i--)
#define Rep(i,c) for((i=c.begin());i!=c.end();i++)
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define sr(x) (int)x.size()
#define modul 1000000007
#define nmax 500100
#define BUG(x) {cout << #x << " = " << x << endl;}
#define PR(x,a,b) {For(i,a,b) cout << x[i] << ' '; cout << endl;}
#define fillchar(x,a,b,delta) For(_,a,b) x[_]=delta;
#define FILL(a) memset(a,0,sizeof(a));
#define sc(a) scanf("%d", &a)
#define scl(a) scanf("%lld", &a)
#define scc(a) scanf("%c", &a)
#define scs(a) scanf("%s", a)
#define Bit(s,i) ((s&(1<<i))>0)
#define Two(x) (1<<x)
#define pii pair<int,int>
#define ll long long
#define e 1e-6
#define PI acos(-1)
#define piii pair < pii ,int >
#define make(a,b,c) mp(mp(a,b),c)
#define gc getchar
#define pc putchar
/*
end of MACRO definition
*/

inline void scanint(int &x)
{
    register int c = 0;
    x = 0;
    int flag = 0;
    for (; ((c != 45) && (c < 48 || c > 57)); c = gc());
    for (; ((c == 45) || (c > 47 && c < 58)); c = gc()) {
        if (c == 45)
            flag = 1;

        else
            x = (x<<1) + (x<<3) + c - 48;
    }

    if (flag)
        x = -x;
}

inline void writeint (int n)
{
    int N = n, rev, count = 0;
    rev = N;
    if (N == 0) { pc('0'); pc('\n'); return ;}
    while ((rev % 10) == 0) { count++; rev /= 10;} //obtain the count of the number of 0s
    rev = 0;
    while (N != 0) { rev = (rev<<3) + (rev<<1) + N % 10; N /= 10;}  //store reverse of N in rev
    while (rev != 0) { pc(rev % 10 + '0'); rev /= 10;}
    while (count--) pc('0');
}

int main()
{
    int t,n,m,i,j,k,l,ans,count,temp,sum,flag;
    string s;
    ifstream fi;
    ofstream fo;

    fi.open("A-large.in");
    fo.open("out.txt");
    fi >> t;
    j = 1;
    while(t--) {
        fi >> n;

        fi >> s;
        ans = 0;
        int cur = (int)s[0] - '0';
        //cout << cur << endl;
        For(i, 1, n) {
            if((i - cur) > 0) {
                ans += (i - cur);
                cur += (i - cur);
            }
            cur += ((int)s[i] - '0');
        }

        fo << "Case #" << j <<": " << ans << endl;
        j++;
    }
    return 0;
}
