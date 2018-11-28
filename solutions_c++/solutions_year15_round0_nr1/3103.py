#ifdef ONLINE_JUDGE
#include <bits/stdc++.h>
#else
#include "header.h"
#endif

using namespace std;
typedef unsigned long long ll;
#define MOD 1000000007
#define X first
#define Y second

int main( int argc, char** argv ){
int T;cin >> T;
for(int nc=0;nc<T;nc++){
  int SMAX;cin >> SMAX;
  int A[SMAX+1];
  string s;
  cin >>s;
  int clapping=0;
  int count=0;
  for(int i=0;i<s.size();i++){
    int n=s[i]-'0';
    if(clapping<i)count+=i-clapping,clapping=i;
    clapping+=n;
  }
  cout << "Case #"<<nc+1<<": "<<count<<endl;
}

}
