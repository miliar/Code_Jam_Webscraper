#include <iostream>
#include <vector>
using namespace std;
void solve(int n){
  int first_row ,second_row;
  vector<int> count_number(32,0);
  
  cin >> first_row;
  for (int i = 1;  i <= 4 ; i++){
    for(int j = 1; j <= 4;j++){
      int tmp ;
      cin >> tmp;
      if(i == first_row)count_number[tmp] ++ ;
    }
  }
  cin >> second_row;
  for (int i = 1;  i <= 4 ; i++){
    for(int j = 1; j <= 4;j++){
      int tmp ;
      cin >> tmp;
      if(i == second_row)count_number[tmp]++;
    }
  }
  int ans = -1,multipleCards=0;
  for(int i = 1; i <= 16; i ++){
#ifdef DEBUG
    cout << "count_number["<<i<<"]="<<count_number[i]<<endl;
#endif
    if (count_number[i] == 2){
      ans = i;
      multipleCards ++;
    }
  }
  if(multipleCards > 1){
    cout << "Case #"<<n<<": Bad magician!"<<endl;  
  }else if (ans < 0){
    cout << "Case #"<<n<<": Volunteer cheated!"<<endl;  
  }else {
    cout << "Case #"<<n<<": " << ans <<endl;  
  }
}
int main(){
  int T;
  cin >> T;
  for(int i = 0; i < T;i++){
    solve(i+1);
  }
  return 0;
}
