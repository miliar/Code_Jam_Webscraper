#include<iostream.h>
#include<stdio.h>
#include<conio.h>

const int Smax=6;

int getDigits(char string[],int arr[]){
 int no=0,i,j;
 for(i=0;string[i]!=' ';i++){
  no=no*10+(string[i]-'0');
 }
 for(j=0;j<=no;j++){
  arr[j]=string[++i]-'0';
 }
 return no;
}

int main(){
 int T,count=0,ans[100];
 cin>>T;
 while(count<T){
  int smax;
  int array[Smax+1];
  int people=0;
  int invite=0,curr_invite=0;
  char string[Smax+5];
  gets(string);
  smax=getDigits(string,array);
  for(int i=0;i<=smax;i++){
   if(people>=i){
    people+=array[i];
   }
   else{
    curr_invite=i-people;
    invite+=curr_invite;
    people+=curr_invite;
   }
  }
  ans[count++]=invite;
 }
 for(int i=0;i<T;i++)
  cout<<"Case #"<<(i+1)<<": "<<ans[i]<<endl;
 getch();
 return 0;
}
