// the stream extraction operator variation of cin
#include <iostream>
using namespace std;
 


int main(void)
{
  int x, y,z,compare;
  int firstline[4];
  int result,number=0;
  int i=0;
  cin>>x;

  while (i<x){
    i++;
    cin>>y;
    for (int j=1;j<=4;j++){
	  if (y==j){	
        for (int f=0;f<4;f++){
	      cin>>firstline[f];
	     }
	   }
	   else{
	     for (int f=0;f<4;f++){
	      cin>>z;
	     }}
	   }
	 
	 cin>>y;
    for (int j=1;j<=4;j++){
	  if (y==j){	
        for (int f=0;f<4;f++){
	      cin>>compare;
	     
	      for (int k=0;k<4;k++){
			  if (compare==firstline[k]){
				
				  number++;
				  result=compare;
			   }
		  }
	     }
	    }
	     else{
	     for (int f=0;f<4;f++){
	      cin>>z;
	     }}
	   }
	 if (number==1)
	   cout<<"Case #"<<i<<": "<<result<<endl;
	 if (number>1)
	   cout<<"Case #"<<i<<": Bad magician!"<<endl;
	 if (number==0)
	   cout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
	 number=0;

	  
  }
  
  return 1;
}
