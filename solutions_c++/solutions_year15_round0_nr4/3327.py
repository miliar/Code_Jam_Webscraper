

#include<iostream>
using namespace std;

int check(int, int, int);

int two_omino(int X,int R,int C) {
  if ((R*C)%2!=0) return 1;
  return 0;
}
int three_omino(int X,int R,int C)
{
  if((R==2 && C==3)||(R==3 && C==2)) return 0;
  else if((R==3 && C==4)||(R==4 && C==3)) return 0;
  else if(R==3 && C==3) return 0;
  else
    return 1;
}
int four_omino(int X,int R,int C)
{
  if((R==3 && C==4)||(R==4 && C==3)) return 0;
  else if(R==4 && C==4) return 0;
  else
    return 1;
}


int main() {
  int omino, row ,flag , col, i,cases;
  cin >> cases;
  for(int i=0;i< cases;) {
    flag=0;
    cin >> omino >> row >> col ;
    switch( omino )  {
    case 1: break; 
    case 2: flag=two_omino(omino,row,col);  break;
    case 3: flag=three_omino(omino,row,col);break;
    case 4: flag=four_omino(omino,row,col); break;
    default:flag=1;        break;
    }
    cout << "Case #" << ++i << ": " << ((flag)? "RICHARD":"GABRIAL") << endl;   
  }
}

