#include <string>
#include <fstream>
#include <iostream>	
#include <vector>

using namespace std;
ifstream infile("input.in");
ofstream outfile("output.in");

bool solve(int X, int R, int C){
	int a,b;
	if(R<=C){
		a = R;
		b = C;
	}
	else{
		a = C;
		b = R;
	}
	switch(X){
		case 1:
			return true;
			break;
		case 2:
			switch(a){
				case 1:
					switch(b){
						case 2:
							return true;
							break;

						case 4:
							return true;
							break;

						default:
							return false;
							break;
					}
					break;
				case 2:
					switch(b){
						case 2:
							return true;
							break;
						case 3: 
							return true;
							break;
						case 4:
							return true;
							break;

						default:
							return false;
							break;
					}
					break;
				case 3:
					switch(b){
						case 4:
							return true;
							break;

						default:
							return false;
							break;	
					}
					break;

				case 4:
					switch(b){
						case 4:
							return true;
							break;
					}
					break;		
			}
			break;

		case 3:
			switch(a){
				case 1:
					return false;
					break;

				case 2:
					if(b == 3){
						return true;
					} else{
						return false;
					}
					break;
				case 3:
					if(b == 3 || 4) return true;
					return false;
					break;

				case 4:
					return false;
					break;
			}
			break;
		case 4:
			if(a == 3 || a == 4){
				if(b == 4) return true;
			}
			return false;
			break;

		default: return false;
	}

	return false;
}


int main(){
	int caseN = 1;
	int testCases;
	infile >> testCases;
	int Cases = testCases;
	while(Cases--){
		int X, R, C;
		infile >> X >> R >> C;
		bool tru = solve(X,R,C);
		string res;
		if(tru){
			res = "Gabriel";
		}
		else{
			res = "Richard";
		}


		outfile << "Case #" << caseN << ": " << res << endl;
		caseN++;
	}
	return 0;
}