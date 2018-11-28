#include <iostream>
 
using namespace std;
 
bool f(char tab, char x){
     if(tab == x)
            return true;
     if(tab == 'T')
            return true;
     return false; 
}
 
int main()
{
   int qtd;
   bool ponto = false;
   char tab[4][4];
   cin >> qtd;
   
   for(int z = 0; z < qtd; z++){
           ponto = false;
      for(int x = 0; x < 4; x++){
         for(int y = 0; y < 4; y++){
            cin >> tab[x][y];  
            if(tab[x][y] == '.'){
               ponto = true;
            }      
         }
      }
      if( ((f(tab[0][0],'X')) && (f(tab[0][1],'X')) && (f(tab[0][2],'X')) && (f(tab[0][3],'X'))) || 
          ((f(tab[1][0],'X')) && (f(tab[1][1],'X')) && (f(tab[1][2],'X')) && (f(tab[1][3],'X'))) ||
          ((f(tab[2][0],'X')) && (f(tab[2][1],'X')) && (f(tab[2][2],'X')) && (f(tab[2][3],'X'))) ||
          ((f(tab[3][0],'X')) && (f(tab[3][1],'X')) && (f(tab[3][2],'X')) && (f(tab[3][3],'X'))) ||
          ((f(tab[0][0],'X')) && (f(tab[1][1],'X')) && (f(tab[2][2],'X')) && (f(tab[3][3],'X'))) ||
          ((f(tab[0][3],'X')) && (f(tab[1][2],'X')) && (f(tab[2][1],'X')) && (f(tab[3][0],'X'))) ||
          ((f(tab[0][0],'X')) && (f(tab[1][0],'X')) && (f(tab[2][0],'X')) && (f(tab[3][0],'X'))) ||
          ((f(tab[0][1],'X')) && (f(tab[1][1],'X')) && (f(tab[2][1],'X')) && (f(tab[3][1],'X'))) ||
          ((f(tab[0][2],'X')) && (f(tab[1][2],'X')) && (f(tab[2][2],'X')) && (f(tab[3][2],'X'))) ||
          ((f(tab[0][3],'X')) && (f(tab[1][3],'X')) && (f(tab[2][3],'X')) && (f(tab[3][3],'X'))) ){
          cout << "Case #" << z+1 << ": X won"; 
          if(z != qtd-1)
          cout << endl;
        
      }else{
          if( ((f(tab[0][0],'O')) && (f(tab[0][1],'O')) && (f(tab[0][2],'O')) && (f(tab[0][3],'O'))) || 
              ((f(tab[1][0],'O')) && (f(tab[1][1],'O')) && (f(tab[1][2],'O')) && (f(tab[1][3],'O'))) ||
              ((f(tab[2][0],'O')) && (f(tab[2][1],'O')) && (f(tab[2][2],'O')) && (f(tab[2][3],'O'))) ||
              ((f(tab[3][0],'O')) && (f(tab[3][1],'O')) && (f(tab[3][2],'O')) && (f(tab[3][3],'O'))) ||
              ((f(tab[0][0],'O')) && (f(tab[1][1],'O')) && (f(tab[2][2],'O')) && (f(tab[3][3],'O'))) ||
              ((f(tab[0][3],'O')) && (f(tab[1][2],'O')) && (f(tab[2][1],'O')) && (f(tab[3][0],'O'))) ||
              ((f(tab[0][0],'O')) && (f(tab[1][0],'O')) && (f(tab[2][0],'O')) && (f(tab[3][0],'O'))) ||
              ((f(tab[0][1],'O')) && (f(tab[1][1],'O')) && (f(tab[2][1],'O')) && (f(tab[3][1],'O'))) ||
              ((f(tab[0][2],'O')) && (f(tab[1][2],'O')) && (f(tab[2][2],'O')) && (f(tab[3][2],'O'))) ||
              ((f(tab[0][3],'O')) && (f(tab[1][3],'O')) && (f(tab[2][3],'O')) && (f(tab[3][3],'O'))) ){
              cout << "Case #" << z+1 << ": O won"; 
              if(z != qtd-1)
              cout << endl;
          }else{
              if(ponto){
                  cout << "Case #" << z+1 << ": Game has not completed"; 
                  if(z != qtd-1)
                  cout << endl;          
              }else{
                  cout << "Case #" << z+1 << ": Draw"; 
                  if(z != qtd-1)
                  cout << endl;        
              }
          }
      }
   }
   
   
   return 0;
}
