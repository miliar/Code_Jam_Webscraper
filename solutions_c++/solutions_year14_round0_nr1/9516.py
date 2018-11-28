#include<iostream>
using namespace std;
int const SIZE = 4;

int main(){
  ios_base::sync_with_stdio(false);
  
  int t;
  cin >> t;
  
  for(int k=1;k<=t;k++){
  
    int f;
    cin >> f;
    int fRow[SIZE];
    int temp;
    for(int i=1;i<=SIZE;i++)
      for(int j=0;j<SIZE;j++)
        if(i == f)
          cin >> fRow[j];          
        else
          cin >> temp;
  
    int s;
    cin >> s;
  
    int sRow[SIZE];
  
    for(int i=1;i<=SIZE;i++)
      for(int j=0;j<SIZE;j++)
        if(i == s)
          cin >> sRow[j];
        else
          cin >> temp;
        
    int check = 0;
    int ans = 0;
    for(int i=0;i<SIZE;i++){
      for(int j=0;j<SIZE;j++){          
          if(fRow[i] == sRow[j]){
            check++;
            ans = fRow[i];
          }
      }
    }
    cout << "Case #" << k << ": ";
    if(check == 1){
      cout << ans << endl;
    }else if(check == 0){
      cout << "Volunteer cheated!" << endl;
    }else{    
      cout << "Bad magician!" << endl;
    }
  }
}

