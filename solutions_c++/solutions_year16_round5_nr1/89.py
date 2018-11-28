#include <bits/stdc++.h>
using namespace std;
#define null NULL
#define mp make_pair
#define pb(a) push_back(a)
#define sz(a) ((int)(a).size())
#define all(a) a.begin() , a.end()
#define fi first
#define se second
#define relaxMin(a , b) (a) = min((a),(b))
#define relaxMax(a , b) (a) = max((a),(b))
#define SQR(a) ((a)*(a))
#define PI 3.14159265358979323846
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef long long ll;

const int MAX = 200010;
const int oo = 1E9;

char buf[MAX];

int CASE = 0;
void Doit(){
  ++CASE;
  cerr << "Case: " << CASE << endl;
  scanf("%s", buf);
  int n = strlen(buf);

  vector<char> left;
  for(int i = 0;i < n;++i){
    left.pb(buf[i]);
    while(sz(left) > 1 &&
          left.back() == left[sz(left) - 2]){
      left.pop_back();
      left.pop_back();
    }
  }

  int bad = sz(left) / 2;
  int good = n / 2 - bad;

  printf("Case #%d: %d\n", CASE, good * 10 + bad * 5);
}

int main(){
  int q;
  scanf("%d", &q);
  while(q-- > 0) Doit();
  return 0;
}
