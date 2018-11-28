#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

vector< vector<int> > readArrangement()
{
	int tmp;
	vector< vector<int> > arrangement;
	for(int i=0; i < 4; i++) {
		vector<int> row;
		for(int j=0; j < 4; j++) {
			cin >> tmp;
			row.push_back(tmp);
		}
		arrangement.push_back(row);
	}

	return arrangement;
}

void solve(int firstAnswer, vector< vector<int> > firstArr, int secondAnswer, vector< vector<int> > secondArr)
{
	vector<int> fr = firstArr[firstAnswer];
	vector<int> sr = secondArr[secondAnswer];
	vector<int> v(8);
	vector<int>::iterator it;

	sort(fr.begin(), fr.end());
	sort(sr.begin(), sr.end());
	it = set_intersection(fr.begin(), fr.end(), sr.begin(), sr.end(), v.begin());
	v.resize(it-v.begin());

	vector<int>::size_type sz = v.size();

	if(sz > 1) {
		cout << "Bad magician!";
	} else if(sz == 1) {
		cout << v[0];
	} else if(sz == 0) {
		cout << "Volunteer cheated!";
	}
}

int main()
{
	int firstAnswer, secondAnswer;
	vector< vector<int> > firstArr, secondArr;

	int numCases = 0;
	cin >> numCases;

	for(int i=0; i < numCases; i++) {
		cin >> firstAnswer;
		firstAnswer -= 1;
		firstArr = readArrangement();

		cin >> secondAnswer;
		secondAnswer -= 1;
		secondArr = readArrangement();

		cout << "Case #" << i+1 << ": ";
		solve(firstAnswer, firstArr, secondAnswer, secondArr);
		cout << endl;
	}

	return 0;
}
