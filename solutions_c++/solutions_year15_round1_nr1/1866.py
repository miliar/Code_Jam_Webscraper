#include <iostream>
#include <vector>

using namespace std;

int main(){
  int T;
  cin >> T;
  for(int t=1; t <=T; ++t){
    int y=0;
    int z=0;
    int n;
    cin >> n;
    vector<int> v;
    for(int i=0; i<n; ++i){
      int tmp;
      cin >> tmp;
      v.push_back(tmp);
    }
    //------------------------------------------------------------------
    for(int i=1; i<n; ++i){
      if(v[i-1] > v[i]){
        y += v[i-1]-v[i];
      }
    }
    //------------------------------------------------------------------
    int maxdiff = 0;
    for(int i=1; i<n; ++i){
      if(v[i-1]-v[i]>maxdiff){
        maxdiff = v[i-1]-v[i];
      }
    }
    for(int i=1; i<n; ++i){
      if(v[i-1]>=maxdiff){
        z += maxdiff;
      }else{
        z += v[i-1];
      }
    }
    //------------------------------------------------------------------
    cout << "Case #" << t << ": "<< y << " " << z  << endl;
  }
}
