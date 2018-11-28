#include <iostream>
#include <vector>
using namespace std;

void get_ans(vector<int>& first, vector<int>& second);

int main(){
 int n;
 cin >> n;

 for (int i = 1; i <= n; ++i){
  vector<int> first;
  vector<int> second;
  int fr, sr, junk;
  cin >> fr;
  for (int e = 1; e <= 4; ++e){
   for (int j = 0; j < 4; ++j){
    cin >> junk;
    if (e == fr){
     first.push_back(junk);
    }
   }
  }
  cin >> sr;
  for (int e = 1; e <= 4; ++e){
   for (int j = 0; j < 4; ++j){
    cin >> junk;
    if (e == sr){
     second.push_back(junk);
    }
   }
  }
  cout << "Case #" << i << ": ";
  get_ans(first, second);
 }
 return 0;
}

void get_ans(vector<int>& first, vector<int>& second){
 vector<int> tmp;
 for (int i = 0; i < 4; ++i){
  for (int j = 0; j < 4; ++j){
   if (first[i] == second[j]){
    tmp.push_back(first[i]);
   }
  }
 }
 if (tmp.size() == 0){
  cout << "Volunteer cheated!\n";
 }
 else if(tmp.size() == 1){
  cout << tmp[0] << endl;
 }
 else {
  cout << "Bad magician!\n";
 }
}
