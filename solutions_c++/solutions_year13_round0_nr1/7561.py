#include<iostream>
#include<conio.h>
#include<stdlib.h>

using namespace std;
int check(char &win) {
   int flag=0;
  // char win;
   char arr[4][4];
   char temp;
  
   for(int i=0;i<4;i++)
	   for(int j=0;j<4;j++)
		   cin>>arr[i][j];

   for(int i=0;i<4;i++) {
	   
       int flag1=0;
	   for(int j=0;j<4;j++) {
		   flag=0;
		 if(j==0||temp=='T'){
			 
			 temp=arr[i][j];
			 if(temp=='T')
				 flag1++;
		 }
		 if(temp=='.') {
			 cout<<"Yes";
			 flag=2;break;}
		 if(arr[i][j]==temp)//&&temp!='.')
			 continue;
		 if(arr[i][j]=='T'&&flag1==0) {
			   flag1++;
			 continue;
            
		 }
		// else {
		//cout<<"Weird";
			  flag=2;
			 break;
				
		 //}
	   }
	   if(flag!=0) {
		   //cout<<"Yes";
	   flag1=0;
	   flag=0;
		 for(int j=0;j<4;j++) {
		 if(j==0||temp=='T'){
			
			 temp=arr[j][i];
			  if(temp=='T')
				 flag1++;
		 }
		 if(temp=='.'){
			 flag=2;
			 break;
		 }
		 if(arr[j][i]==temp&&temp!='.')
			 continue;
		  if(arr[j][i]=='T'&&flag1++==0)
			 continue;
		
			 flag=2;
			 break;
		     
		 
	   }
	  }
       
	   

	   if(flag==0) {
		   win=temp;
		   //cout<<"Yes";
		   break;
		  // cout<<"Yes";
	   }
	   
   }
   int flag1;
   if(flag!=0) {
	  // cout<<"Yes";
   char temp1=arr[0][0];
   
			 if(temp1=='O'||temp1=='X'||temp1=='T'){
				 flag1=0;
				 if(temp1=='T')
					 flag1++;
   
		 
			 flag=0;
	   for(int i=0;i<4;i++){
		 for(int j=0;j<4;j++) {
		 if(i==j){
		 
		 if(arr[i][j]==temp1&&temp1)
			 continue;
		 if(arr[i][j]=='T'&&flag1++==0)
			 continue;
		 else {
			 flag=2;
			 break;
		     
		  }
		 }
		 }
		 if(flag==2)
			 break;
	   }
		win=temp1;
 }
   }
if(flag!=0) {
	//cout<<"Yes";
   char temp1=arr[0][3];
  
    if(temp1=='O'||temp1=='X'||temp1=='T'){
		flag1=0;
		if(temp1=='T')
			flag1++;
		
	flag=0;
		 
		for(int i=0;i<4;i++){
		 for(int j=0;j<4;j++) {
		 if(i==3-j){
		 
		 if(arr[i][j]==temp1)
			 continue;
		  if(arr[i][j]=='T'&&flag1++==0)
			 continue;
		 else {
			 flag=2;
			 break;
		     
		  }
		 }}
		 if(flag==2)
			 break; 
	   }
		  
		win=temp1; }
}

 if(flag !=0){
	 //cout<<"reach";
	 for(int i=0;i<4;i++) {
		for(int j=0;j<4;j++) {
		 if(arr[i][j]=='.') {
			 flag=2;
			 break;
		 }
		 else
			 flag=1;
	    }
		if(flag==2)
			break;
	 }
 }
	return flag;
	
}

void main() {
  int T;
  char win;
  cin>>T;
  int arr[1000];
  char arr1[1000];
  for(int i=0;i<T;i++){
	  arr[i]=check(win);
	  arr1[i]=win;
  }
  system("cls");
  for(int i=0;i<T;i++){
	  cout<<"Case #"<<i+1<<": ";
	  int flag=arr[i];
	  if(flag==0) 
		cout<<arr1[i]<<" won"<<endl;
	else if(flag==1)
		cout<<"Draw"<<endl;
	else if(flag==2)
		cout<<"Game has not completed"<<endl;
  }
  getch();
  getch();
}

   
