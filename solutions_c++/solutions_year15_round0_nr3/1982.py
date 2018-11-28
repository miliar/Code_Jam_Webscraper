#include<bits/stdc++.h>
using namespace std;

#define CLR(a,x) memset(a,x,sizeof(a))
#define PB push_back
#define INF 1000000000
#define MOD 1000000007
#define MP make_pair
#define tr(container , it) for(typeof(container.begin()) it=container.begin() ; it!=container.end() ; it++)
#define FOR(i,a,b) for(i=a;i<b;i++)
#define REP(i,a) FOR(i,0,a)
#define LL long long
#define VI vector < int >
#define PII pair < int , int >
int X,L;
int dp[12][10001][5][2*4];
string str;

bool is_valid(int str_used, int pos, int done, int cur_val) {
  return (pos == 0 && (str_used <= X && str_used%4 == X%4) && cur_val == 3 && done == 2);
}

int mul(int cur_val, char ch) {
  bool is_neg = (cur_val > 3);
  cur_val%=4;
  int other = (ch - 'i' + 1);
  int result;
  if (cur_val == 0) {
    result = other;
  } else if (other == cur_val) {
    result = 4;
  }
  else if (other == cur_val+1 || (other == 1 && cur_val == 3)) {
    result = (cur_val == 1 ? 3 : (cur_val+2)%3);
  } else {
    result = 4 + (other == 1 ? 3 : (other+2)%3);
  }
  if (is_neg) {
    if(result >= 4)
      result -= 4;
    else
      result += 4;
  }
  return result;
}

bool rec(int str_used, int pos, int done, int cur_val) {
  int &ret = dp[str_used][pos][done][cur_val];
  if(ret == -1) {
    ret = is_valid(str_used, pos, done, cur_val);
    if (str_used == 11) {
      return ret;
    }
    if ((cur_val == 1 && done == 0) || (cur_val == 2 && done == 1)) {
      ret |= rec(str_used, pos, done+1, 0);
    }
    if (pos == L) {
      ret |= rec(str_used+1, 0, done, cur_val);
    } else {
      ret |= rec(str_used, pos+1, done, mul(cur_val, str[pos]));
    }
  }
  return ret;
}

int main() {
  int T;
  cin>>T;
  int kase = 1;
  while(T--) {
    long long X1;
    cin>>L>>X1;
    X = (X1 >= 11 ? (X1%4 + 12): (X1));
    cin>>str;
    memset(dp, -1, sizeof(dp));
    if(rec(0, 0, 0, 0)) {
      cout<<"Case #"<<kase++<<": YES\n";
    } else {
      cout<<"Case #"<<kase++<<": NO\n";
    }
  }
  return 0;
}
