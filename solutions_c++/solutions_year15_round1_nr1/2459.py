#include <iostream>

using namespace std;

int main(){
  int T;
  cin >> T;
  for(int t = 1; t <= T; t++){
    int  N;
    cin >> N;
    int list[N];
    int first = 0;
    int prev = 0;
    int rate = 0;
    for(int n = 0; n < N; n++){
      cin >> list[n];
      if(prev - list[n] > rate) rate = prev - list[n];
      if(list[n] < prev){
	first += prev - list[n];
      }
      prev = list[n];
    }
    int second = 0;
    //int rate = list[N-2] - list[N-1];
    for(int n = 0; n < N - 1; n++){
      if(list[n]>rate){
	second += rate;
      }
      else{
	second += list[n];
      }
    }
    cout << "Case #" << t << ": " << first << " " << second << "\n";
  }
}