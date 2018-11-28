#include <cstdio>
#include <cstring>
#include <string>
#include <cctype>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <queue>
#define For(i,N) for(int i=0; i<N; i++)
#define FOR(i,z,k) for(int i=z; z<k; i++)
#define pb push_back
#define mp make_pair

typedef long long ll;

using namespace std;

int A,N,T;
vector<int> V;

int main(){
  scanf("%d",&T);
  For(t,T){
    scanf("%d %d", &A, &N);
    V.clear();
    V.resize(N);
    For(i,N) scanf("%d", &V[i]);
    if(A == 1){printf("Case #%d: %d\n",t+1,N); continue;}
    sort(V.begin(), V.end());
    int mini = 100;
    int cena = 0;
    For(i,N){
      if(V[i] >= A){
	mini = min(mini, cena + N-i);
	while(A <= V[i]){cena++; A += A-1;}
      }
      A += V[i];
      //printf("%d %d\n",mini, cena);
    }
    mini = min(mini, cena);
    printf("Case #%d: %d\n",t+1,mini);
  }
  return 0;
}