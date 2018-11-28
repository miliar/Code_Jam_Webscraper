#include <iostream>
#include<conio.h>

using namespace std;

int check() {
	int check1[100][100];
	int a=0;
	int k=0;
	int possible=1;
	int arr[100][100];
	//int arr2[100][100];
	int arr1[100];
	int arr3[100];
	int arr4[100][100];
	int N,M;
	cin>>N>>M;
	int flag=1;
	for(int i=0;i<N;i++)
		for(int j=0;j<M;j++)
			cin>>arr[i][j];
	//////////////////////
	int temp;
	int flags=1;
	int checkin=1;
	for(int i=0;i<N;i++){
		temp=arr[i][0];
		for(int j=0;j<M;j++) {
			
			if(arr[i][j]==temp){
				
				//if(arr[i][j]>temp)
					//temp=arr[i][j];
				//if(j==M-1)
					//arr1[k++]=1;
				//check1[i][j]=1;
				continue;
			}
			else {
				checkin=0;
			    goto b;
			}
		}
		b: 	// if((arr[i][j]<temp)||j==0){
				//cout<<j;
				//temp=arr[i][j];
		if(checkin==0) {
				for(int q=0;q<M;q++)
				 for(int k=0;k<N;k++)
					if(arr[k][q]<=arr[i][q])  {
				      flags=1;
					  
					  continue;
					}
					else {flags=0; goto a;}
					
				checkin=1;
		
		}
			//arr1[k++]=0;
			//goto a;
	   }

   


	/*for(int i=0;i<N;i++)
		for(int j=0;j<M;j++)
			if(arr1[i]==0)
				if(arr[i][0]==2 && arr[i][N-1]==2 && (i==0 ||i==N-1))
					arr1[i]=1;
	/*for(int i=0;i<N;i++)
		cout<<arr1[i];*/
	//int check=0;
	//int i,j;
	///////////////////////
 /* for(i=0,k=0;i<N;i++){
	 /* if(check==1){
		  k--;
		  check=0;
	  } 
	  //cout<<arr1[i]+" ";
	  if(arr1[i]==0) {
		  //cout<<arr1[k];
		 check=1;
		  a++;
	   for(int j=0;j<M;j++){
		   //int temp=arr[i][j];
		   arr2[k][j]=arr[i][j];
		   
		   }
	   k++;
	  
	  } */
  

      
		  
/*
////////////////////////////
  //////////////////////
  int o=0;
	for(int i=0;i<M;i++){
		for(int j=0;j<N;j++) {
			temp=arr[0][i];
			if(arr[j][i]==temp){
				if(j==N-1)
					arr3[o++]=1;
				continue;
			}
			arr3[o++]=0;
			break;
	   }

   } 
	
	//system("cls");
	//cout<<o;
	
	/*
	int b=0;
	for(int i=0;i<o;i++)
		cout<<arr3[i];
	//int check=0;
	//int i,j;
	///////////////////////
  for(int j=0;j<M;j++) {
	 
	  //cout<<arr1[i]+" ";
	  if(arr3[j]==0) {
		  //cout<<arr1[k];
		 check=1;
	   for(i=0,k=0;i<a;i++){
		   //int temp=arr[i][j];
		   //arr4[j][j]=arr2[j][i];
		   
		   }
	   k++;
	   b++;
	    //cout<<a<<" "<<b;
	  } */
  
            
		  

////////////////////////////
	//system("cls");

//cout<<endl<<b<<endl;
  //for(int i=0;i<a;i++){
	//  for(int j=0;j<b;j++)
		//	cout<<arr4[i][j]<<" ";
			
			//cout<<endl;


  //if(a==0||b==0)
	//  return 1;
 // else
	 // return 0;
	/*for(int i=0;i<N;i++)
		for(int j=0;j<M;j++)
			if(arr3[i]==0)
				if(arr[0][i]==1 && arr[M-1][i]==1)
					arr3[i]=1; */
	//for(int i=0;i<o;i++)
      //cout<<arr3[i]<<" ";
	/////////////////
	/*for(int i=0;i<N;i++)
		for(int j=0;j<M;j++){
			if(arr1[i]==1)
				check1[i][j]=1;
			else 
				check1[i][j]=0;
		    
		}
		
	for(int i=0;i<M;i++)
		for(int j=0;j<N;j++)
			if(check1[j][i]==0)
			 if(arr3[i]==1)
				check1[j][i]=1;
		*/
	////////////////
	/*int flag1=1;
	for(int i=0;i<N;i++)
		for(int j=0;j<M;j++)
		 if (check1[i][j]==0) {
			 
			flag1=0;
			break;
		 }
		
	*/
	

a: return flags;
}
void main() {
 int arr[101];
 int T;
 cin>>T;
 for(int i=0;i<T;i++)
	 arr[i]=check();
 system("cls");
 for(int i=0;i<T;i++)
	 if(arr[i]==1)
		 cout<<"Case #"<<i+1<<": YES"<<endl;
	 else 
		  cout<<"Case #"<<i+1<<": NO"<<endl;

 getch();
} 