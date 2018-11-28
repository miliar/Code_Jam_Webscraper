#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
using namespace std;

int StrToInt( const string& s ){
  int result;
  std::istringstream ss( s );
  ss >> result;
  if (!ss) throw std::invalid_argument( "StrToInt" );

  return result;
 }

int main() {
	bool DEBUG = false;
	int fairSquares[] = {1, 4, 9, 121, 484};
	int cases;
	cin >> cases;
	for(int i = 0; i < cases; i++){
		string A, B;
		cin >> A;
		cin >> B;
		if(DEBUG){
			cout << "A=" << A << " B=" << B << endl;
		}
		int min = StrToInt(A);
		int max = StrToInt(B);
		int fairSquareNum = 0;
		for(int j = 0; j <= 4; j++){
			if((fairSquares[j] >= min) && (fairSquares[j] <= max)){
				if(DEBUG){
					cout << fairSquares[j] << " is fair square!" << endl;
				}
				fairSquareNum++;
			}
		}
		cout << "Case #" << i+1 << ": " << fairSquareNum << endl;
	}

	return 0;
}
