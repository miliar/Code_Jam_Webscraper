#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

void solve();
int getDistance(const string& A, const string& B);
int getValue(vector<vector<int>>& arr, int i, int j);
void updateMin(vector<string>& strings, int& min, string comp);
int minInter(vector<string>& strings);
void printVec(vector<vector<int>>& arr);

int main() {
	int rounds;
	cin >> rounds;
	for (int i = 1; i <= rounds; ++i) {
		cout << "Case #" << i << ": ";
		solve();
		cout << '\n';
	}
	// string A, B;
	// cin >> A >> B;
	// cout << "distance: " << getDistance(A, B) << endl;
}

void solve() {
	int numStrings;
	vector<string> strings;
	string tempString;
	cin >> numStrings;
	for (int i = 0; i < numStrings; ++i) {
		cin >> tempString;
		strings.push_back(tempString);
	}

	int min = -1;
	for (int i = 0; i < numStrings; ++i) {
		updateMin(strings, min, strings[i]);
	}

	int tempInt = minInter(strings);
	if (tempInt < min || min == -1) {
		min = tempInt;
	}

	if (min == -1) {
		cout << "Fegla Won";
	} else {
		cout << min;
	}
}

void updateMin(vector<string>& strings, int& min, string comp) {
	int numActions = 0, distance;
	for (unsigned int j = 0; j < strings.size(); ++j) {
		distance = getDistance(comp, strings[j]);
		if (distance == -1) {
			numActions = -1;
			break;
		} else {
			numActions += distance;
		}
	}

	if (numActions < min || min == -1) {
		min = numActions;
	}
}

int minInter(vector<string>& strings) {
	struct bucket { 
		char c; int num; 
		bucket(char c_in, int num_in) : c(c_in), num(num_in) {};
	};
	vector<bucket> maxBuckets;
	vector<bucket> minBuckets;

	char tempChar = strings[0][0];
	int tempNum = 0;
	for (unsigned int i = 0; i < strings[0].size(); ++i) {
		if (tempChar != strings[0][i]) {
			maxBuckets.push_back(bucket(tempChar, tempNum));
			minBuckets.push_back(bucket(tempChar, tempNum));
			tempChar = strings[0][i];
			tempNum = 1;
		} else {
			tempNum++;
		}
	}
	maxBuckets.push_back(bucket(tempChar, tempNum));
	minBuckets.push_back(bucket(tempChar, tempNum));

	for (unsigned int i = 0; i < strings.size(); ++i) {
		for (unsigned int j = 0; j < maxBuckets.size(); ++j) {
			tempNum = count(strings[i].begin(), strings[i].end(), minBuckets[j].c);
			if (tempNum > maxBuckets[j].num) {
				maxBuckets[j].num = tempNum;
			}
			if (tempNum < minBuckets[j].num) {
				minBuckets[j].num = tempNum;
			}
		}
	}

	string maxString;
	for (unsigned int i = 0; i < maxBuckets.size(); ++i) {
		for (int j = 0; j < maxBuckets[i].num; ++j) {
			maxString.push_back(maxBuckets[i].c);
		}
	}

	string minString;
	for (unsigned int i = 0; i < minBuckets.size(); ++i) {
		for (int j = 0; j < minBuckets[i].num; ++j) {
			minString.push_back(minBuckets[i].c);
		}
	}

	int min = -1;
	updateMin(strings, min, maxString);
	updateMin(strings, min, minString);

	return min;
}



int getDistance(const string& A, const string& B) {
	vector<vector<int>> arr;
	for (unsigned int i = 0; i <= A.length(); ++i) {
		vector<int> temp;
		temp.resize(B.length() + 1);
		arr.push_back(temp);
	}

	arr[0][0] = 0;
	for (unsigned int i = 1; i <= A.length(); ++i) {
		arr[i][0] = -1;
	}
	for (unsigned int i = 1; i <= B.length(); ++i) {
		arr[0][i] = -1;
	}

	for (unsigned int i = 1; i <= A.length(); ++i) {
		for (unsigned int j = 1; j <= B.length(); ++j) {
			if (A[i - 1] == B[j - 1]) {
				arr[i][j] = getValue(arr, i, j);
			} else {
				arr[i][j] = -1;
			}
		}
	}

	// printVec(arr);
	return arr[A.length()][B.length()];
}

int getValue(vector<vector<int>>& arr, int i, int j) {
	int min = -1;
	if ((arr[i - 1][j] != -1) && (arr[i - 1][j] < min || min == -1)) {
		min = arr[i - 1][j] + 1;
	}
	if ((arr[i][j - 1] != -1) && (arr[i][j - 1] < min || min == -1)) {
		min = arr[i][j - 1] + 1;
	}
	if ((arr[i - 1][j - 1] != -1) && (arr[i - 1][j - 1] < min || min == -1)) {
		min = arr[i - 1][j - 1];
	}
	return min;
}

void printVec(vector<vector<int>>& arr) {
	for (unsigned int i = 0; i < arr.size(); ++i) {
		for (unsigned int j = 0; j < arr[i].size(); ++j) {
			cout << arr[i][j] << '\t';
		}
		cout << '\n';
	}
	cout << '\n';
}

