#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
  int T;cin>>T;
  for(int t=1;t<=T;++t){
    int maxLevel;cin>>maxLevel;
    string s;cin>>s;
    unsigned long long clapped = 0;
    unsigned long long needed = 0;
    for(int level=0;level<=maxLevel;++level){
      int num=s[level]-'0';
      if (clapped<level && num>0) {
        needed += level-clapped;
        clapped += level-clapped;
      }
      clapped += num;
    }
    cout<<"Case #"<<t<<": "<<needed<<endl;
  }
  return 0;
}
