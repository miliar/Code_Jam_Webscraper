#include <iostream>
#include <cstdio>
#include <complex>
#include <set>
#include <map>
#include <utility>
#include <queue>
#include <algorithm>
#include <vector>
#include <stack>
#include <sstream>
#include <cmath>
#include <cstdlib>
#include <string>
#include <cstring>

using namespace std;

typedef unsigned long long ULL;
typedef long long LL;

#define DEBUG 0
#define INF 1000000000
#define MOD 1000000007
#define rep(i,s,e) for(int i=s;i<e;i++)
#define rrep(i,s,e) for(int i=s;i>=e;i--)
#define PII pair<int,int>
#define VI vector<int>
#define sf(i) scanf("%d",&i)
#define pf(i) printf("%d\n",i)
#define d(x) if(DEBUG) cerr << x << endl
#define d_arr(a,n) if(DEBUG){ rep(i,0,n) { cerr << *(a+i) << " "; } cerr << endl;}

int A[4][4],B[4][4],a,b,card,ccount;

int main()
{
  freopen("input.txt","r",stdin);
  freopen("output.txt","w+",stdout);
  int test,t;
  cin >> test;
  t = test;
  while(test--)
  {
  	ccount=0;
    cin >> a;
    a--;
    rep(i,0,4)
    	rep(j,0,4)
    		cin>>A[i][j];
    cin >> b;
    b--;
    rep(i,0,4)
    	rep(j,0,4)
    		cin>>B[i][j];
    rep(i,0,4)
    	rep(j,0,4)
    		if(A[a][i]==B[b][j])
    		{
    			ccount++;
    			card = A[a][i];
    		}
    printf("Case #%d: ",t-test);
    if(ccount==0)
    	cout << "Volunteer cheated!\n";
    else if(ccount==1)
    	cout << card << endl;
    else
    	cout << "Bad magician!\n";
  }
  return 0;
}