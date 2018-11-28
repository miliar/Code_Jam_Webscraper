#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
	int T;

	cin >> T;

	for (int t=1; t != T+1; t++){
		cout << "Case #" << t << ": ";
		
		int r1;
		cin >> r1;
		vector <int> row1;
		for (int y = 1; y != 4+1; y++){
			for(int x = 0; x != 4; x++){
				int n;
				cin >> n;
				if (y == r1)
					row1.push_back(n);
			}

		}

		int r2;
		cin >> r2;
		vector <int> row2;
		for (int y = 1; y != 4+1; y++){
			for(int x = 0; x != 4; x++){
				int n;
				cin >> n;
				if (y == r2)
					row2.push_back(n);
			}

		}
		
		vector <int> intersection;	
		sort(row1.begin(),row1.end());		
		sort(row2.begin(),row2.end());

		set_intersection(row1.begin(),row1.end(),row2.begin(),row2.end(),back_inserter(intersection));

		switch (intersection.size()){
			case 0 : cout << "Volunteer cheated!";
				 break;
			case 1 : cout << intersection.front(); 
				 break;
			default : cout << "Bad magician!";
		}
		cout << endl;

	}

	return 0;
}

