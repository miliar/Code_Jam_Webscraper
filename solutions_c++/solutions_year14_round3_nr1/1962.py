#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;

int if_pow2(int N){
int flag = 1;
int ratio=N;
if (ratio==1){
  flag = 0;
  return flag;
}
while (ratio>1){
  //cout << "ratio "<<ratio<<endl;
  if (ratio%2==0){
    //cout<< " here "<<endl;
    ratio=ratio/2;
  }
  if (ratio%2==1&&ratio>1){
  //      cout<< " herereere "<<endl;
    flag = 0;
    break;
  }
}
  return flag;
}

int main () {   
     // cout<<" test "<<if_pow2(4)<<endl;

  char file1[100]; sprintf(file1, "output.txt");     ofstream parOP(file1);

  ifstream input;
  input.open("A-small-attempt1.in");
  
  int number_test;
    input >> number_test;
    cout<<" number_test "<<number_test<<endl;

  
      for (int k=0;k<number_test;k++) {
	int result = 0;
    int upper = 0, lower = 0;
    double percentage = 0.0;
    char slash;
    input >>upper>>slash>>lower;

    percentage = (double)upper/lower;
   // cout<< upper <<" "<<lower<<" " <<percentage<<endl;
    int flag = 0;	

    if (lower%upper==0){
  //    cout << "here"<<endl;
      flag = 1;
     int ratio = lower/upper;
      while (ratio >1){
//	cout<< "ratio"<<ratio<<endl;
	ratio = ratio /2;
	result += 1;
      }
    }
   if (lower%upper!=0 && (if_pow2(lower))){
    // cout<< " Oh , here"<<endl;
     flag = 1;
     int power = 0;
     while(pow(2,power)*upper<lower){
   //    cout<< " power "<<power<<endl;
       power=power+1;
    }
    result= power;
  }
   if (flag == 1) {
	  cout<< "Case #" << k+1 << ": " << result<<endl;
	  parOP<< "Case #" << k+1 << ": " << result<<endl;
   }
    if(flag == 0) {
       //     cout << "here-mygod"<<endl;

      	  cout<< "Case #" << k+1 << ": " << "impossible"<<endl;
	  parOP<< "Case #" << k+1 << ": " << "impossible"<<endl;
    }
      
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