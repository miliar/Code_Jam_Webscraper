//hi~ :)
#include <bits/stdc++.h>
#define X first
#define Y second
#define PB push_back
#define MP make_pair
#define fastio ios::sync_with_stdio(false);cin.tie(0)
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<pii> vii;
typedef vector<pll> vll;
bool _cmp(const pair<int,int>&i, const pair<int,int>&j){
  return ((i.first == j.first) ? (i.second>j.second) : (i.first<j.first));
} //x increase, y decrease
struct Node{
  int x, y;
  Node(int a=0, int b=0):
    x(a), y(b){}
  bool operator < (const Node& a)const{
    return ((x==a.x) ? (y>a.y) : (x<a.x));
  }//x increase, y decrease
};

#define max(x,y) ((x)>=(y) ? (x):(y))
const int mxn = 1e0 + 1;
double eps = 1e-9;
ll ncase = 1;
int N,M,a,b,c, ans;
string str;
vector<bool> arr;

void pre(){
  return;
}
void init(){
  ans = 0;
  arr.clear();
  cin >> str >> N;
}
void sol(){
  for(auto i : str){
    if(i == '-') arr.PB(1); // need to be flip
    else arr.PB(0);
  }
  for(int i=0;i+N <= arr.size();i++){
    if(arr[i]){
      ++ans;
      for(int j=0;j<N;j++) arr[i+j] = !arr[i+j];
    }
  }
  for(int i=max(0,arr.size()-N+1);i<arr.size();i++)
    if(arr[i]){
      ans = -1;
      return;
    }
}

int main(){
  pre();
  cin >> ncase;
  for(int I=1;I<=ncase;I++){
    init();
    sol();
    cout << "Case #" << I << ": " ;
    if(ans == -1) cout << "IMPOSSIBLE" << endl;
    else cout << ans << endl;
  }
}
