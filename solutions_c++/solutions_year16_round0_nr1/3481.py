#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main(){
  int cases;
  cin >> cases;
  stringstream tos;
  long long snum, num;
  bool check[10];
  for( int i = 1; i< cases+1; i++){
    for(int j = 0; j<10; j++){
      check[j] = false;
    }
    bool stop = false;
    cin >> snum;
    int count = 1;
    if(snum == 0){
      cout << "Case #" << i << ": INSOMNIA\n";
    }
    else{
      while(!stop){
        tos.str("");
        num = snum * count;
        tos << num;
        string nums = tos.str();
        for(int j = 0; j<nums.size(); j++){
          check[nums[j] - '0'] = true;
        }
        stop = true;
        for(int j = 0; j<10; j++){
          stop = stop && check[j];
        }
        count++;
      }
      cout << "Case #" << i << ": " << num << endl;
    }
  }
}
