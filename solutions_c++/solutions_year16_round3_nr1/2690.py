#include <iostream>
#include <array>
#include <vector>
#include <algorithm>
typedef unsigned int ui;
using namespace std;

int main(){
  ui t;
  cin >> t;
  for(ui i = 0; i < t; i++){
    ui n;
    cin >> n;
    array<ui, 26> p;
    for(ui j = 0; j < n; j++){
      cin >> p[j];
    }

    cout << "Case #" << i + 1 << ":";
    while(true){
      vector<ui> largest_parties = {};
      ui largest = 0;
      ui second_largest = 0;
      for(ui j = 0; j < n; j++){
        if(largest == p[j]){
          largest_parties.push_back(j);
        } else if(largest < p[j]){
          second_largest = largest;
          largest = p[j];
          largest_parties.clear();
          largest_parties.push_back(j);
        }else if(second_largest < p[j] && largest > p[j]){
          second_largest = p[j];
        }
      }
      if(largest == 0){
        break;
      }
      if(largest_parties.size() % 2 == 1){
        for(ui j = 0; j < largest - second_largest; j++){
          cout << " " << char('A' + largest_parties[0]);
        }
        p[largest_parties[0]] = second_largest;
        largest_parties.erase(largest_parties.begin());
      }
      if(largest_parties.size() > 0){
        for(ui k = 0; k < largest_parties.size(); k += 2){
          for(ui j = 0; j < largest - second_largest; j++){
            cout << " " << char('A' + largest_parties[k]) << char('A' + largest_parties[k + 1]);
          }
        }
      }
      for(auto j : largest_parties){
        p[j] = second_largest;
      }
    }
    cout << endl;
  }
  return 0;
}
