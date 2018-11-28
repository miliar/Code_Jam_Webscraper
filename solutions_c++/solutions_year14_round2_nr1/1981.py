#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

#define FOR(i,a,b) for(int i = a ; i < b ; i++)
#define FORI(i,b,a) for(int i = b - 1 ; i >= a ; i--)

int findDiff(vector <int> arr, int num ) {
	int n = arr.size();
	int sum = 0;
	FOR(i,0,n) {
		sum = sum + abs(arr[i] - num);
	}
	return sum;
}

int findMinVariance(vector <int> arr) {
	int n = arr.size();
	int sum = 0;
	FOR(i,0,n) {
		sum = sum + arr[i];
	}
	if(sum % n != 0) {
		return min(min(findDiff(arr, sum / n), findDiff(arr, sum/n + 1)), findDiff(arr, sum/n - 1));
	} else {
		return findDiff(arr, sum / n);
	}
}

void solvePr1() {
	int T;
	cin >> T;
	for(int tc = 1 ; tc <= T ; tc++) {
		int N;
		cin >> N;
		int arr[102][102];
		memset(arr, 0, 0);
		int ans = 0;
		bool flag = false;
		vector <string> strArr(N);
		vector <int> startIndex(N, 0);
		vector <int> matchLen(N);
		FOR(i,0,N) {
			cin >> strArr[i];
		}
		while(startIndex[0] != strArr[0].length()) {
			char ch1 = strArr[0][startIndex[0]];
			FOR(i,1,N) {
				if(ch1 != strArr[i][startIndex[i]]) {
					cout << "Case #" << tc << ": Fegla Won" << endl;
					flag = true;
					break;
				} else {
					int c = 0;
					FOR(j, startIndex[i], strArr[i].length() + 1) {
						if(j == strArr[i].length() || ch1 != strArr[i][j]) {
							matchLen[i] = c;
							startIndex[i] = j;
							break;
						}
						c++;
					}
				}
			}
			if(flag) {
				break;
			} else {
				int c = 0;
				FOR(j, startIndex[0], strArr[0].length() + 1) {
					if(j == strArr[0].length() || ch1 != strArr[0][j]) {
						matchLen[0] = c;
						startIndex[0] = j;
						break;
					}
					c++;
				}
				ans = ans + findMinVariance(matchLen);
			}
		}
		if (!flag) {
		FOR(i,0,N) {
			if(startIndex[i] != strArr[i].length()) {
				cout << "Case #" << tc << ": Fegla Won" << endl;
				flag = true;
				break;
			}
		}
		}
		if(!flag) {
			cout << "Case #" << tc << ": " << ans << endl;
		}
	}
}

int main() {
	freopen("C:/Users/deepd/Downloads/in.txt", "r", stdin);
	freopen("C:/Users/deepd/Downloads/out.txt", "w", stdout);
	solvePr1();
	return 0;
}
