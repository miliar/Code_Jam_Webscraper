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

int t,T;
int r;
int R,N,M,K;
int prod[10];
double probs[7][7][7][150];
int best[3];

double sum(int i, int j, int k){
 int l;
 double ans=1.0;
//printf("sum (%d,%d,%d)\n",i,j,k);
// for(l=0;l<K;l++) printf("   soucin %d: %lf\n",prod[l],probs[i][j][k][prod[l]]);
 for(l=0;l<K;l++) ans*=probs[i][j][k][prod[l]];
 return ans;
}

int main(){
 int i,j,k,l;
 scanf("%d",&T);
 for(t=1;t<=T;t++){
  scanf("%d%d%d%d",&R,&N,&M,&K);
  printf("Case #%d:\n",t);
  for(i=2;i<=M;i++) for(j=i;j<=M;j++) for(k=j;k<=M;k++) for(l=0;l<150;l++) probs[i][j][k][l]=0.0;
  for(i=2;i<=M;i++){
   for(j=i;j<=M;j++){
    for(k=j;k<=M;k++){
 probs[i][j][k][1]+=1.0/8.0;
//printf("nyni je (%d,%d,%d,1): %lf\n",i,j,k,probs[i][j][k][1]);
 probs[i][j][k][i]+=1.0/8.0;
 probs[i][j][k][j]+=1.0/8.0;
 probs[i][j][k][k]+=1.0/8.0;
 probs[i][j][k][i*j]+=1.0/8.0;
 probs[i][j][k][i*k]+=1.0/8.0;
 probs[i][j][k][j*k]+=1.0/8.0;
 probs[i][j][k][i*j*k]+=1.0/8.0;
    }
   }
  }
  for(r=0;r<R;r++){
   for(i=0;i<K;i++) scanf("%d",prod+i);
   best[0]=best[1]=best[2]=2;
   for(i=2;i<=M;i++){
    for(j=i;j<=M;j++){
     for(k=j;k<=M;k++){
//printf("(%d,%d,%d): %lf\n",i,j,k,sum(i,j,k));
      if(sum(i,j,k)>sum(best[0],best[1],best[2])){
       best[0]=i; best[1]=j; best[2]=k;
      }
     }
    }
   }
   printf("%d%d%d\n",best[0],best[1],best[2]);
  }
 }

 return 0;
}
