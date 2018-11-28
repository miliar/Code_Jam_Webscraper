#include <cstdio>
#include <iostream>

using namespace std;


char b[4][4];

bool emptycell()
{
  int i,j;
  for(i=0;i<4;i++)
    for(j=0;j<4;j++)
      if(b[i][j]=='.')return true;
  return false;
}

bool won(char p)
{
  int i,j,k;

  // check for rows
  for(i=0;i<4;i++)
    if(b[i][0]==p and b[i][1]==p and b[i][2]==p and b[i][3]==p) return true;
  
  // check for columns
  for(i=0;i<4;i++)
    if(b[0][i]==p and b[1][i]==p and b[2][i]==p and b[3][i]==p) return true;

  // check for diagnols
  if((b[0][0]==p and b[1][1]==p and b[2][2]==p and b[3][3]==p) or
     (b[0][3]==p and b[1][2]==p and b[2][1]==p and b[3][0]==p)) return true;
  
  // check for 3 symbols and a  T
  bool tp=false;
  int pc=0;
  for(i=0;i<4;i++){
    for(j=0;j<4;j++){
      if(b[i][j]=='T')tp=true;
      if(b[i][j]==p)++pc;
    }
  }
  if(tp and pc==3) return true;
  return false;
}

int main()
{
  int i,j,k,t,cs=1;
  scanf("%d", &t);

  while(t--){

    for(i=0;i<4;i++)scanf("%s", b[i]);

    if(won('O')) printf("Case #%d: O won\n", cs++);
    else if(won('X'))printf("Case #%d: X won\n", cs++);
    else if(emptycell()) printf("Case #%d: Game has not completed\n", cs++);
    else printf("Case #%d: Draw\n", cs++);
  }

  return 0;
}
