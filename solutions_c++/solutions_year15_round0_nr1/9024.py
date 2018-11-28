#include <iostream>
#include <string.h>
#include <string>
#include <fstream>
#include <vector>
#include <iomanip>
#include <queue>
#include <set>
#include <stack>
#include <math.h>
#include <stdlib.h>
#include <algorithm>
#include <cstdio>
#include <cassert>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;
typedef pair <double, double> pdd;

const double eps=1E-9;
const double Exp=2.718281828459045;
const double Pi=3.1415926535897932;

#define f first
#define s second
#define linf 2000000000000000000LL
#define FILL(a,b) memset(a, b, sizeof(a))
#define pb push_back
#define mp make_pair
#define sc(mas) scanf("%d",&mas)
#define scll(mas) scanf("%I64d",&mas)
#define sc2(f1,f2) scanf("%d%d",&f1,&f2)
#define sc3(f1,f2,f3) scanf("%d%d%d",&f1,&f2,&f3)
#define fore(op,po) for (int op=0;op<po;++op)
#define fori(p) for (int i=0;i<p;++i)
#define forj(p) for (int j=0;j<p;++j)
#define rep(a,b) for (int i=a;i<=b;++i)
#define srep(i,f) for (int i=1;i<=n;++i)
#define bit(mask,i) ((mask>>i)&1)
#define pri(ff) printf("%d\n",ff)
#define pr2(f1,f2) printf("%d %d\n",f1,f2)
#define prll(fl) printf("%I64d\n",fl)
#define prid(f1) printf("%.15lf\n",f1);
#define prn printf("NO\n")
#define pry printf("YES\n")

const int Max_Bit=63;
const int INF=2000000000;
const ll LINF=1000000000000000007ll;
const int MOD=1000000007;
const int NMAX=100005;
const int MMAX=3005;

int gcd(int a,int b){return b?gcd(b,a%b):a;}

int main() {
    int T;
    ifstream a("A-large.in");
    ofstream b("output.txt");
    a >> T;
    fori(T) {
       int n,k=0,ans=0;
       string s;
       a >> n;
       a >> s;
       forj(n+1) {
          if (k<j) {k++; ans++;}
          k+=(int)s[j]-'0';
       }
       b << "Case #" << i+1 << ": " << ans << endl;
    }
    b.close();
    return 0;
}
