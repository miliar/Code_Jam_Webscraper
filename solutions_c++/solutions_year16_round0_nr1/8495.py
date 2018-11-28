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

bool ended(bool *arr) {
  for(int i=0; i<10; i++) {
    if(arr[i] == false)return false;
  }
  return true;
}

void dataset() {
  int n, num, cnt = 1;
  bool arr[11];
  map<int, bool> m;

  CLR(arr);

  cin >> n;
  num = n;
  while(1) {
    if(m[num] == true) {
      cout << "INSOMNIA";
      return;
    }
    m[num] = true;

    string s = toString(num);
    for(int i=0; i<s.size(); i++) {
      arr[s[i] - '0'] = true;
    }

    if(ended(arr)) break;

    num = n * (++cnt);
  }

  cout << num;
  return;
}

int main()
{
  ios_base::sync_with_stdio(false);
  int t;

  cin >> t;
  for(int p=1; p<=t; p++) {
    cout << "Case #" << p << ": ";
    dataset();
    cout << endl;
  }

  return 0;
}
