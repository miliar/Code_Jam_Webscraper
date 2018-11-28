#include <iostream>
using namespace std;

bool seen[10];

bool end(){
  for(int i = 0; i < 10; i++){
    if (!seen[i]){
      return false;
    }
  }
  return true;
}

void fillrests(unsigned long num){
  while(num != 0){
    seen[num % 10] = true;
    num /= 10;
  }
}

int main(){
  int T;
  cin >> T;

  for(int i = 0; i < T; i ++){
    unsigned int n;

    cin >> n;
    unsigned long curnum = 0;
    for(int j = 0; j < 10; j++){
      seen [j] = false;
    }

    if ( n == 0){
      cout << "Case #" << i+1 << ": INSOMNIA" << endl;
      continue;

    }
    while(!end()){
      curnum += n;
      fillrests(curnum);
    }
    cout << "Case #" << i+1 << ": " << curnum << endl;

  }


}
