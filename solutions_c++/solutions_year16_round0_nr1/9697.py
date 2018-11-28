#include <iostream>
#include <cstdlib>
#include <vector>

using namespace std;

bool seenAllNumbers(std::vector<int> array){
  for(int i = 0; i < array.size(); i++){
    if(array[i] != i){
      return false;
    }
  }
  return true;
}

int main(){
  int T = 0, N = 0, j = 1, num = 0;
  vector<int> nSeen(10);
  cin >> T;
  if(T < 1 || T > 100)
    exit(0);
  for(int i = 1; i <= T; i++){
    cin >> N;
    if(N < 0 || N > 1000000)
      exit(0);
    fill(nSeen.begin(), nSeen.end(), -1);
    if(N == 0)
      cout << "Case #" << i << ": INSOMNIA" << endl;
    else{
      while(!seenAllNumbers(nSeen)){
        num = N * j++;
        int n = num;
        while (n != 0) {
             nSeen[n % 10] = n % 10;
             n /= 10;
        }
      }
      cout << "Case #" << i << ": " << num << endl;
      num = 0, j = 1;
    }

  }

  exit(0);
}
