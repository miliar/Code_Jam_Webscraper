#include<bits/stdc++.h>

using namespace std;
#define reps(i,j,k) for(int i = (j); i <= (k); ++i)
#define rep(i,j) reps(i,0,int(j)-1)
#define all(X) (X).begin(),(X).end()
#define rall(X) (X).rbegin(),(X).rend()
#define eb emplace_back
#define rrep(X,Y) for(int (X) = (Y)-1; (X) >=0; --(X))
#define X first
#define Y second
#define in(i,j,k) ((i)>=(j)&&(i)<=(k))
#define sz size()

typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;

int main(){
  int t, n;
  cin >> t;
  reps(i,1,t){
    bool flag;
    cin >> n;
    int k;
    int x[10] = {0};

    reps(j,1,1000){
      flag = false;
      k = n * j;

      while(!flag && k){
        flag = true;
        x[k%10] = 1;
        k/=10;
        rep(l,10) flag &= x[l]&1;
      }
      if(flag){k=n*j;break;}
    }
    printf("Case #%d: ", i);
    if(flag) printf("%d\n", k);
    else printf("INSOMNIA\n");
  }
  return 0;
}
