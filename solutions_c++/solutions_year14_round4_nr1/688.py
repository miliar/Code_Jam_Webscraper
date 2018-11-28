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

int T,N,X;
int S[10005];
int files;

int main(){
  scanf("%d",&T);
  FOR(t,1,T){
    files=0;
    scanf("%d%d",&N,&X);
    REP(i,N){
      scanf("%d",S+i);
    }
    sort(S,S+N);
    int j=0;
    FORD(i,N-1,0){
      if(i<j) break;
      if(S[i]+S[j]<=X){
        j++;
      }
      files++;
    }
    printf("Case #%d: %d\n",t,files);
  }


  return 0;
}
