#include<cstdio>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<algorithm>
#include<string>
#include<utility>
#include<cstring>
using namespace std;

#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)

set<vector<int> > s;

vector<int> multi(vector<int> a){
  int i, j;
  vector<int> res(100, 0);

  rep(i,100) rep(j,100){
    if(i+j >= 100 && a[i]*a[j] > 0){ res[0]=-1; return res; }
    if(a[i]*a[j]>0) res[i+j] += a[i]*a[j];
  }

  rep(i,99) res[i+1] += res[i] / 10, res[i] %= 10;
  if(res[99] >= 10) res[0] = -1;
  return res;
}

void doit(vector<int> &a, int dig, int now, int rest){
  int i, j, k, op, mul;

  op = dig-1 - now;
  if(op < now){
    if(rest==9) return;
    vector<int> b = multi(a);
    if(b[0]!=-1){
      reverse(b.begin(), b.end());
      s.insert(b);
    }
    return;
  }

  mul = 2;
  if(op==now) mul = 1;
  rep(i,4) if(mul*i*i <= rest){
    if(now==0 && i==0) continue;
    a[now] += i;
    if(op!=now) a[op] += i;
    doit(a, dig, now+1, rest-mul*i*i);
    a[now] -= i;
    if(op!=now) a[op] -= i;
  }
}

vector<int> reader(void){
  int i, n;
  vector<int> res(100, 0);
  char buf[110];

  scanf("%s",buf);
  n = strlen(buf);

  rep(i,n) res[i] = buf[n-1-i] - '0';
  reverse(res.begin(), res.end());
  return res;
}

int main(){
  int T, count = 0;

  int i, j, k, res;
  vector<int> a, b;

  REP(i,1,51){
    vector<int> a(100, 0);
    doit(a, i, 0, 9);
  }

  vector<vector<int> > vs(s.begin(), s.end());
  vector<vector<int> >::iterator ia, ib;

  scanf("%d",&T);
  while(T--){
    a = reader();
    b = reader();

    ia = lower_bound(vs.begin(), vs.end(), a);
    ib = lower_bound(vs.begin(), vs.end(), b);
    res = distance(ia, ib) + s.count(b);

    printf("Case #%d: %d\n",++count, res);
  }

  return 0;
}
