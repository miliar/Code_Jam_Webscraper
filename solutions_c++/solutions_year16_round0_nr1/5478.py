#include <iostream>
#include <vector>

#include <cstdio>

using namespace std;

int main(){

  int n;
  cin >> n;

  for(int k = 1; k <= n;k++){
    int N;
    cin >> N;
    vector<int> v(10,0);

    printf("Case #%i: ", k);
    if(N!=0){
      int i = 1;
      int found = 0;
      while(found < 10){
        int x = N*i;
        i++;

        while(x > 0){
          int d = x%10;
          x /= 10;

          if(v[d] == 0){
            found++;
            v[d] = 1;
          }
        }

      }

      printf("%i\n", N*(i-1));

    }else{
      printf("INSOMNIA\n");
    }
  }
  return 0;
}
