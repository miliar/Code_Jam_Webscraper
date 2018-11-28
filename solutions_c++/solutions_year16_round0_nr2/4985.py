/*
 *  he Infinite House of Pancakes has just introduced a new kind of pancake! It has a happy face made of chocolate chips on one side (the "happy side"), and nothing on the other side (the "blank side").

You are the head waiter on duty, and the kitchen has just given you a stack of pancakes to serve to a customer. Like any good pancake server, you have X-ray pancake vision, and you can see whether each pancake in the stack has the happy side up or the blank side up. You think the customer will be happiest if every pancake is happy side up when you serve them.

You know the following maneuver: carefully lift up some number of pancakes (possibly all of them) from the top of the stack, flip that entire group over, and then put the group back down on top of any pancakes that you did not lift up. When flipping a group of pancakes, you flip the entire group in one motion; you do not individually flip each pancake. Formally: if we number the pancakes 1, 2, ..., N from top to bottom, you choose the top i pancakes to flip. Then, after the flip, the stack is i, i-1, ..., 2, 1, i+1, i+2, ..., N. Pancakes 1, 2, ..., i now have the opposite side up, whereas pancakes i+1, i+2, ..., N have the same side up that they had up before. 

*/


#include <cmath>
#include <iostream>
#include <string>
#include <algorithm>
#include <queue>  
#include <vector>

using namespace std;

int testCaseNumber;
int lastNumberNamed;




int main(){

//input the given number of test cases and values
 int t;
 string n;
 cin >> t;  // the number of test cases we are given
queue<vector<int> > totalStacks;
  for (int i = 1; i <= t; i++) {
    cin >> n ; 
	int theLength=n.size();
	vector<int> tempVector (theLength);
  	for(int j=0; j<theLength;j++){
	  if(n[j]=='+'){
		tempVector.at(j)=1;
		}
	}
	totalStacks.push(tempVector);
  }
for(int i=0; i<t;i++){
vector<int> pancake=totalStacks.front();
totalStacks.pop();
int sizeOfStack=pancake.size();
int flips=0;
bool notCorrectlyFlipped=true;

while(notCorrectlyFlipped){
	int wrong=pancake[0];
	int counter=1;
	//we know how far we must flip
	while(wrong==pancake[counter]&&counter!=sizeOfStack){
		counter++;
	}
	if(counter==sizeOfStack && wrong==1){
		//final output
   		cout<<"Case #"<<i+1<<": "<<flips<<endl;
		notCorrectlyFlipped=false;
	}
	else{
		for(int j=0; j<counter; j++){
			pancake[j]=(pancake[j]+1)%2;
		}
		flips++;
	}
}


 }
}


