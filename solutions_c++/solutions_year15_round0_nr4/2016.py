// Jai Mata Di
#include <iostream>
#include <vector>
using namespace std;
class BackgroundGrid{
	public:
	short r;
	short c;
	vector< vector <bool> > isCovered;
	BackgroundGrid(short r,short c){
		this->r = r;
		this->c = c;
	}
};
class Nomino{
	public:
	short n;
	short height;
	short width;
	vector< vector <bool> > isCovered;
};
class NominoSolver{
	int x;
	int r;
	int c;
	public:
	void input(){
		cin>>x>>r>>c;
	}
	string winner(){
		if(x == 1){
			return "GABRIEL";
		}else if (x == 2){
			if((r*c)%2==0){
				return "GABRIEL";
			}else{
				return "RICHARD";
			}
		}else if (x == 3){
			if ( ( (r == 2) && (c == 3)) 
			||   ( (r == 3) && (c == 2)) 
			||   ( (r == 3) && (c == 3)) 
			||   ( (r == 3) && (c == 4)) 
			||   ( (r == 4) && (c == 3))){
				return "GABRIEL";
			}
			else{
				return "RICHARD";
			}
			
		}else{
			if ( ( (r == 3) && (c == 4)) 
			||   ( (r == 4) && (c == 3)) 
			||   ( (r == 4) && (c == 4))){
				return "GABRIEL";
			}
			else{
				return "RICHARD";
			}
		}
	}
};
int main() {
	int noOfTestCases = 0;
	cin>>noOfTestCases;
	for(int testCaseNo=1;testCaseNo<=noOfTestCases;testCaseNo++){
		NominoSolver nominoSolver;
		nominoSolver.input();
		cout<<"Case #"<<testCaseNo<<": ";
		cout<<nominoSolver.winner()<<endl;
	}
	return 0;
}
