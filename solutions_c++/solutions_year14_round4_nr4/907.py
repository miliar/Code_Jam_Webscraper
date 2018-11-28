#include <iostream>
#include <string>
#include <set>
using namespace std;

string s[10];
int a[10];

int answer;
int cnt;
int m, n;

void calc_answer() {
  int aa = 0;
  set<string> ss[10];
  for (int mi=0;mi<m;mi++) {
    int sl = s[mi].size();
    for (int si=0;si<sl;si++) {
      ss[a[mi]].insert(s[mi].substr(0, si+1));
    }
  }
  for (int ni=0;ni<n;ni++) {
    if (ss[ni].size() > 0)
      aa += ss[ni].size() + 1;
  }
  if (aa > answer) {
    answer = aa;
    cnt = 1;
  } else if (aa == answer)
    cnt++;
}

void alloc(int i) {
  for (int ni=0;ni<n;ni++) {
    a[i] = ni;
    if (i == m-1) {
      calc_answer();
    } else {
      alloc(i+1);
    }
  }
}

int main() {
  int t;
  cin>>t;
  for (int ti=0;ti<t;ti++) {
    answer = 0;
    cnt = 0;
    cin>>m>>n;
    for (int mi=0;mi<m;mi++)
      cin>>s[mi];
    alloc(0);
    cout<<"Case #"<<ti+1<<": "<<answer<<" "<<cnt<<endl;
  }
  return 0;
}
