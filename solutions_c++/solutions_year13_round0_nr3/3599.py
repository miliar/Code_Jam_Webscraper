
#include <iostream>
#include <sstream>
using namespace std;

typedef long long LL;


bool is_palin(LL l){

  ostringstream ss;
  ss << l;
  string str = ss.str();

  int str_l = str.length();
  for(int i=0; i<str_l; i++)
    if(str[i] != str[str_l-i-1]) return false;

  return true;
}


int count_range(LL low, LL high){

  int c = 0;
  for(int i = 0; ; i++){
    if(i*i > high) break;
    if(is_palin(i)){
      if(is_palin(i*i)){
        if(i*i < low) continue;
        c++;
      }
    }
  }

  return c;

}



int main(){

  
  int ncases;
  cin >> ncases;

  for(int i=0; i<ncases; i++){

    int low, high;
    cin >> low;
    cin >> high;

    cout << "Case #" << i+1 << ": " << count_range(low,high) << endl;


  }

}

