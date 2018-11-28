#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;
int n;
vector<double> A,B;

bool f(int x) {
  int j=-1;
  for (int i=n-x;i<n;i++) {
    j++;
    if (A[i]<B[j]) { return false; }
  }
  return true;
}
void solve(int test) {
  cin>>n;
  A=*new vector<double>(n); B=*new vector<double>(n); 
  for (int i=0;i<n;i++) { cin>>A[i]; }
  for (int i=0;i<n;i++) { cin>>B[i]; }
  sort(A.begin(),A.end());
  sort(B.begin(),B.end());
  //for (int i=0;i<n;i++) {cout<<A[i]<<" ";} cout<<endl;
  //for (int i=0;i<n;i++) {cout<<B[i]<<" ";} cout<<endl;
  int l=0,r=n;
  while (l<r) {
    int mid=(l+r+1)/2;
    if (f(mid)) {
      l=mid;
    } else { r=mid-1; }
  }
  int x=l;  
  
  int y=n;
  int j=0; queue<double> Bq; for (int i=0;i<n;i++) Bq.push(B[i]);
  for (int i=0;i<n;i++) {
    while ((A[i]>=Bq.front()) and (Bq.size()>0)) {
      Bq.pop();
    }
    if (Bq.size()>0) {y--; Bq.pop();}
  }
  cout<<"Case #"<<test<<": "<<x<<" "<<y<<endl;
}
  
int main() {
  ios::sync_with_stdio(false);
  int t; cin>>t;
  for (int i=1;i<=t;i++) { solve(i); }
}
