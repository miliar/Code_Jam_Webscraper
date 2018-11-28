#include <iostream> 
#include <string>
using namespace std;  
int main() {
  int t, n, m,mm;
  char input_string[500][500],result[500][500];
  cin >> t;
  for(int i=0;i<t;i++){
    cin>>input_string[i];
  }
  for(int i=0;i<t;i++){
    int top=0;
    result[i][top] = input_string[i][0];
    for(int j =1;input_string[i][j]!='\0';j++){      
         if( input_string[i][j] != result[i][top] && input_string[i][j]!='\0' ){
             result[i][++top] = input_string[i][j];   
         }else{
               continue;
         }       
    }
  mm = strlen(result[i]);
  if(result[i][mm-1] == '+'){
    mm = mm -1;
  }
  cout << "Case #" << (i+1) << ": " << mm << endl;
  }//end of i



}
