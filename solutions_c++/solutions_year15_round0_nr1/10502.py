/*////////////////////////////////////
	   Harsh  Rumalwala
	   ---- hr1212 ----
////////////////////////////////////*/

#include <list>
#include <deque>
#include <stack>
#include <bitset>
#include <functional>
#include <utility>
#include <sstream>
#include <iomanip>
#include <ctime>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <numeric>
#include <valarray>
#include <complex>
#include <string.h>
#include <climits>

using namespace std;

const int dr[]={0,-1,0,1,-1,1, 1,-1};
const int dc[]={1,0,-1,0, 1,1,-1,-1};

typedef long long ll;
typedef long long unsigned ull;
typedef long double ld;
typedef unsigned short us;
typedef unsigned int uint;
typedef unsigned char uchar;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef pair<int,pii> piii;
typedef map<int,int> mi;
typedef map<string,int> msi;

#define ss(a) scanf("%s",a)
#define si(a) scanf("%d",&a)
#define sii(a,b) scanf("%d %d",&a,&b)
#define siii(a,b,c) scanf("%d %d %d",&a,&b,&c)
#define sll(a) scanf("%lld",&a);
#define pi(a) printf("%d\n",a);
#define pll(a) printf("%lld\n",a);
#define sz(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define f(a,b) for(int i=a;i<b;i++)
#define rf(a,b) for(int i=a;i>=b;i--)
#define l(a) (int)a.length()
#define maximum(a) (*max_element(all(a)))
#define minimum(a) (*min_element(all(a)))
#define clr(x,a) memset(x,a,sizeof(x))
//#define getchar getchar_unlocked
//#define putchar putchar_unlocked

uint inp() {
  uint n;
  int c;
  while( (c = getchar()) < '0') {
    ;
  }
  n = c - '0';
  while( (c = getchar()) >= '0')
    n = n * 10 + (c - '0');
  return n;
}

void pt(uint n) {
  uchar stack[30];
  int top = 0;
  if(n == 0) {
    putchar('0');
  } else {
    while(n > 0) {
      stack[top++] = n % 10 + '0';
      n /= 10;
    }
    while(top > 0) {
      putchar(stack[--top]);
    }
  }
  putchar('\n');
}

int a[1000000],b[1000000];
char s1[1000000],s2[1000000];

int main(){
	int i,j,k,m,n,t;
    t=inp();
    ll ans,x;
    for(k=1;k<=t;k++){
        m=inp();
        f(0,m+1){
            scanf("%c",&s1[i]);
        }
        ans=0;
        n=s1[0]-'0';
        f(1,m+1){
            if(n>=i){
                n+=s1[i]-'0';
            }
            else{
                x=(i-n);
                n+=(s1[i]-'0')+x;
                ans+=x;
            }
        }
        printf("Case #%d: %lld\n",k,ans);
    }
	return 0;
}
