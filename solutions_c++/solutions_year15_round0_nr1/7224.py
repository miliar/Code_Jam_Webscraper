#include <iostream>
#include <cstdio>
#include <string>
using namespace std;
int main(){
  int Case,C;
  int mx=0;
  int stand;
  int need;
  string str;
  cin >> Case;
  C=1;
  while(Case--){
    stand = 0;
    need = 0;
    cin >> mx >> str;
    for(int i = 0 ; i < str.size() ; i++){
      int p = int(str[i])-int('0');
      if(p>0){
        if(stand>=i)stand+=p;
        else{
          need += i-stand;
          stand = i+p;
        }
      }
    }
  //  cout << "Case #1: " << C++ <<": " << need << endl;
    printf("Case #%d: %d\n",C++,need);
  }
  return 0;
}
