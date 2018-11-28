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
    int s = 0;
    cin >> n;
    priority_queue<pair<int,char>> q;
    rep(j,n){
      int x;
      cin >> x;
      q.push(pair<int,char>(x, 'A'+j));
      s += x;
    }
    printf(" Case #%d: ", i);
    if(s % 2){
      int c = q.top().X;
      char x = q.top().Y;q.pop();
      printf("%c ", x);
      if(c-1>0)
        q.push(pair<int,char>(c-1, x));
    }
      
    while(!q.empty()){
      int c = q.top().X;
      char x = q.top().Y;q.pop();
      printf("%c", x);
      if(c-1>0)
        q.push(pair<int,char>(c-1, x));
      c = q.top().X;
      x = q.top().Y;q.pop();
      printf("%c ", x);
      if(c-1>0)
        q.push(pair<int,char>(c-1, x));
    }
    puts("");
  }
  return 0;
}
