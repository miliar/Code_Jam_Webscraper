#include <cstdio>
#include <vector>

using namespace std;

int T, N, K;
vector<vector<int> > M; //bitmask, last;
vector<int> L;		//kluce na zac
vector<vector<int> > C;	//kluce v chestoch
vector<int> O;		//kluce na otvorenie

bool b=0;
int vys=-1;

void rek(int m, int l){
  if(b) return;
  if(m == (1<<N)-1){
    b=1;
    vys = l;
    return;
  }
  for(int i=0; i<N; i++) if(!(1<<i & m) && L[O[i]] > 0 && M[m|1<<i][i] == -1){
    L[O[i]]--;
    for(int j=0; j<C[i].size(); j++) L[C[i][j]]++;
    
    M[m|1<<i][i] = l;
    rek(m|1<<i,i);
    
    L[O[i]]++;
    for(int j=0; j<C[i].size(); j++) L[C[i][j]]--;
  }
}

int main(){
  scanf("%d",&T);
  for(int t=0; t<T; t++){
    scanf("%d %d",&K, &N);
    M.clear(); L.clear(); C.clear(); O.clear();
    M.resize(1<<N, vector<int> (N,-1));
    L.resize(201,0); C.resize(N); O.resize(N);
    for(int i=0; i<K; i++){ int a; scanf("%d", &a); L[a]++; }
    for(int i=0; i<N; i++){
      int a,b; scanf("%d %d",&a, &b);
      O[i] = a;
      for(int j=0; j<b; j++){int c; scanf("%d",&c); C[i].push_back(c);}
    }
    b=0;
    vys = -1;
    rek(0,0);
    // zrekonstruujeme cesty
    if(vys == -1){ printf("Case #%d: IMPOSSIBLE\n",t+1); continue;}
    vector<int> F(N);
    int curm = (1<<N)-1, curl = vys, nl;
    for(int i=0; i<N; i++){
      F[N-i-1] = curl+1;
      nl = M[curm][curl];
      curm = curm ^ 1<<curl;
      curl = nl;
    }
    printf("Case #%d:",t+1);
    for(int i=0; i<N; i++) printf(" %d",F[i]);
    printf("\n");
  }
  return 0;
}