#include<iostream>
#include<fstream>

using namespace std;

int main()
{
  ifstream input;
  input.open("A-small-attempt0.in");
  ofstream output;
  output.open("A-small-attempt0.out");
  
  int main_loop;
  input >> main_loop;
  for(int i=0;i<main_loop;i++){
    int s1;
    input >> s1;
    int arr1[4][4];
    s1--;
    
    for(int k=0;k<4;k++){
    for(int j=0;j<4;j++){
      input >> arr1[k][j];
      //cout << arr1[k][j] << endl;
    }
    }
    
    int s2;
    input >> s2;
    int arr2[4][4];
    s2--;
    for(int j=0;j<4;j++){
    for(int k=0;k<4;k++){
      input >> arr2[j][k];
      //cout << arr2[j][k] << endl;
    }
    }
    int sel=0,count=0;
    
    for(int j=0;j<4;j++){
      for(int k=0;k<4;k++){
        if(arr1[s1][j]==arr2[s2][k]){
          sel=arr1[s1][j];
          count++;
        }
      }
    }
    //cout << s1 << "  " << s2 << endl;
    
    if(count==0){
      output << "Case #" << i+1 << ": Volunteer cheated!" << endl;
    }
    else if(count==1){
      output << "Case #" << i+1 << ": " << sel << endl;
    }
    else{
      output << "Case #" << i+1 << ": Bad magician!" << endl;
    }
    //system("pause");
  }
  
  
  //system("pause");
  return 0;
}
