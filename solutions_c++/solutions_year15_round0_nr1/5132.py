#include <iostream>
#include <vector>


using namespace std;

void getResult(int caseNum);

int main(){

	int sum;
	int testCase;

	cin >> testCase;

	for(int i=0; i<testCase; i++){
		getResult(i+1);
	}



	return 0;
}
void getResult(int caseNum){
	int S;
	string stream;
	int tmp;
	int sum = 0;
	int result = 0;
	vector<int> arr;

	cin >> S;
	cin >> stream;


	for(int i=0; i<stream.length(); i++){
		tmp = stream[i]-48;
		sum += tmp;
		arr.push_back(sum);
	}

	for(int i=1; i<S+1; i++){
		int diff = i- (arr.at(i-1)+result) ;
		if( diff > 0 )
			result += diff;
	}

	cout << "Case #" << caseNum << ": " << result <<endl;

	return;
}





