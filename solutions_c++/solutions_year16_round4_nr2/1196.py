#include <bits/stdc++.h>
using namespace std;

#define dbg(x) cerr<<#x<<"="<<x<<endl
typedef long long ll;
typedef pair<int,int> pii;

int N,K;
double P[300];

double f(int k, vector<double> v, int i){
  if(i==N)
    return (k?0:v[K/2]);

  double ret = f(k,v,i+1);
  vector<double> v2(v.size()+1,0);
  for(int j=0;j<v.size();j++){
    v2[j] += v[j]*(1-P[i]);
    v2[j+1] += v[j]*P[i];
  }
  return max(ret, f(k-1, v2, i+1));
}

void run(){
  cin>>N>>K;
  for(int i=0;i<N;i++)
    cin>>P[i];
  vector<double> v;
  v.push_back(1);
  printf("%.7lf",f(K, v, 0));
}


int main(){
  int T;
  cin>>T;
  for(int t=1;t<=T;t++){
    cout<<"Case #"<<t<<": ";
    run();
    cout<<endl;
  }
  return 0;
}
