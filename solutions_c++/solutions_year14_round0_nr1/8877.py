#include <iostream>
#include <fstream>
//#include <sstream>
#include <string>
#include <vector>
#include <cstdlib>

//      cout << "Square: " << endl;
//      for (vector<int>::const_iterator i = square.begin(); i != square.end(); i++)
//	cout << *i << " ";

using namespace std;

int main(int argc, char* argv[]){
  int cases,n,j,k;
  string token;
  ifstream f(argv[1]);
  int volunteer, length;
  vector<int> square;
  vector<int> chosen;
  int result, hits;

  f >> token;
  cases = atoi(token.c_str());
  //for each case
  for(n = 1; n <= cases; n++){
    //two choices
    for(j = 1; j <= 2; j++){
      //get volunteer choice
      f >> token;
      volunteer = atoi(token.c_str());
      k = 1;
      //fill the square
      while( k <= 16 && f >> token) {
	square.push_back(atoi(token.c_str()));
	k++;
      }
      if (j == 1){
	//store chosen row
	for(int i = volunteer * 4 - 4; i < volunteer * 4; i++){
	  chosen.push_back(square[i]);
	} 

      }else{
	//find number from chosen in volunteer row
	hits = 0;
	for(int p = volunteer * 4 - 4; p < volunteer * 4; p++){
	  length = chosen.size();

	  for(int q = 0; q < length; q++){
	    if(square[p] == chosen[q]){
	      result = chosen[q];
	      hits ++;
	      break;
	    }
	  }
	  
	  if(hits == 2){
	    break;
	  }
	}
	cout << "Case #" << n << ": ";
	if (hits == 1){
	  cout << result << endl;
	}else if(hits == 2){
	  cout << "Bad magician!" << endl;
	}else if(hits == 0){
	  cout << "Volunteer cheated!" << endl;
	}
	chosen.clear();
      }
      square.clear();
    }
  }
  
}
