#include<iostream>
#include<fstream>
using namespace std;
int main(){
    ifstream in("input.txt");
    ofstream n("out.txt");
    
    int size = 0;
    bool winX = false;
    bool winO = false;    
    bool incomplete = false;
    in>>size;
    int total = size+1;
    while(size!=0){
          char arr[4][4];
          for(int i=0; i<4;i++){
                  for(int j=0; j<4;j++){
                    in>>arr[i][j];
                  }
          }
          winX = false;
          winO = false; 
          incomplete = false;   
          for(int i=0; i<4;i++){
                  for(int j=0; j<4;j++){
                    if(arr[i][j] == '.'){incomplete = true;}
                  } 
                  if(arr[i][0] == arr[i][1] && arr[i][1]== arr[i][2] && arr[i][2] == arr[i][3]){
                               if(arr[i][1] == 'X'){winX = true;}
                               else if(arr[i][1] == 'O'){winO = true;}
                  }
                  else if(arr[i][0] == arr[i][1] && arr[i][1]== arr[i][2] && arr[i][3] == 'T'){
                               if(arr[i][1] == 'X'){winX = true;}
                               else if(arr[i][1] == 'O'){winO = true;}
                  }
                  else if(arr[i][1] == arr[i][2] && arr[i][2]== arr[i][3] && arr[i][0] == 'T'){
                               if(arr[i][1] == 'X'){winX = true;}
                               else if(arr[i][1] == 'O'){winO = true;}
                  }
                  else  if(arr[0][i] == arr[1][i] && arr[1][i]== arr[2][i] && arr[2][i] == arr[3][i]){
                               if(arr[1][i] == 'X'){winX = true;}
                               else if(arr[1][i] == 'O'){winO = true;}
                  }
                  else if(arr[0][i] == arr[1][i] && arr[1][i]== arr[2][i] && arr[3][i] == 'T'){
                               if(arr[1][i] == 'X'){winX = true;}
                               else if(arr[1][i] == 'O'){winO = true;}
                  }
                  else if(arr[1][i] == arr[2][i] && arr[2][i]== arr[3][i] && arr[0][i] == 'T'){
                               if(arr[1][i] == 'X'){winX = true;}
                               else if(arr[1][i] == 'O'){winO = true;}
                  }
                  else if(arr[0][0] == arr[1][1] && arr[1][1]== arr[2][2] && arr[2][2] == arr[3][3]){
                               if(arr[1][1] == 'X'){winX = true;}
                               else if(arr[1][1] == 'O'){winO = true;}
                  }
                  else if(arr[0][0] == arr[1][1] && arr[1][1]== arr[2][2] && arr[2][2] == arr[3][3]){
                               if(arr[1][1] == 'X'){winX = true;}
                               else if(arr[1][1] == 'O'){winO = true;}
                  }
                  
                  else if(arr[0][0] == arr[1][1] && arr[1][1]== arr[2][2] && arr[3][3] == 'T'){
                               if(arr[1][1] == 'X'){winX = true;}
                               else if(arr[1][1] == 'O'){winO = true;}
                  }
                  else if(arr[1][1] == arr[2][2] && arr[2][2]== arr[3][3] && arr[0][0] == 'T'){
                               if(arr[1][1] == 'X'){winX = true;}
                               else if(arr[1][1] == 'O'){winO = true;}
                  }
                  else if(arr[0][3] == arr[1][2] && arr[1][2]== arr[2][1] && arr[2][1] == arr[3][0]){
                               if(arr[1][2] == 'X'){winX = true;}
                               else if(arr[1][2] == 'O'){winO = true;}
                  }
                  else if(arr[0][3] == arr[1][2] && arr[1][2]== arr[2][1] && arr[3][0] == 'T'){
                               if(arr[1][1] == 'X'){winX = true;}
                               else if(arr[1][2] == 'O'){winO = true;}
                  }
                  else if(arr[1][2] == arr[2][1] && arr[2][1]== arr[3][0] && arr[0][3] == 'T'){
                               if(arr[1][1] == 'X'){winX = true;}
                               else if(arr[1][2] == 'O'){winO = true;}
                  }
          }
          cout<<"Case #"<<total-size<<": ";
          if(winX){cout<<"X won";}
          else if(winO){cout<<"O won";}
          else if(incomplete){cout<<"Game has not completed";}
          else{cout<<"Draw";}
          cout<<endl;

         n<<"Case #"<<total-size<<": ";
          if(winX){n<<"X won";}
          else if(winO){n<<"O won";}
          else if(incomplete){n<<"Game has not completed";}
          else{n<<"Draw";}
          n<<endl;

          size--;              
    }
    system("pause");
    
    
}
