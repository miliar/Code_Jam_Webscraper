//-------------include
#include<cstdio>
#include<string>
#include<iostream>
#include<cstring>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<algorithm>
#include<cmath>
#include<cstdlib>
#include<climits>
#include<vector>
#include<list>
#include<deque>
#include<functional>
#include<sstream>

//-------------define
#define ALL(a)  (a).begin(),(a).end()
#define PB push_back
#define MP make_pair
#define SORT(c) sort((c).begin(),(c).end())
#define DUMP(x)  cerr << #x << " = " << (x) << endl;
#define CLR(a) memset((a), 0 ,sizeof(a))
#define rep(i,n) for(int i=0;i<(int)n;i++)
#define fi first
#define se second

//-------------namespace
using namespace std;

//-------------inline
inline int toInt(string s) {int v; istringstream istr(s);istr>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}

//-------------typedef
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int, int> pii;

//-------------var
int dx[]={0,-1,0,1,1,1,-1,-1};
int dy[]={1,0,-1,0,1,-1,1,-1};

bool ended(string s, int n) {
  for(int i=0; i<n; i++) {
    if(s[i] == '-') return false;
  }
  return true;
}

string reverse(string s, int end) {
  for(int i=0; i<=(end-1)/2; i++) {
    if(s[i] == '-')s[i] = '+';
    else s[i] = '-';

    if(s[end-i] == '-')s[end-i] = '+';
    else s[end-i] = '-';

    char tmp = s[i];
    s[i] = s[end-i];
    s[end-i] = tmp;
  }
  if(end%2 == 0){
    if(s[end/2] == '-') s[end/2] = '+';
    else s[end/2] = '-';
  }

  return s;
}

void dataset() {
  string s;
  cin >> s;

  int n = s.size(), end, cnt = 0;
  while(!ended(s, n)) {
    for(int i=0; i<n; i++) {
      if(s[i] == '-') end = i;
    }

    int top = -1;
    if(s[top+1] == '+') {
      while(s[top+1] == '+')top++;
      s = reverse(s, top);
    }

    s = reverse(s, end);
    if(top<0)cnt++;
    else cnt+=2;
  }

  cout << cnt;
}

int main()
{
  ios_base::sync_with_stdio(false);

  int t;
  cin >> t;
  for(int i=1; i<=t; i++) {
    cout << "Case #" << i << ": ";
    dataset();
    cout << endl;
  }

  return 0;
}
