#include <stdio.h>
#include <iostream>
#include <vector>
#include <bitset>
#include <string.h>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <math.h>
#include <fstream>
using namespace std;
#define IN(a)          scanf("%d", &a)
#define IN2(a, b)    scanf("%d%d", &a, &b)
#define IN3(a,b, c) scanf("%d%d%d", &a, &b, &c)
#define ENDL              printf("\n")
#define FOR0(n)     for(unsigned int i=0; i<n; i++)
#define FOR1(n)     for(unsigned int i=1; i<=n; i++)
#define FOR(i,a, b)  for(unsigned int i=a; i<b; i++)
#define FORV(a)	  for(int i=0; i<(int)a.size(); i++)
#define FORT(t,a)	  for(t::itr it=a.begin(); it!=a.end(); ++it)
#define mxc(mx, c)	{if((mx)<(c)) {(mx)=(c);}}
#define mnc(mn, c)	{if((mn)>(c)) {(mn)=(c);}}
#define itr			        iterator
#define fi                  first
#define se                second
#define CLR(a)         memset(a, 0, sizeof a)
#define LINF     4611686018427387904LL
#define WHITE  0
#define BLACK  1
#define GRAY    2
#define COMMENT(args...) DEBUG(printf(args); ENDL;)
#define TT DEBUG(printf("\t\t");)
#define DEBUG(X)		X
typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
enum { INF = 1000000000, N = 1250 };
int n;
char s[N];
int main()
{
  ifstream fin("A-large.in");
  ofstream fout("A-large.out");
  int TC; fin>>TC; FOR1(TC)
  {
    fin>>n;
    fin>>s;
    int sol = 0;
    int sum = 0;
    for(int i = 0; i<=n; i++)
    {
      if(sum<i&&s[i]!='0') sol+=i-sum, sum=i;
      sum+=s[i]-'0';
    }
    fout<<"Case #"<<i<<": "<<sol<<endl;
  }
  return 0;
}












