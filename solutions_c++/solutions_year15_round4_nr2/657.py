#include <iostream>
#include <algorithm>
#include <cassert>
#include <vector>
#include <string>
using namespace std;
#define double long double
#define p pair<double,double>



void solve(){
  int N;
  double V;
  double X;
  vector<p> sources;
  
  cin>>N>>V>>X;
  for(int i=0;i<N;i++){
    double r, t;
    cin>>r>>t;
    t-=X;
    sources.push_back(make_pair(t,r));
  }

  if(N==2 && sources[0].first==sources[1].first){
    N--;
    sources[0].second=sources[0].second + sources[1].second;
  }
  if(N==2 && sources[0].first==0.0){
    N--;
    if(sources[1].first==0.0)
      sources[0].second=sources[0].second + sources[1].second;
  }
  if(N==2 && sources[1].first==0.0){
    N--;
    sources[0]=sources[1];
  }
  if(N==1){
    if(sources[0].first==0.0){
      cout<<V/sources[0].second;
    }else{
      cout<<"IMPOSSIBLE";
    }
    return;
  }else if(N==2){
    //    cout<<sources[0].first<<" "<<sources[1].first<<endl;
    if((sources[0].first<0 && sources[1].first< 0 )|| (sources[0].first>0 && sources[1].first>0 )){
      cout<<"IMPOSSIBLE";
    }else{
      double v1= V * sources[1].first / (sources[1].first-sources[0].first);
      double v2= V-v1;
      assert(v1>=0 && v2>=0);
      cout<<max(v1/sources[0].second,v2/sources[1].second);
    }
  }else{
    cout<<"";
  }
}

int main(){
  int cases;
  cin>>cases;
  for(int i=0;i<cases;i++){
    cout.precision(20);
    cout<<"Case #"<<i+1<<": ";
    solve();
    cout<<endl;
  }
  return 0;
}
