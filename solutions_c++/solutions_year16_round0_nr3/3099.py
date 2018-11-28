#include <vector>
#include <string>
#include <iostream>
#include <set>
using namespace std;

long long convert(long long N, int B) {
  long long fact=1,ret=0;
  while(N) {
    if(N%10==1) ret+=fact;
    N/=10;
    fact*=B;
  }
  return ret;
}

vector<long long> getFactors(long long N) {
  vector<long long> ret;
  for(int i=2;i<=10;i++) {
    long long num=convert(N,i);
    for(long long j=2;j*j<=num;j++) {
      if(num%j==0) {
        ret.push_back(j);
        break;
      }
    }
    if(ret.size()+1!=i) return vector<long long>();
  }
  return ret;
}

void doit(int N, int J) {
  srand (time(NULL));
  int have=0;
  set<long long> all;
  for(int j=0;j<1000;j++) {
    long long val=1,fact=10;
    for(int k=1;k<=N-2;k++) {
      if(rand()%2) {
        val+=fact; 
      }
      fact*=10;
    }
    val+=fact;
    if(all.count(val)) continue;
    all.insert(val);
    vector<long long> ret=getFactors(val);
    if(ret.size()) {
      cout<<val;
      for(int k=0;k<ret.size();k++) cout<<" "<<ret[k];
      cout<<endl;
//      for(int k=0;k<ret.size();k++) cout<<" "<<convert(val,k+2)<<endl;
//      cout<<endl;
      have++;
      if(have==J) break;
    }
  }
}

int main() {
  int tests;
  cin>>tests;
  for(int i=0;i<tests;i++) {
    int N,J;
    cin>>N>>J;
    cout<<"Case #"<<(i+1)<<": "<<endl;
    doit(N,J);
  }
  return 0;
}
