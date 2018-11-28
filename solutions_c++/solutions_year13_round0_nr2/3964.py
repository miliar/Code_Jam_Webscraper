#include <iostream>
#include <sstream>
#include <cstdio>
#include <string>
#include <cstring>
#include <complex>
#include <cstdlib>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
using namespace std;

#define INF (1<<29)
#define eps 1e-9

#define ll long long
#define ld long double
#define ull unsigned long long

#define mp make_pair
#define pb push_back

#define Clear(t) memset((t), 0, sizeof(t))
#define Clear2(t, v) memset((t), (v), sizeof(t))

#define For(i,a,b) for(int i = (int)(a), _t = (int)(b); i <= _t; i++)
#define Ford(i,a,b) for(int i = (int)(a), _t = (int)(b); i >= _t; i--)

#define SZ(t) ( (int)((t).size()) )
#define All(v) (v).begin(), (v).end()
#define Sort(v) sort(All(v))
#define present(c,x) ((c).find(x) != (c).end())

#define MAX 100

int n, m;
int a[MAX][MAX];

bool solve(){
   For(i, 0, n-1)   For(j, 0, m-1){
      int maxL = 0;
      For(k, 0, j-1) maxL = max(maxL, a[i][k]);
      
      int maxR = 0;
      For(k, j+1, m-1)  maxR = max(maxR, a[i][k]);
      
      int maxU = 0;
      For(k, 0, i-1) maxU = max(maxU, a[k][j]);
      
      int maxD = 0;
      For(k, i+1, n-1)  maxD = max(maxD, a[k][j]);
      
      if((maxL >a[i][j] || maxR > a[i][j]) && (maxU > a[i][j] || maxD > a[i][j])) return false;
   }
   return true;
}

int main(){
   //freopen("input.txt", "rt", stdin);
	//freopen("B-small-attempt0.in", "rt", stdin); 
	freopen("B-large.in", "rt", stdin);     
   freopen ("output.txt","w",stdout);
	
	int sotest;   cin >> sotest;
	For(run, 1, sotest){   cout << "Case #" << run << ": ";
	  cin >> n >> m;
	  
	  Clear(a);
	  For(i, 0, n-1)   For(j, 0, m-1)   cin >> a[i][j];
	  	     
     if(solve())  cout << "YES" << endl;
     else         cout << "NO" << endl;    
   }
	
	return 0;
}


