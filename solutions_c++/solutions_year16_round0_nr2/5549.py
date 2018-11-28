#include <iostream>
#include <vector>

#include <cstdio>

using namespace std;

int main(){
  int n;

  cin >> n;

  for(int k = 1; k <= n; k++){
    string str;
    cin >> str;
    printf("Case #%i: ", k);

    if(str.size() == 1){
        if(str[0] == '-'){
          printf("1\n");
        }else{
          printf("0\n");
        }
    }else{
      int resp = str[str.size()-1] == '-' ? 1 : 0;
      for(int i = 1; i < str.size(); i++){
        if(str[i-1] != str[i]){
          resp++;
        }
      }

      printf("%i\n",resp);
    }

  }

  return 0;
}
