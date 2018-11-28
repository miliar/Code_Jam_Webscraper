#include<iostream>
#include<cstdio>
#include<algorithm>
#include<functional>
#include<vector>
#include<iterator>
using namespace std;

vector<double> a,b;

int win(const vector<double>& a, const vector<double>& b) {
  int n = a.size();
  int ahead = 0;
  int bhead = 0;
  int result = 0;
  while(bhead < n) {
    while(bhead < n && a[ahead] < b[bhead]) bhead++;
    if (bhead < n) {
      result++;
      ahead++;
      bhead++; 
    }
  }
  return result;
}

int main() {
  int T,t,n;
  double d;
  cin >> T;
  t = 0;
  while(t++<T) {
    cin >> n;
    a.resize(n);
    b.resize(n);
    copy_n(istream_iterator<double>(cin), n, a.begin());
    copy_n(istream_iterator<double>(cin), n, b.begin());
    sort(a.begin(), a.end(), greater<double>());
    sort(b.begin(), b.end(), greater<double>());
    printf("Case #%d: %d %d\n", t, win(a,b), n-win(b,a));
  }
  return 0;
}
