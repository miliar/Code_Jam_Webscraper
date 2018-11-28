#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <complex>
#pragma comment(linker, "/STACK:266777216")
using namespace std;

#define assert(f) { if(!(f)) { fprintf(stderr,"Assertion failed: "); fprintf(stderr,#f); fprintf(stderr,"\n"); exit(1); } }

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<double> VD;
typedef pair<double,double> PDD;

const int inf=1000000000;
const LL INF=LL(inf)*inf;
const double eps=1e-9;
const double PI=2*acos(0.0);
#define bit(n) (1<<(n))
#define bit64(n) ((LL(1))<<(n))
#define pb push_back
#define sz size()
#define mp make_pair
#define cl clear()
#define all(a) (a).begin(),(a).end()
#define fill(ar,val) memset((ar),(val),sizeof (ar))
#define MIN(a,b) {if((a)>(b)) (a)=(b);}
#define MAX(a,b) {if((a)<(b)) (a)=(b);}
#define sqr(x) ((x)*(x))
#define X first
#define Y second

clock_t start=clock();

// p1[x] is a min prime divisor of 1+x^8
int p1[11] = {0, 0, 257, 2, 65537, 2, 17, 2, 97, 2, 17};
// p2[x] is a min prime divisor of 1+x^16
int p2[11] = {0, 0, 65537, 2, 641, 2, 353, 2, 193, 2, 353};

int main()
{
	freopen("2.in","r",stdin);
	freopen("2.out","w",stdout);
	int TST,tst=0;
	for(scanf("%d",&TST);TST--;)
	{
		printf("Case #%d:\n",++tst);
		fprintf(stderr,"Case #%d:\n",tst);
    int n,k;
    scanf("%d%d",&n,&k);
    int m=n/2;
    for(int j=0;j<k;j++) {
      assert(j<bit(m-2));
      int a[111];
      for(int i=0;i<m-2;i++)
        a[i]=(j>>i)%2;
      printf("1");
      for(int i=0;i<m-2;i++) printf("%d",a[i]);
      printf("11");
      for(int i=0;i<m-2;i++) printf("%d",a[i]);
      printf("1");
      for(int x=2;x<=10;x++) printf(" %d",n==16?p1[x]:p2[x]);
      printf("\n");
    }
	}
	fprintf(stderr,"time=%.3lfsec\n",0.001*(clock()-start));
	return 0;
}
