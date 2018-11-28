#include <fstream>
#include <iostream>
#include <string>
#include <set>
#include <vector>
#include <sstream>
#include <stack>
#include <algorithm>

using namespace std;

int main(int argc, char *argv[]){

  ifstream fs(argv[1]);
  int T,N;
  long eaten,max,x;
  string s;
  vector<long> mm;


  getline(fs, s);
  istringstream(s) >> T;
  for(int i = 0; i < T; i++){
	  getline(fs, s);
	  istringstream(s) >> N;
	  getline(fs, s);
	  istringstream is(s);
	  mm.clear();
	  cout << "Case #" << i+1 << ": ";
	  for(int j = 0; j < N; j++){
		  is >> x;
		  mm.push_back(x);
	  }
	  //method 1
	  eaten = 0;
	  for(int j = 1; j < N; j++)
		  if(mm[j] < mm[j-1]) eaten += (mm[j-1]-mm[j]);
	  cout << eaten << " ";

	  //method 2
	  max = 0;
	  eaten = 0;
	  for(int j = 1; j < N; j++)
		  if ((mm[j-1] - mm[j]) > max) max = mm[j-1]-mm[j];
	  for(int j = 0; j < N-1; j++)
		  eaten+= mm[j] < max ? mm[j] : max;
	  cout << eaten << endl;

	  }
}
