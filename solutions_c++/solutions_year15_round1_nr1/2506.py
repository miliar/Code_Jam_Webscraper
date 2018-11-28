#include <iostream>
#include <vector>
using namespace std;

void solve(int testNum);
int solve1(vector<int> plate);
int solve2(vector<int> plate);
int main(){
	int testCase;
	int plateNum;
	cin >> testCase;
	vector<int> plate;


	for(int i=0; i<testCase; i++){
		solve(i+1);
	}

	return 0;
}
void solve(int testNum){

	int plateNum;
	int tmp;
	vector<int> plate;

	cin >> plateNum;

	for(int i=0; i<plateNum; i++){
		cin>>tmp;
		plate.push_back(tmp);
	}

	int result1 = solve1(plate);
	int result2 = solve2(plate);

	cout<< "Case #" << testNum << ": " << result1 << " " << result2 << endl;

}

int solve1(vector<int> plate){
	int ate=0;
	for(int i=1; i<plate.size(); i++){
		if( plate.at(i)< plate.at(i-1))
			ate+= ( plate.at(i-1) - plate.at(i) );
	}
	return ate;
}
int solve2(vector<int> plate){
	int max=0;
	int result=0;
	for(int i=1; i<plate.size(); i++){

		if( plate.at(i) < plate.at(i-1)){
			
			int ate= ( plate.at(i-1) - plate.at(i) );
			if( ate > max )
				max = ate;
		}
	}

	for(int i=0; i<plate.size()-1; i++){
		if( plate.at(i) < max )
			result += plate.at(i);
		else
			result += max;

	}

	return result;
}
