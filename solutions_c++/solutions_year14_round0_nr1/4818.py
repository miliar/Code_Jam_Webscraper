#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<ctime>
#include<cmath>

#include<algorithm>
#include<bitset>
#include<complex>
#include<deque>
#include<iostream>
#include<map>
#include<numeric>
#include<queue>
#include<stack>
#include<string>
#include<set>
#include<vector>
using namespace std;

#define pb push_back
#define mp make_pair
#define x first
#define y second
#define sz(a) (int((a).size()))
#define all(a) (a).begin(), (a).end()

#define For(it,c) for(typeof(c) it = ((c).begin()); it != ((c).end()) ; ++it)

#define forn(i,n) for (int i=0; i<int(n); ++i)
#define fornd(i,n) for (int i=int(n)-1; i>=0; --i)
#define forab(i,a,b) for (int i=int(a); i<int(b); ++i)

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;

typedef complex<int> cI;
typedef complex<double> cD;

typedef pair<int,int> pI;
typedef pair<ll, ll> pL;



int main()
{
  int i,j;
  int ans, val;
  int T;

  int arr[30];
  vector< int > sav;

  cin >> T;
  for(int z=1; z<=T; z++){
    fill(arr, arr+20, 0);
    cin >> ans;
    for(i=1;i<=4;i++){
      for(j=0;j<4;j++){
        cin >> val;
        if(ans==i) arr[val] |= 1;
      }
    }
    cin >> ans;
    for(i=1;i<=4;i++){
      for(j=0;j<4;j++){
        cin >> val;
        if(ans==i) arr[val] |= 2;
      }
    }
    sav.clear();
    for(i=1;i<=16;i++)
      if(arr[i]==3)
        sav.pb(i);

    printf("Case #%d: ", z);
    if(sz(sav)==0)printf("Volunteer cheated!\n");
    else if(sz(sav)==1) printf("%d\n", sav[0]);
    else printf("Bad magician!\n");

  }
  return 0;
}
