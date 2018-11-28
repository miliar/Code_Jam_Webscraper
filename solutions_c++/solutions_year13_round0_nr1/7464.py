#include<iostream>
using namespace std;

int main(){

 int T,i,j,m,total;
 char tic[16];
 
 cin>>T;
 int flag=0;
 for(m=0;m<T;m++){
  flag=0;
  total=0;
  for(i=0;i<16;i++){
   cin>>tic[i];
  }
  //Row calculation 
  for(i=0;i<16;){
   total=0;
   for(j=0;j<4;j++){
    total=total+tic[i+j];
   }
   if((total=='X'*4) || (total==('X'*3 + 'T'))){
    cout<<"Case #"<<m+1<<": "<<"X won"<<endl;
    flag=1;
    break;
   }
   if((total=='O'*4) || (total==('O'*3 + 'T'))){
    cout<<"Case #"<<m+1<<": "<<"O won"<<endl;
    flag=1;
    break;
   }
   i=i+4;
  }
  if(flag)
   continue;
  //Column calculation
  for(i=0;i<4;i++){
   total=0;
   for(j=0;j<16;j+=4){
    total=total+tic[i+j];
   }
   if((total=='X'*4) || (total==('X'*3 + 'T'))){
    cout<<"Case #"<<m+1<<": "<<"X won"<<endl;
    flag=1;
    break;
   }
   if((total=='O'*4) || (total==('O'*3 + 'T'))){
    cout<<"Case #"<<m+1<<": "<<"O won"<<endl;
    flag=1;
    break;
   }
  }
  if(flag)
   continue;

 //back Diagonal calculation
   total=0;
   for(i=0;i<16;i++){
    total=total+tic[i];
    i+=4;
   }
   if((total=='X'*4) || (total==('X'*3 + 'T'))){
    cout<<"Case #"<<m+1<<": "<<"X won"<<endl;
    flag=1;
   }
   if((total=='O'*4) || (total==('O'*3 + 'T'))){
    cout<<"Case #"<<m+1<<": "<<"O won"<<endl;
    flag=1;
   }
  if(flag)
   continue;

 //Forward Diagonal calculation
   total=0;
   for(i=3;i<14;){
    total=total+tic[i];
    i=i+3;
   }
   if((total=='X'*4) || (total==('X'*3 + 'T'))){
    cout<<"Case #"<<m+1<<": "<<"X won"<<endl;
    flag=1;
   }
   if((total=='O'*4) || (total==('O'*3 + 'T'))){
    cout<<"Case #"<<m+1<<": "<<"O won"<<endl;
    flag=1;
   }
  if(flag)
   continue;

 //Draw and Not Completed
  total=0;
  for(i=0;i<16;i++){
   if(tic[i]=='.')
    total++;
  }
  if(total)
   cout<<"Case #"<<m+1<<": "<<"Game has not completed"<<endl;
  else
   cout<<"Case #"<<m+1<<": "<<"Draw\n";
  flag=1;
 }

 return 0;
}
