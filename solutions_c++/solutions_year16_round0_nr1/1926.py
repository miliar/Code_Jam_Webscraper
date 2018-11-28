#include <bits/stdc++.h>
using namespace std;

#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define MODV 10


typedef long long ll;
typedef double dbl;
typedef vector<int> vi;
typedef pair<int, int> pi;

bool setnum(int i, bool *a, int &cnt){
  if(!a[i]){
    a[i]=true;
    cnt++;
    if(cnt==10)return true;
  }
  return false;
}

void doit() {
  int cnt=0;
  bool a[10];
  for(auto i=0;i<10;i++){ a[i]=false; }
  long long n,nn;
  scanf("%lld", &n);
  if(n==0){printf("INSOMNIA\n");return;}
  for(ll i=1;;i++){
    nn=n*i;
    while(nn){
      if(setnum(nn%MODV,a,cnt)){
        printf("%lld\n",n*i);
        return;
      }
      nn /= MODV;
    }
  }

}

int main() {
  int tc;
  scanf("%d",&tc);
  for(int i=1;i<=tc;i++){
    printf("Case #%d: ",i);
    doit();
  }
  return 0;
}
