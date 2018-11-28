#include <iostream> 
#include <string>
using namespace std;  

int main() {
  int t, n, m,tries[100],vals[100];
  char pat[100][100],final[100][100];
  
  cin >> t;  // number of text cases

  for(int i=0;i<t;i++){
    cin>>pat[i];
    //strcpy(local[i],pat[i]);
  }

  for(int i=0;i<t;i++){
    int top=0;
    final[i][top] = pat[i][0];
    for(int j =1;pat[i][j]!='\0';j++){      
         if( pat[i][j] != final[i][top] && pat[i][j]!='\0' ){
             final[i][++top] = pat[i][j];   
         }else{
               continue;
         }       
    }//end og j
 
  int mm = strlen(final[i]);

  if(final[i][mm-1] == '+'){
    mm = mm -1;
  }
 
  cout << "Case #" << (i+1) << ": " << mm << endl;
  }//end of i



}
