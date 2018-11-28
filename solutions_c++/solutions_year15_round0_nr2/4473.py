#include <bits/stdc++.h>
#include <fstream>
using namespace std;
int n, num;

bool cmp(int a, int b)
{
    return a > b ? true : false;
}

int main() {
	//ofstream myfile;
   // myfile.open("output3.txt");
    int tc;
	scanf("%d", &tc);
	for (int ncase = 1; ncase <= tc; ncase++) {
		scanf("%d", &n);
		vector<int> v1, v2;
		int res = 0;
		for (int i = 0; i < n; i++) {
			scanf("%d", &num);
			res = max(res, num);
			v1.push_back(num);
			v2.push_back(num);
		}

		int time = 0;
		while (true) {
			if (v1.size() == 0) break;
			sort(v1.begin(), v1.end(), cmp);
			int cur = v1[0];
			int totalTime = time + cur;
			res = min(res, totalTime);
			if (cur <= 3)
				break;
			if (cur == 6) {
				v1[0] = 3;
				v1.push_back(3);
			} else if (cur == 9) {
				v1[0] = 3;
				v1.push_back(6);
			} else {
				v1[0] = cur / 2 + cur % 2;
				v1.push_back(cur / 2);
			}
			time++;
		}

		time = 0;
		while (true) {
			if (v2.size() == 0) break;
			sort(v2.begin(), v2.end(), cmp);
			int cur = v2[0];
			int totalTime = time + cur;
			res = min(res, totalTime);
			if (cur <= 3)
				break;

            v2[0] = cur / 2 + cur % 2;
            v2.push_back(cur / 2);

			time++;
		}

		cout << "Case #"<<ncase<<": "<<res << endl;
		//myfile << "Case #"<<ncase<<": "<<res << endl;
	}
	//myfile.close();
}
