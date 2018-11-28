#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

#define REP(i, n) FOR(i, 0, n)
#define BACK(i, n) ROF(i, 0, n)
#define FOR(i, a, b) for (ll i = (a); i < (b); i++)
#define ROF(i, a, b) for (ll i = (b); --i >= (a); )
#define REP1(i, n) FOR(i, 1, n+1)
typedef pair<int, int> pii;
typedef pair<string, int> psi;
#define fi first
#define se second


int ri()
{
  int x;
  scanf("%d", &x);
  return x;
}
double rd()
{
  double x;
  scanf("%lf", &x);
  return x;
}

ll rl()
{
  ll x;
  scanf("%lld", &x);
  return x;
}

string rs()
{
 	string x;
  cin >> x;
  return x;
}

int main(){
	ll cases = rl();
  bool array[10];
  ll count;
	REP1(cc , cases){
		ll k = ri();
    printf("Case #%lld: ",cc);
    if (k == 0){
      printf("INSOMNIA\n");
    }
    else{
      REP(i,10) array[i] = false;
      count = 1;
      ll z = k;
      while(1){
        ll y = z;
        while(y){
          array[y%10] = true;
          y /= 10;
        }
        // REP(i,10) cout << array[i]<<endl;
        if(array[0] && array[1] && array[2] && array[3] && array[4] && array[5] && array[6] && array[7] && array[8] && array[9])
          break;
        // cout<<endl;
        count++;
        z = count*k;
      }
      printf("%lld\n", z); 
    }
	}
}
