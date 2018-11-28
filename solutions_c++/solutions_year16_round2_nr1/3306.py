#include <iostream>

using namespace std;

int S;

int main(){
  cin >> S;
  for(int ni = 0; ni < S; ni++){
    string t; cin >> t;
    int temp[26];
    int count[10];
    for(int i = 0; i < 26; i++){temp[i] = 0;}
    for(int i = 0; i < 10; i++){count[i]= 0;}
    for(int i = 0; i < t.length(); i++){
      temp[t[i]-'A'] ++;
    }
    count[0] = temp[25]; temp[4] -= temp[25]; temp[17]-=temp[25];temp[14]-=temp[25];
    count[2] = temp[22]; temp[19]-= temp[22]; temp[14] -= temp[22];
    count[4] = temp[20]; temp[5] -= temp[20]; temp[14] -= temp[20]; temp[17]-=temp[20];
    count[6] = temp[23]; temp[18] -= temp[23]; temp[8] -= temp[23];
    count[8] = temp[6]; temp[4]-=temp[6]; temp[8] -= temp[6]; temp[7] -= temp[6]; temp[19]-=temp[6];
    count[3] = temp[19]; temp[7] -= temp[19]; temp[17] -= temp[19]; temp[4] -= 2*temp[19];
    count[7] = temp[18]; temp[4]-=2*temp[18]; temp[21] -= temp[18]; temp[13]-=temp[18];
    count[5] = temp[21]; temp[5] -= temp[21]; temp[8]-=temp[21]; temp[4] -= temp[21];
    count[1] = temp[14]; temp[4]-= temp[14]; temp[13]-=temp[14];
    count[9] = temp[4];

    cout << "Case #" << ni+1 << ": ";
    for(int i = 0; i < 10; i++){
      for(int j = 0; j < count[i]; j++){
	cout << i;
      }
    }
    cout << endl;
  }
  return 0;
}
    
