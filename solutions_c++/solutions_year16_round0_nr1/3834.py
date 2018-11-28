
#include <iostream>
#include <cmath>
#include <vector>
#include <string>

using namespace std;

void pv(vector<int> v){
  for(int i=0; i<v.size(); i++){
    cout << v[i] << " ";
  }
  cout << endl;
}

int main(){
  int T;
  cin >> T;
  for(int t=1; t<=T; t++){
    vector<int> v(10, 0);
    int f;
    cin >> f;
    int n = f;
    int last = 0;

    //cout << "f: " << f << endl;

    bool found = false;
    for(int i=0; i<10000; i++){

      //cout << "f: " << f << endl;
      last = n;
      while(true){
        int d = n % 10;
        v[d] += 1;
        n = floor(n/10);
        if(n <= 0){break;}
      }

      //cout << "v: ";
      //pv(v);

      bool done = true;
      for(int j=0; j<v.size(); j++){
        if(v[j] < 1){
          done = false;
        }
      }
      if(done){
        found = true;
        break;
      }
      n = f * (i+2);
    }
    if(found){
      cout << "Case #" << t << ": " << last << endl;

    }else{
      cout << "Case #" << t << ": " << "INSOMNIA" << endl;

    }


  }
  return 0;
}
