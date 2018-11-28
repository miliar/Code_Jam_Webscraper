// Author: Xujie Si
// Email: six@gatech.edu
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <utility>
using namespace std;

#define FOR(i,X) for(int i=0;i<(X);++i)
#define PB(X) push_back( (X) )

typedef long long LL;
typedef vector<int> VI;

priority_queue<int> maxQ; // largest on the top
priority_queue<int, VI, greater<int> > minQ; // smallest on the top

//auto cmp1 = [](int& a, int& b) -> bool {return a>b;};
//auto dbg = ostream_iterator<int>(cerr, ",");

string P(int);
string R(int);
string S(int);


string P(int n) 
{
  if(n == 0) return "P";
  string a = P(n-1);
  string b = R(n-1);

  if(a < b) {
    return a + b;
  }  
  return b + a;
}

string R(int n) 
{
  if(n == 0) return "R";
  string a = R(n-1);
  string b = S(n-1);
 if(a < b) {
    return a + b;
  }  
  return b + a;
}

string S(int n) 
{
  if(n == 0) return "S";
  string a = P(n-1);
  string b = S(n-1);

 if(a < b) {
    return a + b;
  }  
  return b + a;
}

VI count(string & ss)
{
  int r,p,s;
  r = p = s = 0;

  for(int i=0;i<ss.length();++i){
    if(ss[i] == 'R') ++r;
    else if(ss[i] == 'P') ++p;
    else if(ss[i] == 'S') ++s;
    else {
      fprintf(stderr, "unknown char: %c\n", ss[i]);
    }
  }

  VI res;
  res.PB( r );
  res.PB( p );
  res.PB( s );

  return res;
}


bool test(string& s, int R, int P, int S)
{
  VI res = count(s);

  return res[0] == R && res[1] == P && res[2] == S;
}

void solve(){
	// exact implementation appears here
  int n, r, p, s;

  cin >> n >> r >> p >> s;

  string ss = P(n);


  string ans = "ZZ";

  //cout << "P(n): " << ss <<endl;

  if( test(ss, r,p,s) ) {

    if(ss < ans)
      ans = ss;
    //cout << ss << endl;
    //return;
  }

  ss = R(n);
  if( test(ss,r ,p,s) ) {
    if(ss < ans)
      ans = ss;

    //cout << ss << endl;
    //return;
  }


  ss = S(n);
  if( test(ss, r,p,s) ) {

    if(ss < ans)
      ans = ss;

    //cout << ss << endl;
    //return;
  }

  if(ans [0] != 'Z') {
    cout << ans <<endl;
  }
  else
    puts("IMPOSSIBLE");
}

int main()
{
  int cs = 0, T;
  scanf("%d",&T);
  while(++cs <= T){
    printf("Case #%d: ", cs);
    solve();
  }
  return 0;
}
