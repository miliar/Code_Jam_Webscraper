#include<iostream>
using namespace std;

int main(){
  int cases = 0, radius = 0, paint = 0;
  cin >> cases;
  int cp = cases;
  while(cp > 0){
    int count = 0;
    cin >> radius >> paint;
    radius++;
    while(paint > 0 && (paint-2*radius+1) >= 0){
      paint = paint-2*radius+1;
      radius +=2;
      count++;
    }
    cp--;

    cout << "Case #" << cases-cp << ": ";
    cout << count << endl;
  }
  return 0;
}
