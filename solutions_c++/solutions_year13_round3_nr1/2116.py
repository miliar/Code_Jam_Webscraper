#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>

using namespace std;

int main(){


  int n;
  cin >> n;

  for(int i = 0; i < n; i++){
    int length;
    string str;
    int res = 0;
    cin >> str >> length;
    int end = 0;


    for(int j = str.size(); j >= length; j--){
      int add = 0;
      for(int k = 0; k <= str.size() - j; k++){
        int count = 0;
        string tmp = str.substr(k, j);
        for(int num = 0; num < j; num++){
          char ch = tmp[num];
          if(ch != 'a' && ch != 'i' && ch != 'u' && ch != 'e' && ch != 'o'){
            count++;
            if(count >= length){
              res++;
              break;
            }
          }else{
            count = 0;
          }
        }
      }
    }
    printf("Case #%d: %d\n", i+1, res);
  }
  return 0;
}
