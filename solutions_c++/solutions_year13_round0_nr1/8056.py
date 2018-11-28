#include<iostream>

using namespace std;

int main()
{
  int tes,cases;
  int i,j,trow,tcol;
  char mat[4][4]; 
  bool isEmpty;
  bool isFound;
  char curr;
  char option[3]="X0";

  cin>>tes;

  for(cases=1; cases<=tes; cases++) {
   
    isEmpty = false;
    isFound = false;
    for(i=0; i<4; i++) {
     for(j=0; j<4; j++) {
      cin>>mat[i][j];
      
      if(mat[i][j] == 'T'){
        trow = i;
        tcol =j;
      }
      
      if(mat[i][j] == '.')
        isEmpty = true;
             
     }
    }
    
    ////////////////////////////////////////////
    //////////////////case1/////////////////////
    ////////////////////////////////////////////


    //case1: replace 'T' with 'X'
    mat[trow][tcol] = 'X';
    
    //check row-wise
    for(i=0; i<4; i++) {
     curr = mat[i][0];
     if(curr == mat[i][1] && curr == mat[i][2] && curr == mat[i][3] && curr != '.')
     {
       isFound = true;
       break;
     }
    }

    if(isFound == true)
    {
      cout<<"Case #"<<cases<<": "<<curr<<" "<<"won"<<endl;
      continue;
    }

    //check col-wise
    for(i=0; i<4; i++) {
     curr = mat[0][i];
     if(curr == mat[1][i] && curr == mat[2][i] && curr == mat[3][i] && curr != '.')
     {
       isFound = true;
       break;
     }
    }

    if(isFound == true)
    {
      cout<<"Case #"<<cases<<": "<<curr<<" "<<"won"<<endl;
      continue;
    }


    //check in main diagonal
     curr = mat[0][0];
     if(curr == mat[1][1] && curr == mat[2][2] && curr == mat[3][3] && curr != '.')
     {
       isFound = true;
       cout<<"Case #"<<cases<<": "<<curr<<" "<<"won"<<endl;
       continue;
     }
 
     //check in other diagonal
     curr = mat[0][3];
     if(curr == mat[1][2] && curr == mat[2][1] && curr == mat[3][0] && curr != '.')
     {
       isFound = true;
       cout<<"Case #"<<cases<<": "<<curr<<" "<<"won"<<endl;
       continue;
     }
    
     ////////////////////////////////////////////////////////////
     //////////////////case 2////////////////////////////////////
     ////////////////////////////////////////////////////////////
 
     //case2: replace 'T' with 'O'
    mat[trow][tcol] = 'O';
    
    //check row-wise
    for(i=0; i<4; i++) {
     curr = mat[i][0];
     if(curr == mat[i][1] && curr == mat[i][2] && curr == mat[i][3] && curr != '.')
     {
       isFound = true;
       break;
     }
    }

    if(isFound == true)
    {
      cout<<"Case #"<<cases<<": "<<curr<<" "<<"won"<<endl;
      continue;
    }

    //check col-wise
    for(i=0; i<4; i++) {
     curr = mat[0][i];
     if(curr == mat[1][i] && curr == mat[2][i] && curr == mat[3][i] && curr != '.')
     {
       isFound = true;
       break;
     }
    }

    if(isFound == true)
    {
      cout<<"Case #"<<cases<<": "<<curr<<" "<<"won"<<endl;
      continue;
    }


    //check in main diagonal
     curr = mat[0][0];
     if(curr == mat[1][1] && curr == mat[2][2] && curr == mat[3][3] && curr != '.')
     {
       isFound = true;
       cout<<"Case #"<<cases<<": "<<curr<<" "<<"won"<<endl;
       continue;
     }
 
     //check in other diagonal
     curr = mat[0][3];
     if(curr == mat[1][2] && curr == mat[2][1] && curr == mat[3][0] && curr != '.')
     {
       isFound = true;
       cout<<"Case #"<<cases<<": "<<curr<<" "<<"won"<<endl;
       continue;
     }


     //draw or incomplete
     if(isEmpty == true) {
       cout<<"Case #"<<cases<<": "<<"Game has not completed"<<endl;
     } else {
       cout<<"Case #"<<cases<<": "<<"Draw"<<endl;
     }

  }
 
 return 0;
}
