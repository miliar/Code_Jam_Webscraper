#include<bits/stdc++.h>
#define ft first
#define sd second
#define pb push_back
using namespace std;

typedef long long ll;

const int N = 1100000;

int how_many(int n){
  vector<int> digits(10);
  int ile = 0;
  for(int i = 1; i <= 100; i++){
    int k = n * i;
    while(k){
      int r = k % 10;
      if(digits[r] == 0){
	digits[r] = 1;
	ile++;
	if(ile == 10) return i;
      }
      k /= 10;
    }
  }
}

int main(){
  ios_base::sync_with_stdio(0);
  int t;
  cin>>t;
  for(int tt = 1; tt <= t; tt++){
    int n;
    cin>>n;
    if(n == 0){
      cout<<"Case #" << tt <<": INSOMNIA\n";
      continue;
    }
    cout << "Case #"<< tt << ": " << how_many(n) * n << "\n";
  }
}