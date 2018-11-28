#include <iostream>
#include <string>
#include <algorithm>
#include <utility>

using namespace std;

int ns[1000];
int m_is[1000][1000];
int result1[1000];
int result2[1000];

int main(){
	//input
	int test_case_no;
	cin >> test_case_no;
	for (int i = 0; i < test_case_no; i++){
		cin >> ns[i];
		//cout << ns[i] << endl;
		for (int j = 0; j < ns[i]; j++){
			cin >> m_is[i][j];
			//cout << m_is[i][j] << endl;
		}
	}

	//calculate
	for (int i = 0; i < test_case_no; i++){
		result1[i] = 0;
		result2[i] = 0;
		for (int j = 0; j < ns[i] - 1; j++){
			//cout << m_is[j] - m_is[j + 1];
			result1[i] += max(0, m_is[i][j] - m_is[i][j + 1]);
		}

		int most_decrease = 0;
		for (int j = 0; j < ns[i] - 1; j++){
			most_decrease = max(most_decrease, max(0, m_is[i][j] - m_is[i][j + 1]));
		}
		for (int j = 0; j < ns[i] - 1; j++){
			result2[i] += min(m_is[i][j], most_decrease);
		}

	}

	//output
	for (int i = 0; i < test_case_no; i++){
		cout << "Case #" << i + 1 << ": " << result1[i] << " " << result2[i] << endl;
	}

	return 0;
}