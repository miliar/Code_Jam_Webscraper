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

int CASE = 0;

int N, R, P, S;
string STR[20][300];

void Doit(){
  ++CASE;
  scanf("%d%d%d%d", &N, &R, &P, &S);
  cerr << "Case: " << CASE << endl;

  string ans = "";

  string c1 = STR[N]['R'];
  string c2 = STR[N]['P'];
  string c3 = STR[N]['S'];

  vector<string> use;

  if(count(all(c1), 'R') == R &&
     count(all(c1), 'P') == P &&
     count(all(c1), 'S') == S) use.pb(c1);

  if(count(all(c2), 'R') == R &&
     count(all(c2), 'P') == P &&
     count(all(c2), 'S') == S) use.pb(c2);

  if(count(all(c3), 'R') == R &&
     count(all(c3), 'P') == P &&
     count(all(c3), 'S') == S) use.pb(c3);

  sort(all(use));

  if(use.empty()) printf("Case #%d: IMPOSSIBLE\n", CASE);
  else printf("Case #%d: %s\n", CASE, use[0].c_str());
}

int main(){
  vector<char> use({'R', 'P', 'S'});
  STR[0]['R'] = "R";
  STR[0]['P'] = "P";
  STR[0]['S'] = "S";

  for(int i = 1;i <= 14;++i)
    for(char r : use){
      char a, b;
      if(r == 'R') a = 'R', b = 'S';
      if(r == 'P') a = 'P', b = 'R';
      if(r == 'S') a = 'S', b = 'P';

      string c1 = STR[i - 1][a] + STR[i - 1][b];
      string c2 = STR[i - 1][b] + STR[i - 1][a];

      STR[i][r] = min(c1, c2);
    }

  int Q;
  scanf("%d", &Q);
  while(Q-- > 0) Doit();

  return 0;
}
