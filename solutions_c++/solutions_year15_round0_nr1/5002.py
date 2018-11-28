#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
using namespace std;
void main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int nCase;
	cin >> nCase;
	for (int cc = 0; cc < nCase; ++cc) {
		int maxSh;
		string str;
		cin >> maxSh >> str;
		vector<int> shArr(str.size());
		for (int i = 0; i < maxSh + 1; ++i)
			shArr[i] = str[i] - '0';
		
		int sumStandingPeople = 0;
		int invitePeople = 0;
		for (int i = 0; i < shArr.size(); ++i) {
			int needStandingPeople = 0;
			if (sumStandingPeople < i) 
				needStandingPeople = i - sumStandingPeople;
			
			sumStandingPeople += shArr[i] + needStandingPeople;
			invitePeople += needStandingPeople;
		}
		cout << "Case #" << cc+1 << ": " << invitePeople << endl;
	}
}