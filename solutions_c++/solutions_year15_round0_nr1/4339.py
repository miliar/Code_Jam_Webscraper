#include <iostream>

#include <vector>

using namespace std;

class ShynessPuzzleSolver{
	public:

	vector<int> shynessVector;

	int maxShynessLevel;
	
	int calculate(){
		int minReq = 0;
		int sum = 0;

		for(int i=0;i<shynessVector.size();i++){
			if(shynessVector[i] > 0){
				if(sum >= i){
					sum += shynessVector[i];
				}else{
					minReq += (i-sum);
					sum +=  ( (i-sum) + shynessVector[i] );
				}
			}
		}
		return minReq;
	}
};
int main() {
	int nT = 0;
	cin>>nT;
	for (int tC = 1; tC <= nT; tC++)
	{
		ShynessPuzzleSolver shynessPuzzleSolver;
		cin>>shynessPuzzleSolver.maxShynessLevel;
		for(int i=0;i<=shynessPuzzleSolver.maxShynessLevel;i++){
			char c;
			cin>>c;
			shynessPuzzleSolver.shynessVector.push_back(c-'0');
		}
		cout<<"Case #"<<tC<<": "<<shynessPuzzleSolver.calculate()<<endl;
	}
	return 0;
}
