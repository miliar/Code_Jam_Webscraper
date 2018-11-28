#include <iostream>
#include <sstream>
#include <string>

using namespace std;

string judge_magician(int ct[],int b){
  string result;
  const int MagicNumber = 2;
  int judge = 0, judgeNumber;
  ostringstream stream;
  
  for(int k=0;k<b;k++){
    if(ct[k] == MagicNumber){
      judge++;
      judgeNumber = k+1;
    }
  }
  if(judge == 0){
    result = "Volunteer cheated!";
  }
  else if(judge == 1){
    stream << judgeNumber;
    result = stream.str();
  }
  else{
    result = "Bad magician!";
  }
  return result;
}

void disptable(int size, int table[4][4]){
  for(int row=0;row<size;row++){
    for(int col=0;col<size;col++){
      cout << table[row][col] << "  ";
    }
    cout << endl;
  } 
}

int main(){
  int repeat;
  int row_num;
  const int tSize = 4;
  const int tSquaresize = tSize*tSize;
  int table[tSize][tSize];

  cin >> repeat;
  
  for(int i=0;i<repeat;i++){
    cin >> row_num;
    row_num--;
    int compare_table[tSquaresize] = {0};

    for(int row=0; row < tSize;row++){
       for(int col=0; col < tSize;col++){
	cin >> table[row][col];
      }
    }
    for(int col=0;col < tSize;col++){
      compare_table[table[row_num][col]-1]++;
    }

    //    disptable(tSize,table);

    cin >> row_num;
    row_num--;
    for(int row=0; row < tSize;row++){
       for(int col=0; col < tSize;col++){
	cin >> table[row][col];
      }
    }
    for(int col=0;col < tSize;col++){
      compare_table[table[row_num][col]-1]++;
    }

    //    disptable(tSize,table);

    cout << "Case #"<< i+1 << ": ";
    cout << judge_magician(compare_table,tSquaresize);
    //    if(i<repeat-1){
      cout << endl; 
      //    }
  }  
}
