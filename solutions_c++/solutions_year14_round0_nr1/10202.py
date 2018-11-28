#include <iostream>
#define BAD "Bad magician!"
#define CHEAT "Volunteer cheated!"
using namespace std;

int main(){
	int ntest;
	cin >> ntest;
	for(int test_no = 1; test_no <= ntest; test_no++){
		int a, b;
		int x[4][4], y[4][4];

		//enter
		cin >> a;
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				cin >> x[i][j];
		cin >> b;
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4;j ++)
				cin >> y[i][j];

		//solve
		int cnt = 0;
		int result;
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				if (x[a - 1][i] == y[b - 1][j]){
					cnt++;
					result = x[a-1][i];
				}

		//print result
		cout << "Case #"<< test_no << ": ";
		if (cnt == 0)
			cout << CHEAT;
		else if (cnt == 1)
			cout << result;
			else
				cout << BAD;
		cout << endl;
	}
	return 0;
}
