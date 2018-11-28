#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(){
  int kase;
  cin >> kase;
  int k = 0;
  while(k < kase){
    string line;
    cin >> line;
    int n = line.length();
    int cnt = 0;
    char now = line[0];
    for(int i=1;i<n;i++){
      char c = line[i];
      if(c!=now){
        cnt++;
        now = c;
      }
    }
    if(now=='-') cnt++;
    cout<<"Case #"<<(k+1)<<": "<<cnt<<endl;
    k++;
  }
  return 0;
}
