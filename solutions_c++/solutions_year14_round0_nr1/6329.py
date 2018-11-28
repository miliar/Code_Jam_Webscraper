#include<iostream>
#include<set>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; t++){
		int answer1;
		cin >> answer1;
		set<int> candidate;
		for (int y = 0; y < 4; y++){
			for (int x = 0; x < 4; x++){
				int temp;
				cin >> temp;
				if (y == answer1 - 1) candidate.insert(temp);
			}
		}
		int answer2;
		cin >> answer2;
		int num = 0;
		int ans = 0;
		for (int y = 0; y < 4; y++){
			for (int x = 0; x < 4; x++){
				int temp;
				cin >> temp;
				if (y == answer2 - 1 && candidate.count(temp)){
					num++;
					ans = temp;
				}
			}
		}
		cout << "Case #" << t+1 << ": ";
		if (num == 1) cout << ans << endl;
		else if (num == 0) cout << "Volunteer cheated!"<<endl;
		else cout << "Bad magician!" << endl;
	}
}