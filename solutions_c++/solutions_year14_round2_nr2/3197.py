#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;

int main () {   
  char file1[100]; sprintf(file1, "output.txt");     ofstream parOP(file1);

  
     int *B_digit=new int [11];
   int *A_digit=new int [11];
   int *result=new int [11];
   int *K_digit=new int [11];
   
  ifstream input;
  input.open("B-small-attempt0.in");
  
  int number_test;
    input >> number_test;
    cout<<" number_test "<<number_test<<endl;

  
  for (int k=0;k<number_test;k++) {

      int A2, B2, K,A1,B1,A=1,B;
      input >> A1>>B1>>K;

cout<<"Here "<<A/2<<endl;
    int stract =0;
    int sum = 0;
    	int i=0,ii=0;
 for (B2=B1-1;B2>=0;B2--){
   for (A2=A1-1;A2>=0;A2--){
for (i=0; i<11;i++){B_digit[i]=0;A_digit[i]=0;}
   B=B2;A=A2;
        if(k==1){
	cout << "A "<<A<<" B "<<B;}
   if (B==0){ for (i=0; i<11;i++){B_digit[i]=0;}}
      if (A==0){ for (i=0; i<11;i++){A_digit[i]=0;}}
     ii=0;
	while(B>0){

 	  B_digit[ii]=B%2;
 	  B=(B-B%2)/2;
 	  ii++;
 	}
// 	
	ii=0;
      while(A>0){
	  A_digit[ii]=A%2;
	  A=(A-A%2)/2;   
	  ii++;
	}
	    int resulttt= 0;
  if (A2==1&&B2==1){ for (int j=0; j<11;j++){cout<<B_digit[j]<<" Wow";}}
    for (int j=0; j<11;j++){result[j]=0;
      result[j]=(A_digit[j]*B_digit[j]);
    if (A2==1&&B2==1){
      cout<<" "<<A_digit[j]<<"*"<<B_digit[j]<<endl;
    }

      resulttt+=result[j]*pow(2,j);
    }
//      if(k==1){
// 	cout <<" result "<<resulttt<<endl;}
	
    if(resulttt<K){
      sum=sum+1;
     if(k==1){
	cout <<" result "<<resulttt<<endl;}
    }
  } 
 }
//       

	  cout<< "Case #" << k+1 << ": " << sum<<endl;
	  parOP<< "Case #" << k+1 << ": " << sum<<endl;
       }

  input.close();
  return 0;
}






/*     
 *
 *    vector<int> mote_sizes;
 *
 *
 *	
 *	 input >> temple;
      mote_sizes.push_back(temple);
    }
    
   sort(mote_sizes.begin(),mote_sizes.end());
   
	     mote_sizes.erase(mote_sizes.begin());
	     
	 
	if ( Armin_size<=mote_sizes[0] ) {

	  if ( Armin_size>1 && n1<=mote_sizes.size()){

	    mote_sizes.erase(mote_sizes.begin()); 
*/




/*      
 * int ** win = new int* [number_players];
	for (int i=0; i<number_players; i++)
	  {
	    win[i] = new int [number_players];  
	}
	*/