#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

int lawn[128][128];
int rowMax[128], colMax[128];

int main() {

	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	int T, N, M;
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> N >> M;

		for (int j = 0; j < 127; j++) {
			rowMax[j] = 0;
			colMax[j] = 0;
			for (int k = 0; k < 127; k++) {
				lawn[j][k] = 0;
			}
		}

		for (int j = 0; j < M; j++) {
			colMax[j] = 1;
		}

		int a;
		for (int j = 0; j < N; j++) {
			rowMax[j] = 1;
			for (int k = 0; k < M; k++) {
				cin >> a;
				if (a > colMax[k])
					colMax[k] = a;			
				if (a > rowMax[j])
					rowMax[j] = a;
				lawn[j][k] = a;
			}
		}
		bool result = true;
		for (int j = 0; result && j < N; j++) {
			for (int k = 0; result && k < M; k++) {
				if (lawn[j][k] < rowMax[j] && lawn[j][k] < colMax[k])
					result = false;
			}
		}

		string output = "NO";
		if (result)
			output = "YES";

		cout << "Case #" << i+1 << ": " << output << endl;
	}

	return 0;
}