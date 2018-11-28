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
int E,R,N;
int v[10005];
pii w[10005];
int e[10005];
int r[10005];
set<int> used,used2;
int bef,aft;
int pos;
ll sum;

bool comp(pii a, pii b){
 return a.first>b.first;
}

int main(){
 int i;
 scanf("%d",&T);
 for(t=1;t<=T;t++){
  scanf("%d%d%d",&E,&R,&N);
  for(i=0;i<N;i++){
   scanf("%d",v+i);
   w[i]=mp(v[i],i);
  }
  sort(w,w+N,comp);
  used.clear();
  used2.clear();
  for(i=0;i<N;i++){
   pos = E;
   if(used2.lower_bound(-w[i].Y)!=used2.end()){
    bef=*used2.lower_bound(-w[i].Y);
    pos = (int)min((ll)pos,r[-bef]+((ll)bef+w[i].Y)*(ll)R);
   }
   e[w[i].Y] = pos;
   if(used.lower_bound(w[i].Y)!=used.end()){
    aft=*used.lower_bound(w[i].Y);
    e[w[i].Y] = (int)min((ll)pos,(ll)max(0LL,pos+((ll)aft-w[i].Y)*(ll)R-e[aft]-r[aft]));
   }
//printf("krok %d, w(%d,%d), pos %d, e %d\n",i,w[i].X,w[i].Y,pos,e[w[i].Y]);
   r[w[i].Y] = pos-e[w[i].Y];
   used.insert(w[i].Y);
   used2.insert(-w[i].Y);
  }
  sum = 0;
  for(i=0;i<N;i++){
   sum += (ll)e[i]*(ll)v[i];
//printf("e a val: %d, %d\n",e[i],v[i]);
  }
  printf("Case #%d: %lld\n",t,sum);
 }

 return 0;
}
