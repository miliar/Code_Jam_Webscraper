#include<iostream>
#include<string>
 
using namespace std;
 
bool fini(string[]);
string gagnant(string[]);
 
int main(void)
{
int T=0;
string tab[4];
cin >> T;
string res="";
for(int i=0 ; i<T ; i++)
{
  cout << "Case #" << i+1 <<": ";
  for(int j=0 ; j<4 ; j++)
  {
      cin >> tab[j];
  }
  res=gagnant(tab);
  if(res!="")
    cout<<res+" won";
  else if(fini(tab))
    cout << "Draw";
  else
    cout << "Game has not completed";
  cin.ignore();
  if(i!=(T-1))
    cout << endl;
}
}
 
bool fini(string* tab)
{
  for(int i=0 ; i<4 ; i++)
  {
    if(tab[i].find_first_of(".")!=tab[i].npos)
      return false;
  }
  return true;
}
 
string gagnant(string *tab)
{
  for(int i=0 ; i<4 ; i++)
    if(tab[i][0]=='T' || tab[i][0]=='O')
      if(tab[i][1]=='T' || tab[i][1]=='O')
        if(tab[i][2]=='T' || tab[i][2]=='O')
          if(tab[i][3]=='T' || tab[i][3]=='O')
            return "O";
  for(int i=0 ; i<4 ; i++)
    if(tab[0][i]=='T' || tab[0][i]=='O')
      if(tab[1][i]=='T' || tab[1][i]=='O')
        if(tab[2][i]=='T' || tab[2][i]=='O')
          if(tab[3][i]=='T' || tab[3][i]=='O')
            return "O";
  if(tab[0][0]=='O' || tab[0][0]=='T')
    if(tab[1][1]=='O' || tab[1][1]=='T')
      if(tab[2][2]=='O' || tab[2][2]=='T')
        if(tab[3][3]=='O' || tab[3][3]=='T')
          return "O";
  if(tab[0][3]=='O' || tab[0][3]=='T')
    if(tab[1][2]=='O' || tab[1][2]=='T')
      if(tab[2][1]=='O' || tab[2][1]=='T')
        if(tab[3][0]=='O' || tab[3][0]=='T')
          return "O";
  for(int i=0 ; i<4 ; i++)
    if(tab[i][0]=='T' || tab[i][0]=='X')
      if(tab[i][1]=='T' || tab[i][1]=='X')
        if(tab[i][2]=='T' || tab[i][2]=='X')
          if(tab[i][3]=='T' || tab[i][3]=='X')
            return "X";
  for(int i=0 ; i<4 ; i++)
    if(tab[0][i]=='T' || tab[0][i]=='X')
      if(tab[1][i]=='T' || tab[1][i]=='X')
        if(tab[2][i]=='T' || tab[2][i]=='X')
          if(tab[3][i]=='T' || tab[3][i]=='X')
            return "X";
  if(tab[0][0]=='X' || tab[0][0]=='T')
    if(tab[1][1]=='X' || tab[1][1]=='T')
      if(tab[2][2]=='X' || tab[2][2]=='T')
        if(tab[3][3]=='X' || tab[3][3]=='T')
          return "X";
  if(tab[0][3]=='X' || tab[0][3]=='T')
    if(tab[1][2]=='X' || tab[1][2]=='T')
      if(tab[2][1]=='X' || tab[2][1]=='T')
        if(tab[3][0]=='X' || tab[3][0]=='T')
          return "X";
  return "";
}