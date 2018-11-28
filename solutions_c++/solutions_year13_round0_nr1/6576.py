#include<stdio.h>
#include<iostream>
using namespace std;
  char a[4][4],temp[4];
  int flag=0;
void checkH(char xo){
  for(int i=0;i<4;i++){   
    if((a[i][0]==xo||a[i][0]=='T')&&
    (a[i][1]==xo||a[i][1]=='T')&&
    (a[i][2]==xo||a[i][2]=='T')&&
    (a[i][3]==xo||a[i][3]=='T')){
      {
        cout<<xo<<" won";
        flag=1;
      }
    }
  }
}  
void checkV(char xo){
  for(int i=0;i<4;i++){   
    if((a[0][i]==xo||a[0][i]=='T')&&
    (a[1][i]==xo||a[1][i]=='T')&&
    (a[2][i]==xo||a[2][i]=='T')&&
    (a[3][i]==xo||a[3][i]=='T')){
      {
        cout<<xo<<" won";                         
        flag=1;
      }
    }
  }
} 
void checka(char xo){
    if((a[0][0]==xo||a[0][0]=='T')&&
    (a[1][1]==xo||a[1][1]=='T')&&
    (a[2][2]==xo||a[2][2]=='T')&&
    (a[3][3]==xo||a[3][3]=='T')){
      {
        cout<<xo<<" won";                         
        flag=1;
      }
    }
}  
void checkb(char xo){
    if((a[0][3]==xo||a[0][3]=='T')&&
    (a[1][2]==xo||a[1][2]=='T')&&
    (a[2][1]==xo||a[2][1]=='T')&&
    (a[3][0]==xo||a[3][0]=='T')){
      {
        cout<<xo<<" won";                         
        flag=1;
      }
    }
}  
void checkcomplete(){
  int k=0;   
  if(flag==0){ 
    for(int i=0;i<4;i++){
      for(int j=0;j<4;j++){
        if(a[i][j]=='.'){
          k=1;
          break;
        }  
      }
    }
    if(k==1){
      cout<<"Game has not completed";                          
      flag=1;
    }     
  }     
}
void check(){
  checkH('X');
  if(flag==0){
    checkH('O');
    if(flag==0){
      checkV('X');
      if(flag==0){
        checkV('O');
        if(flag==0){
          checka('X');
          if(flag==0){
            checka('O');
            if(flag==0){
              checkb('X');
              if(flag==0){
                checkb('O');  
                if(flag==0){
                  checkcomplete();
                }
              }  
            }  
          }
        }
      }
    }
  }
  if(flag==0){
    cout<<"Draw";          
  }
}
int main(void)
{
  int round;
  cin >> round;
  for(int j=0;j<round;j++){
      cin>>a[0][0]; 
      cin>>a[0][1];
      cin>>a[0][2];
      cin>>a[0][3];
      
      cin>>a[1][0]; 
      cin>>a[1][1];
      cin>>a[1][2];
      cin>>a[1][3];
      
      cin>>a[2][0]; 
      cin>>a[2][1];
      cin>>a[2][2];
      cin>>a[2][3];
      
      cin>>a[3][0]; 
      cin>>a[3][1];
      cin>>a[3][2];
      cin>>a[3][3];
      //cin>>temp;
      cout <<"Case #"<<j+1<<": ";
      check();
      cout<<endl;
      flag=0;
      
  }
  return 0;
}
