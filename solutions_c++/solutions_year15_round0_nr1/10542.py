#include <iostream>
using namespace std;

int main() {
	int testCase;
	cin >> testCase;
	for(int i=0; i<testCase; i++) {
		int max;
		cin >> max;
		char personString[max+2];
		cin >> personString;
		int nowClap = 0;
		int minimumAdd = 0;
		for(int j=0; j<=max; j++){
			//cout << int(personString[j]-'0') << " ";
			int number = int(personString[j]-'0');
			//cout << nowClap << " ";
			if(nowClap >= j)
				nowClap+=number;
			else if(number > 0) {
				minimumAdd = minimumAdd+(j-nowClap);
				nowClap = nowClap+number+minimumAdd;
			}
		}
		cout <<"Case #"<<i+1<<": " <<minimumAdd << endl;
	}
	return 0;
}