#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <string>
#include <queue>
#include <stack>
#include <deque>
#include <cstring>
#include <cstdlib>
#include <climits>

using namespace std;

#define FOR(I,A,B) for(int I= (A); I<(B); ++I)
#define REP(I,N) FOR(I,0,N)
#define S(N) scanf("%d", &N)
#define S_String(A) scanf("%s",A)
#define SL(N) scanf("%ld", &N)
#define SLL(N) scanf("%lld", &N)
#define PR(N) printf("%d\n",N)
#define PRL(N) printf("%ld\n",N)
#define PRLL(N) printf("%lld\n",N)
#define SPACE printf(" ")
#define NEW_LINE printf("\n")

typedef long long int LL;
typedef vector<int> VI;

int main()
{
  freopen("C-large-1.in", "r", stdin);
  freopen("out.txt","w", stdout);
  LL arr[]={1, 2, 3, 11, 22, 101, 111, 121, 202, 212, 1001, 1111, 2002, 10001, 10101, 10201, 11011, 11111, 11211, 20002, 20102, 100001, 101101, 110011, 111111, 200002, 1000001, 1001001, 1002001, 1010101, 1011101, 1012101, 1100011, 1101011, 1102011, 1110111, 1111111, 2000002, 2001002};
  int t,ans;
  LL a,b,tmp;
  S(t);
  FOR(k,1,t+1)
  {
    ans=0;
    SLL(a);
    SLL(b);
    REP(i,39)
    {
        tmp=arr[i]*arr[i];
        if(tmp>=a && tmp<=b)
        ans++;
    }
    cout<<"Case #"<<k<<": "<<ans<<endl;
  }

}
