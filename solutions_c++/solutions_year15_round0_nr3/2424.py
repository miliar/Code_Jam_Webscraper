#include<iostream>
#include<fstream>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<ctime>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<utility>
#include<numeric>
#include<deque>
using namespace std;
#define LL long long

#define I (2)
#define J (3)
#define K (4)

const int tab_A[4][4]=
{{1,1,1,1},{1,-1,1,-1},{1,-1,-1,1},{1,1,-1,-1}};
const int tab_B[4][4]=
{{1,I,J,K},{I,1,K,J},{J,K,1,I},{K,J,I,1}};

struct num {
  int v, x;
  num(int _v=0,int _x=0):v(_v),x(_x){};
  void clear() {
    v = 1; x = 1;
  }
  num minus() {
    num tmp;
    tmp.v=-v;
    tmp.x=x;
    return tmp;
  }
};

vector<num> allnum;
num right_div[10][10];
num left_div[10][10];

bool operator < (num a, num b){
  if(a.v != b.v) return a.v < b.v;
  return a.x < b.x;
}

inline num operator * (num a, num b) {
  num ret;
  ret.v = a.v * b.v * tab_A[a.x-1][b.x-1];
  ret.x = tab_B[a.x-1][b.x-1];
  return ret;
}

map<num,int> ind;

int L;
LL X;

char S[10010];
num val[10100];
int rep[256];
num lt[10100],rt[10100];
num base, part[10];
int n;

int avail[8][8];

bool run() {
  scanf("%d %lld",&L,&X);
  scanf("%s",S+1);
  lt[0].v = 1;
  lt[0].x = 1;
  rt[L+1].v = 1;
  rt[L+1].x = 1;
 // cerr << "L = "<<L<<" X = "<<X<<endl;
  for(int i=1;i<=L;++i){
    val[i].v = 1;
    val[i].x = rep[S[i]];
  }
  for(int i=1;i<=L;++i){
    lt[i] = lt[i-1] * val[i];
   // cerr << "lt["<<i<<"] = ("<<lt[i].v<<","<<lt[i].x<<") val["<<i<<"] = ("<<val[i].v<<","<<val[i].x<<")"<<endl;
  }
  for(int i=L;i>=1;--i){
    rt[i] = val[i] * rt[i + 1];
  }
  //for(int i=1;i<=L;++i)
   // cerr << "rt["<<i<<"] = ("<<rt[i].v<<","<<rt[i].x<<")"<<endl;
  
  base = lt[L];
  part[0].v = 1;
  part[0].x = 1;
  n = 1;
  part[n] = base;
  
 // cerr << "base = ("<<base.v<<","<<base.x<<")"<<endl;
  
  while(base.v!=1||base.x!=1) {
    base = base * lt[L];
    part[++n]=base;
  }
  base = lt[L];
  
  //cerr << "n = "<<n<<endl;
  
  memset(avail,-1,sizeof(avail));
  for(int i=0;i<L;++i)
    avail[ind[lt[i]]][ind[rt[i+1]]]=i;
  
  // X = a * n + b
  num A,B,C;
  for(int rem = 0; rem <= 2 && rem <= X; ++ rem) {
    int b = (X - rem) % n;
    int a = (X - rem) / n;
   // cerr << "X = "<<X<<" rem = "<<rem<<" b = "<<b<<endl;
    
    for(int sl = 0; sl <= n; ++ sl) {
      for(int sr = 0; sr + sl <= n; ++ sr) {
        int sm = (b+n+n - sl - sr) % n;
        int ta = (sl+sr+sm)/n;
        if(ta>a) continue;
        if(rem == 0) {
          if(part[sl].v==1&&part[sl].x==I
            && part[sm].v==1&&part[sm].x==J
            && part[sr].v==1&&part[sr].x==K)
            return true;
          continue;
        }
        
        // rem >= 1
        for(int p = 0; p < L; ++ p) {
          num A;
          A = part[sl] * lt[p];
          if(A.v != 1 || A.x != I) continue;
          
          if(p==0 && rem == 2) continue;
          
          if(rem == 1) {
            // only split at one place
            if(p == 0) {
              num B;
              for(int q = 1; q < L; ++ q) {
                B = part[sm] * lt[q];
                if(B.v != 1 || B.x != J) continue;
                num C = rt[q+1] * part[sr];
                if(C.v == 1 && C.x == K) return true;
              }
            } else {
              // normal case
            //  cerr << "check p = "<<p<<" sl = "<<sl<<" sm = "<<sm<<" sr = "<<sr<<" ... ";
              num B;
              B = rt[p + 1] * part[sm];
              C = part[sr];
              if(B.v ==1 && B.x==J && C.v==1&&C.x==K)return true;
            //  cerr <<"fail"<<endl;
              // special case
              if(sm == 0){
                
              //  cerr << "check p = "<<p<<" ... ";
                
                num B, C;
                // B = [p + 1 ... x] = J
                // C = [x + 1 ... L] * part[sr] = K
                //     [1 ... x]   = [1 ... p] * J
                //     [x + 1 ..L] = K \ part[sr] 
                //     p < x < L
                int x = ind[lt[p] * num(1, J)];
                num xx=lt[p]*num(1,J);
                int y = ind[right_div[ind[num(1, K)]][ind[part[sr]]]];
                num yy = right_div[ind[num(1, K)]][ind[part[sr]]];
              //  cerr << "avail = "<<avail[x][y]<<endl;
                
              //  cerr << "  --> xx = ("<<xx.v<<","<<xx.x<<")"<<endl;
                //cerr << "  --> yy = ("<<yy.v<<","<<yy.x<<")"<<endl;
                
                if(avail[x][y] > p) return true;
              }
            }
          } else { // rem == 2
            num B, C;
            // B = rt[p + 1] * part[sm] * lt[x] = J
            // C = rt[x + 1] * part[sr] = K
            //     [1 ... x]   = left_div[J][rt[p+1] * part[sm]]
            //     [x + 1 ..L] = right_div[K][part[sr]]
            //     0 < x < L
            int x = ind[
              left_div[ind[num(1, J)]]
                      [ind[rt[p+1]*part[sm]]]
                      ];
            int y = ind[
              right_div[ind[num(1, K)]]
                       [ind[part[sr]]]
                       ];
            if(avail[x][y] > 0) return true;
          }
        }
      }
    }
  }
  return false;
}

int main() {
  freopen("C.in","r",stdin);
  freopen("C.out","w",stdout);
  
  rep['i']=I;
  rep['j']=J;
  rep['k']=K;
  allnum.clear();
  for(int i=1;i<=4;++i){
    num v;
    v.v = 1;
    v.x = i;
    ind[v]=allnum.size();
    allnum.push_back(v);
    v.v = -1;
    ind[v]=allnum.size();
    allnum.push_back(v);
  }

  for(int i=0;i<allnum.size();++i)
    for(int j=0;j<allnum.size();++j) {
      // a[i] * a[j] = c
      int c = ind[allnum[i]*allnum[j]];
      right_div[c][j] = allnum[i];
      left_div[c][i] = allnum[j];
    }
  
  int test;
  scanf("%d", &test);
  for(int no=1;no<=test;++no)
    cout << "Case #"<<no<<": "<<(run() ? "YES" : "NO")<<endl;
}
