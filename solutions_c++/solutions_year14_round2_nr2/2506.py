#include <iostream>
#include <string>

using namespace std;

int count;

int winNum(int a, int b,int c){
  for (int i=0; i<a;i++){
    for (int j=0; j<b;j++){
      int win = i&j;
      if (win < c)
	count++;
    }
  }
  return count;
}

void mission() {
  int a,b,k;
  cin >> a >> b >>k;
  cout << winNum(a,b,k);
}

int main() {
  int numInput;
  cin >> numInput;
  for (int i = 1; i <= numInput; i++) {
    count = 0;
    cout <<  "Case #" <<  i <<  ": ";
    mission();
    cout <<  endl;
  }
  return 0;
}