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

int arr[1010], inv[1010];

int main()
{
  int T;
  int N;
  int head, tail;
  int p;
  int ans;

  cin >> T;
  for(int z=1;z<=T;z++){
    cin >> N;
    for(int i=0;i<N;i++){
      cin >> arr[i];
    }
    ans = 0;
    head = 0;
    tail = N;
    for(int i=0;i<N;i++){
      p = -1;
      for(int j=head;j<tail;j++){
        if(p==-1 || arr[j] < arr[p]) p = j;
      }
      if(p==-1) break;
      if(p - head <= tail - p - 1){
        for(int j=p;j-1>=head;j--){
          ans++;
          swap(arr[j], arr[j-1]);
        }
        head++;
      }else{
        for(int j=p;j+1<tail;j++){
          ans++;
          swap(arr[j], arr[j+1]);
        }
        tail--;
      }
    }

    printf("Case #%d: %d\n", z, ans);
  }
  return 0;
}
