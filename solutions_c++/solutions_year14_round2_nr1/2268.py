#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int CaseNum;
	cin >> CaseNum;
	for (int Case = 1; Case <= CaseNum; Case++)
	{
		cout << "Case #" << Case << ": ";
		fprintf(stderr, "Case #%d\n", Case);
		int N;
		cin >> N;

		vector<string> list;
		for (int i = 0; i < N; i++) {
			string temp;
			cin >> temp;
			list.push_back(temp);
		}

		int cnt = 0;

		while (list[0].length() != 0) {
			char c = list[0][0];
			int sum = 0;
			vector<int> index;
			for (int i = 0; i < N; i++) {
				int idx;
				bool flag = true;
				for (idx = 0; idx < list[i].length(); idx++) {
					if (list[i][idx] != c ) {
						index.push_back(idx);
						list[i] = list[i].substr(idx);
						flag = false;
						break;
					}
				}
				if (idx == 0) {
					cnt = -1;
					break;
				}
				else if (flag) {
					index.push_back(idx);
					list[i] = string();
				}
				sum += idx;
			}
			if (cnt == -1)
				break;
			int mean = (sum * 2 + 1) / (2 * N);
			for (int i = 0; i < index.size(); i++) {
				cnt += abs(index[i] - mean);
			}

		}

		for (int i = 0; i < N; i++) {
			if (list[i].length() != 0) cnt = -1;
		}

		if (cnt == -1)
			cout << "Fegla Won"<< endl;
		else 
			cout << cnt << endl;

	} 

}