#include <iostream>
#include <cstdio>
#include <set>
#include <algorithm>
#include <cassert>
#define MAXN 1005
using namespace std;

typedef long long int ll;

int testcase,M;
ll N,best,ans,O[MAXN],E[MAXN],P[MAXN];
bool cur=0,pre=1;
set <pair<ll,ll> > pq[2];
set <pair<ll,ll> >::iterator it;
struct event{
  event(){}
  event(ll _p, ll _cnt){p = _p, cnt = _cnt;}
  ll p,cnt;
}A[2*MAXN];

bool cmp(event a,event b){
  if(a.p != b.p) return a.p < b.p;
  return a.cnt > b.cnt;
}

ll val(ll s, ll x){
  return s * x - x * (x - 1ll) / 2ll;
}

int main(){
  freopen("A-small-attempt1.in","r",stdin);
  freopen("A.out","w",stdout);
  scanf("%d",&testcase);
  for(int TC=1;TC<=testcase;++TC){
//    printf("doing %d\n",TC);
    scanf("%lld%d",&N,&M);
    best = ans = 0;
    for(int i=0;i<M;++i){
      scanf("%lld%lld%lld",&O[i],&E[i],&P[i]);
      best += P[i] * val(N, E[i] - O[i]);
      A[2*i] = event(O[i],P[i]);
      A[2*i+1] = event(E[i],-P[i]);
    }
  //  printf("%lld %d\n",N,M);
 //   if(M > 50) continue;
    sort(A,A+2*M,cmp);
    pq[0].clear();
    pq[1].clear();

    for(int i=0;i<2*M;++i){   //CHANGE THIS LATER!!!
      cur = !cur;
      pre = !pre;
      pq[cur].clear();
      if(!i) pq[cur].insert(pair<ll,ll>(N,A[0].cnt));
      else{
        ll tot_size = 0, fin_size = 0, change = A[i].cnt;
        for(it=pq[pre].begin();it!=pq[pre].end();++it){
          pair<ll,ll> t1 = pair<ll,ll>(it->first - (A[i].p - A[i-1].p),it->second);
          while(pq[cur].find(t1) != pq[cur].end()){
            pq[cur].erase(t1);
            t1.second *= 2ll;
          }
          pq[cur].insert(t1);
          tot_size += it->second;
          ans += it->second * val(it->first, A[i].p - A[i-1].p);
        }
    //    printf("%d: size is %lld, A[%d] is %lld\n",i,tot_size,i,A[i].cnt);
      //  printf("done size = %d\n",pq[cur].size());
        if(A[i].cnt > 0){
          pair<ll,ll> t1 = pair<ll,ll>(N,A[i].cnt);
          while(pq[cur].find(t1) != pq[cur].end()){
            pq[cur].erase(t1);
            t1.second *= 2ll;
          }
          pq[cur].insert(t1);
        }
        else{
          A[i].cnt *= -1;
          while(A[i].cnt > 0){
         //   printf("hi %d\n",pq[cur].size());
            it = pq[cur].end();
            --it;
            pair<ll,ll> t1 = *it;
          //  if(i == 167) printf("remove %lld\n",t1.second);
            pq[cur].erase(t1);
            if(t1.second < A[i].cnt) A[i].cnt -= t1.second;
            else{
              t1.second -= A[i].cnt;
              if(t1.second > 0){
                while(pq[cur].find(t1) != pq[cur].end()){
                  pq[cur].erase(t1);
                  t1.second *= 2ll;
                }
                pq[cur].insert(t1);//, printf("add back %lld\n",t1.second);
              }
              break;
            }
          }
        }
        for(it=pq[cur].begin();it!=pq[cur].end();++it) fin_size += it->second;
      //  printf("Init %lld, Chn, %lld, Fin %lld\n",tot_size, change, fin_size);
    //    if(tot_size + change != fin_size) printf("FAIL!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n");
      }
    }
 //   exit(0);
   // printf("best = %lld, ans = %lld\n",best,ans);
    printf("Case #%d: %lld\n",TC,best - ans);
   // exit(0);
  }
  //system("pause");
}
