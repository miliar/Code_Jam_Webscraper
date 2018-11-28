#include <iostream>
#include <vector>
using namespace std;

int main() {
	int t;

	cin >> t;
	int c;
	while(t--){
		c++;
		int a[5][5],b[5][5];
		vector<int> common;
		int f,s;

		cin >> f;
		for(int i =1;i<=4;i++)
			for(int j =1;j<=4;j++)
				cin >> a[i][j];

		cin >> s;

		for(int i =1;i<=4;i++)
			for(int j =1;j<=4;j++)
				cin >> b[i][j];

		for(int i = 1;i<=4;i++)
			for(int j =1;j<=4;j++){
				if(a[f][i] == b[s][j])
					common.push_back(a[f][i]);
			}


		int size = common.size();

		cout << "Case #" <<c<< ": "; 
		if(size == 0)
			cout << "Volunteer cheated!" <<endl;
		else if(size == 1)
			cout << common[0] <<endl;
		else if(size > 1)
			cout << "Bad magician!" <<endl;


	}
}