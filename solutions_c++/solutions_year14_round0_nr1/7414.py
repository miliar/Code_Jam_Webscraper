#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<fstream>

using namespace std;

void magic(int* arr1, int* arr2, int caseNum){
  int count = 0;
  int card = 0;
  for(int i = 0; i < 4; ++i){
    for(int j = 0; j < 4; ++j){
      if(arr1[i] == arr2[j]){
	card = arr1[i];
	count++;
      }
    }
  }
  cout << "Case #" << caseNum +1<< ": ";
  if(count == 0){
    cout << "Volunteer cheated!" << endl;
  }
  else if(count == 1){
    cout << card << endl;
  }
  else{
    cout << "Bad magician!" << endl;
  }
}

int main(){
  ifstream case1;
  int numCases = 0, arr1[4], arr2[4], rowNum = 0, tmp = 0; 
  string line;
  case1.open("A-small-attempt1.in");
  case1 >> numCases;
  
  for(int i = 0; i < numCases; ++i){
    case1 >> rowNum;
    for(int j = 0; j < 4; ++j){
      for(int k = 0; k < 4; ++k){
	case1 >> tmp;
	if((j+1) == rowNum){
	  arr1[k] = tmp;
	}
      }
    }
    case1 >> rowNum;
    for(int j = 0; j < 4; ++j){
      for(int k= 0; k < 4; ++k){
	case1 >> tmp;
	if((j+1) == rowNum){
	  arr2[k] = tmp;
	}
      }
    }
    magic(arr1, arr2, i);
  }
  case1.close();
  return 0;
}

