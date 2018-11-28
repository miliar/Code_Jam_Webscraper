#include <iostream>
#include <vector>
#include<string>
//#define DEBUG
using namespace std;

char enter_Game(){
  vector<vector<char> > Game (5, vector<char> (5, 'T')) ;
  vector<bool> bcol (5,true);
  bool bligne ;
  bool cpt = true ;
  string s ;

  for (int i = 1; i < 5; i++){
    bligne = true ;
    for (int j = 1; j < 5; j++){
      cin >> Game[i][j] ;
      if (Game[i][j] != '.'){
        bligne = bligne && (Game[i][j] == Game[i][j-1] || Game[i][j-1] == 'T' || Game[i][j] == 'T') ;
        bcol[j] = bcol[j] && (Game[i][j] == Game[i-1][j] || Game[i-1][j] == 'T' || Game[i][j] == 'T' ) ;
      }
      else {
        cpt = false;
        bligne = false ;
        bcol[j] = false ;
      }
    }
    if (bligne){
      for(int k = 0; k <= 4-i; k++)
        getline(cin, s) ;

      return (Game[i][1] != 'T')? Game[i][1] : Game[i][2];
    }
  }

  for(int j = 1; j < 5; j++){
    if (bcol[j])
      return (Game[1][j] != 'T')? Game[1][j] : Game[2][j] ;
  }
#ifdef DEBUG
  for (int i = 1; i < 5; i++){
    for (int j = 1; j < 5; j++)
      cout << Game[i][j] ;
    cout << endl ;
  }
#endif 

  if (Game[1][1] != '.' &&
(Game[1][1] == Game[2][2] || Game[1][1] == 'T' || Game[2][2] == 'T')
&&
(Game[2][2] == Game[3][3] || Game[3][3] == 'T' || Game[2][2] == 'T')
&&
(Game[4][4] == Game[3][3] || Game[4][4] == 'T' || Game[3][3] == 'T'))
    return  (Game[1][1] != 'T')? Game[1][1] : Game[2][2] ;

  if (Game[4][1] != '.' &&
(Game[4][1] == Game[3][2] || Game[4][1] == 'T' || Game[3][2] == 'T')
&&
(Game[3][2] == Game[2][3] || Game[2][3] == 'T' || Game[3][2] == 'T')
&&
(Game[1][4] == Game[2][3] || Game[1][4] == 'T' || Game[2][3] == 'T'))
    return  (Game[4][1] != 'T')? Game[4][1] : Game[3][2] ;



  if (cpt)
    return 'D' ;
  else
    return 'N';
}



int main()
{
  int N ;
  cin >> N ;

  for (int k = 1; k <= N; k++){
    char w ;
    w = enter_Game() ;
    cout << "Case #" << k << ": " ;
    switch (w){
      case 'X': 
        {
          cout << "X won" << endl;
          break ;
        }
      case 'O': 
        {
          cout << "O won" << endl;
          break;
        }
      case 'D':
        {
          cout << "Draw" << endl;
          break;
        }
      case 'N':
        {
          cout << "Game has not completed" << endl ;
        }
    }
  }
}


