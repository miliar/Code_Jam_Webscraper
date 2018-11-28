/*
 *  Bleatrix Trotter the sheep has devised a strategy that helps her fall asleep faster. First, she picks a number N. Then she starts naming N, 2 × N, 3 × N, and so on. Whenever she names a number, she thinks about all of the digits in that number. She keeps track of which digits (0, 1, 2, 3, 4, 5, 6, 7, 8, and 9) she has seen at least once so far as part of any number she has named. Once she has seen each of the ten digits at least once, she will fall asleep.

Bleatrix must start with N and must always name (i + 1) × N directly after i × N. For example, suppose that Bleatrix picks N = 1692. She would count as follows:

    N = 1692. Now she has seen the digits 1, 2, 6, and 9.
    2N = 3384. Now she has seen the digits 1, 2, 3, 4, 6, 8, and 9.
    3N = 5076. Now she has seen all ten digits, and falls asleep.

What is the last number that she will name before falling asleep? If she will count forever, print INSOMNIA instead. 
*INPUT: The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line with a single integer N, the number Bleatrix has chosen. 
* 1<=t<=100
* if output=0, print insominia 
*/


#include <cmath>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int testCaseNumber;
int lastNumberNamed;




int main(){

//input the given number of test cases and values
 int t, n;
 cin >> t;  // the number of test cases we are given
 int bigN [t];
  for (int i = 1; i <= t; i++) {
    cin >> n ;  //the bigN number
	bigN[i-1]=n;
  }
//once intCounter=counter, we know we are done
int counter[]={1,1,1,1,1,1,1,1,1,1};

//loop through and solve each piece
for(int i=0; i<t; i++){
bool stillAwake=true;
int mult=2;
int intCounter []={0,0,0,0,0,0,0,0,0,0};
int N=bigN[i];
 if(bigN[i]==0){
	cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
 }

else{
while (stillAwake){
int copyOfN=N;    
//put the intergers in the correct spot
    while(copyOfN!=0){
	int tempVar=copyOfN%10;
	if(intCounter[tempVar]==0){
	    intCounter[tempVar]=1;
	}
	copyOfN=copyOfN/10;
    }
    bool temp=true;
    for(int j=0; j<10;j++){
	if(intCounter[j]!=counter[j]){
		temp=false;
	}
    }
    if(temp){
	stillAwake=false;
    }
    else{
	N=bigN[i]*mult;
	mult++;
    }

 }


//final output
   cout<<"Case #"<<i+1<<": "<<N<<endl;
}
}
}





