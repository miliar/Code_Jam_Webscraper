#include<cstdio>
#include<cstring>
#include<cmath>
#include<ctime>
#include<algorithm>
#include<map>
#include<set>
#include<vector>
using namespace std;

#define ll long long
#define ull unsigned long long
#define ld long double
#define pb push_back
#define popb pop_back

#define pii pair<int,int>
#define mp make_pair
#define X first
#define Y second

#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)

#define INF 1000000005

int T,N;
int A[2005];
int mini,indi;

int main(){
  scanf("%d",&T);
  FOR(t,1,T){
    scanf("%d",&N);
    REP(i,N){
      scanf("%d",A+i);
    }
    int l=0,r=N-1,help;
    int swaps=0;
    while(l<r){
      indi=l;mini=INF;
      FOR(i,l,r){
        if(A[i]<mini){
          mini=A[i];
          indi=i;
        }
      }
      if(indi-l<=r-indi){
        swaps+=indi-l;
        FORD(i,indi,l+1){
          help=A[i]; A[i]=A[i-1]; A[i-1]=help;
        }
        l++;
      }
      else{
        swaps+=r-indi;
        FOR(i,indi,r-1){
          help=A[i]; A[i]=A[i+1]; A[i+1]=help;
        }
        r--;
      }
    }
    printf("Case #%d: %d\n",t,swaps);
  }

  return 0;
}
