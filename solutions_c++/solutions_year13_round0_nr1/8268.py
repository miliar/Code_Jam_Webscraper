// tic tac toe

#include<iostream>
using namespace std;

int main() {
    int t;
    cin>>t;
    for(int k=1; k<=t; k++) {
       char g[4][4];
       bool isComp=true, xWon=false, yWon=false;
       for(int i=0; i<4; i++){
           for(int j=0; j<4; j++) {
               cin>>g[i][j];
               if(g[i][j]=='.')
                  isComp=false;
           }
       }           
       
       // check rows
       for(int i=0; i<4; i++){
           char f; 
           
           if(xWon || yWon)
              break;
                 
           for(int j=0; j<4; j++) {
               if(j==0) {
                  if(g[i][j]!='T')
                     f=g[i][j];
                  else
                     f=g[i][j+1];   
               }
               else if(g[i][j]!=f && g[i][j]!='T') {
                  break;
               }
               else if(j==3) {
                  if(f=='X') {
                     xWon=true;
                     cout<<"Case #"<<k<<": X won\n";
                  } else if (f=='O') {
                     yWon=true;
                     cout<<"Case #"<<k<<": O won\n";
                  }                   
               }                       
           }
       }
       
       if(xWon || yWon)
              continue;
       
       // check colms
       for(int i=0; i<4; i++){
           char f; 
           
           if(xWon || yWon)
              break;
                 
           for(int j=0; j<4; j++) {
               if(j==0) {
                  if(g[j][i]!='T')
                     f=g[j][i];
                  else
                     f=g[j+1][i];   
               }
               else if(g[j][i]!=f && g[j][i]!='T') {
                  break;
               }
               else if(j==3) {
                  if(f=='X') {
                     xWon=true;
                     cout<<"Case #"<<k<<": X won\n";
                  } else if (f=='O') {
                     yWon=true;
                     cout<<"Case #"<<k<<": O won\n";
                  }                   
               }                       
           }
       }
       
       if(xWon || yWon)
              continue;
       
       // check diagonals
       for (int i=0; i<4; i++) {
           char f;
            if(i==0) {
                  if(g[i][i]!='T')
                     f=g[i][i];
                  else
                     f=g[i+1][i+1];   
               }
               else if(g[i][i]!=f && g[i][i]!='T') {
                  break;
               }
               else if(i==3) {
                  if(f=='X') {
                     xWon=true;
                     cout<<"Case #"<<k<<": X won\n";
                  } else if (f=='O') {
                     yWon=true;
                     cout<<"Case #"<<k<<": O won\n";
                  }     
               }              
       }
       
       if(xWon || yWon)
              continue;
              
       for (int i=0; i<4; i++) {
           char f;
            if(i==0) {
                  if(g[i][3-i]!='T')
                     f=g[i][3-i];
                  else
                     f=g[i+1][2-1];   
               }
               else if(g[i][3-i]!=f && g[i][3-i]!='T') {
                  break;
               }
               else if(i==3) {
                  if(f=='X') {
                     xWon=true;
                     cout<<"Case #"<<k<<": X won\n";
                  } else if (f=='O') {
                     yWon=true;
                     cout<<"Case #"<<k<<": O won\n";
                  }     
               }   
       }
       
       if(xWon || yWon)
              continue;
              
       if(isComp == false)
           cout<<"Case #"<<k<<": Game has not completed\n";
       else
           cout<<"Case #"<<k<<": Draw\n";             
              
              
       
    }
    return 0;
}
