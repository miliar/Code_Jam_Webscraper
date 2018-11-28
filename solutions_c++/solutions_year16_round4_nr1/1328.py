#include<bits/stdtr1c++.h>
using namespace std;
typedef long long LL;
typedef pair<char, char> pr;

struct node {
  int r, l, p;
  int x;
  node() {
    l = r = p = -1;
  }
  node(int p, int l, int r) :
      p(p), l(l), r(r) {
  }
};
vector<node> v;
int n;

void build() {
  v.push_back(node());
  int k = (1 << (n + 1)) - 1;
  //cout<<k<<endl;
  queue<int> q;
  q.push(0);
  k--;
  while (k) {
    int ind = q.front();q.pop();
    k -= 2;
    v[ind].l = v.size();
    q.push(v.size());
    v.push_back(node());
    v.back().p = ind;

    v[ind].r = v.size();
    q.push(v.size());
    v.push_back(node());
    v.back().p = ind;
  }
}

bool win(int ind, int w, vector<int> &x) {

  bool ret = 1;
  while (ind != -1) {
    //cout<<ind<<" "<<w<<endl;
    if (!x[w]){
      //cout<<ind<<"---------- "<<w<<endl;
      return 0;
    }
    if(v[ind].l == -1) {
      x[w]--;
      v[ind].x = w;
    }

    if (v[ind].p != -1) {
      int r = v[v[ind].p].r;
      if(r != ind)
        ret &= win(r, (w + 1) % 3, x);
    }
    ind = v[ind].l;
  }
  return ret;
}

vector<int> ans;
void winA(int ind) {
  if (v[ind].l == v[ind].r && v[ind].r == -1) {
    ans.push_back(v[ind].x);
    return;
  }
  winA(v[ind].l);
  winA(v[ind].r);
}
string ANS(int ind) {
  if (v[ind].l == v[ind].r && v[ind].r == -1) {
    string s = "RSP";
    string r="";
    r +=s[v[ind].x];
    return r;
  }
  string ret="";
  string a = ANS(v[ind].l);
  string b = ANS(v[ind].r);
  ret += min(a,b);
  ret += max(a,b);
  return ret;
}

void pre(int ind) {
  if (ind == -1) {
    return;
  }
  cout<<ind<<" ";
  pre(v[ind].l);
  pre(v[ind].r);
}
int main() {
#ifndef ONLINE_JUDGE
  freopen("2.in", "r", stdin);
  freopen("2.out","w",stdout);
#endif // ONLINE_JUDGE  ios::sync_with_stdio(false);  cin.tie(NULL);  cout.tie(NULL);  int T;
  cin >> T;
  vector<int> arr;
  arr.resize(3);
  for (int ic = 1; ic <= T; ic++) {
    v.clear();
    ans.clear();
    cin >> n >> arr[0] >> arr[2] >> arr[1];
    build();
    //pre(0);
    int F =0;

    cout << "Case #" << ic << ": ";
    vector<string> A;
    for (int i = 0; i < 3; i++) {
      vector<int> x = arr;
      ans.clear();
      if (win(0, i, x)) {
        A.push_back(ANS(0));
        F = 1;
      }
    }
    if(!F)
      cout << "IMPOSSIBLE" << endl;
    else {
      sort(A.begin(),A.end());
      cout<<A[0]<<endl;
    }
  }

  return 0;

}
