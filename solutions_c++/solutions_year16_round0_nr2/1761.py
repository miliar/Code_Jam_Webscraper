#include<iostream>
#include<stdio.h>
#include<string>

using namespace std;

int main(){
  int T;
  scanf("%d", &T);
  string pancakes;
  int flip = 0;
  for (int t = 0; t < T; t++){
    flip = 0;
    cin >> pancakes;
    for (int i = 1; i < pancakes.length(); i++){
      if (pancakes[i] != pancakes[i - 1]) flip++;
    }
    //cout << flip << "\n";
    //if (flip > 0 && pancakes[0]=='+') flip++;
    if (pancakes[pancakes.length()-1] == '-') flip++;
    //if (flip % 2 == 0 and pancakes[0] == '-') flip++;
    printf("Case #%d: %d\n", t+1, flip);
  }
  return 0;
}