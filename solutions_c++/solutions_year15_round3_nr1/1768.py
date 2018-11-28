#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#define push_back PB
using namespace std;

typedef long long in;

int main(){
  in t;
  cin >> t;
  for(in test=1;test<=t;test++){
    int r,c,w;
    cin >> r >> c >> w;
    int score=c/w-1;
    if(c%w==0)
      score+=w;
    else
      score+=(1+w);
    cout << "Case #" << test << ": " << score << endl;
  }
  return 0;
}