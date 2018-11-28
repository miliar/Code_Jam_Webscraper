#include<iostream>
#include<vector>
#include<string>
#include<fstream>
using namespace std;
void main(){
	int cases;
	vector<string> answer;
	if (cin >> cases){
		for (int i = 0; i != cases; ++i){
			int first, second;
			vector<vector<int>> a, b;
			cin >> first;
			int x;
			for(int j=0;j!=4;++j){
				vector<int> c;
				for (int i = 0; i != 4; ++i){
					cin >> x;
					c.push_back(x);
				}
				a.push_back(c);
			}
			cin >> second;
			for (int j = 0; j != 4; ++j){
				vector<int> d;
				for (int i = 0; i != 4; ++i){
					cin >> x;
					d.push_back(x);
				}
				b.push_back(d);
			}
			int total = 0;
			for (auto i : a[first - 1]){
				for (auto j : b[second - 1]){
					if (i == j)
						++total;
				}
			}
			int z = 0;
			if (total>1)
				answer.push_back("Case #" + to_string(i + 1) + ": Bad magician!");
			if (total == 0)
				answer.push_back("Case #" + to_string(i + 1) + ": Volunteer cheated!");
			if (total == 1){
				for (auto r : a[first - 1]){
					for (auto s : b[second - 1]){
						if (r == s){
							answer.push_back("Case #" + to_string(i + 1)+": "+to_string(r));
							z = 1;
							break;
						}
					}
					if (z == 1)
						break;
				}
			}
		}
	}
	for (auto j : answer)
		cout << j << endl;
}