#include <iostream>
#include <fstream>
#include <math.h>


using namespace std;


bool isP(long long num){
  long long pow = 1;
  long long temp = num;
  while(temp /= 10){
    pow *= 10;
  }
  if(pow == 1)
    return true;
  
  int left, right;
  while(pow != 0){
    left = num / pow;
    right = num % 10;
    if(left != right)
      return false;
    num %= pow;
    num /= 10;
    pow /= 100;
  }

  return true;
}
int main(int argc, char ** argv){
  ifstream inputFile;
  ofstream outputFile("output");
  if(argc < 2){
    cout << "Usage : " << argv[0] << " s/l" << endl;
    return 0;
  }
  
  if(argv[1][0] == 's'){
    inputFile.open("small");
  }else{
    inputFile.open("large");
  }

  if(inputFile.is_open() && outputFile.is_open()){
    int gameCount;
    string line;
    
    inputFile >> gameCount; 
    getline(inputFile, line);

    for(int i = 1; i <= gameCount; i++){
      string result;
      long long low, high;
      inputFile >> low;
      inputFile >> high;
      cout <<  low << " ------ " << high << endl;
      long long root = (long long) sqrt(low);
      getline(inputFile, line);
      long long square = root * root;
      long long count = 0;
      if(square < low){
	root++;
	square = root * root;
      }
	
      while(square <= high){
	if(isP(root) && isP(square)){
	  count++;
	  cout << " root = " << root << endl;
	  cout << " sqaure = " << square << endl;
	}
	root++;
	cout << " root " << root << endl;
	square = root * root;
      }
      cout << "Case #" << i << ": " << count << endl;
      outputFile << "Case #" << i << ": " << count  << endl;
    }
  }else{
    cout << "Can't open file" << endl;
  }



  return 0;
}

