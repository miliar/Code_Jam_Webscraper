#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <queue>
#include <stack>
#include <set>

using namespace std;

vector<int> pairing(vector<int> &inp)
{
	vector<pair<int, int> > vals;
	for (int i=0;i<inp.size();i++) {
		vals.push_back(make_pair(inp[i], i));
	}
	vector<int> result(3, 0);
	sort(vals.rbegin(), vals.rend());
	while (vals[0].first > 0) {
		int idx1 = vals[0].second;
		vals[0].first--;
		int idx2 = vals[1].second;
		vals[1].first--;
		if (vals[1].first < 0) {
			result[0] = -1;
			return result;
		}
		result[(idx1+idx2)%3]++;
		sort(vals.rbegin(), vals.rend());
	}
	return result;
}

string construct(string str, int n)
{
	if (n == 0) {
		if (str == "R") return "RS";
		if (str == "S") return "PS";
		if (str == "P") return "PR";
	}
	string str1, str2;
	if (str == "R") {
		str1 = construct("R", n-1);
		str2 = construct("S", n-1);
	}
	if (str == "S") {
		str1 = construct("P", n-1);
		str2 = construct("S", n-1);
	}
	if (str == "P") {
		str1 = construct("R", n-1);
		str2 = construct("P", n-1);
	}
	if (str1 < str2) return str1+str2;
	return str2+str1;
}

int main()
{
	freopen("C:\\Projects\\gcj\\input.txt", "r", stdin);
	freopen("C:\\Projects\\gcj\\output.txt", "w", stdout);

	int z;
	cin >> z;
	for (int q1=0;q1<z;q1++) {
		int n,r,p,s;
		cin >> n >> r >> p >> s;
		int vals[13][3] = { 0 };
		int pairs[13][3] = { 0 };
		vals[0][0] = r;
		vals[0][1] = p;
		vals[0][2] = s;
		bool flag = true;
		for (int i=1;i<=n;i++) {
			vector<int> temp;
			temp.push_back(vals[i-1][0]);
			temp.push_back(vals[i-1][1]);
			temp.push_back(vals[i-1][2]);
			vector<int> result = pairing(temp);
			if (result[0] == -1) {
				flag = false;
				break;
			}
			for (int j=0;j<3;j++) {
				pairs[i][j] = result[j];
			}
			vals[i][0] = result[2];
			vals[i][1] = result[1];
			vals[i][2] = result[0];
			//cout << vals[i][0] << " " << vals[i][1] << " " << vals[i][2] << endl;
		}
		cout << "Case #" << (q1+1) << ": ";
		if (!flag) {
			cout << "IMPOSSIBLE" << endl;
		}
		else {
			int final;
			for (int i=0;i<3;i++) {
				if (vals[n][i] != 0)
					final = i;
			}
			string str1 = "";
			if (final == 0) {
				str1 = "R";
			}
			else if (final == 1) {
				str1 = "P";
			}
			else {
				str1 = "S";
			}
			cout << construct(str1, n-1) << endl;
		}
	}

	fclose(stdout);
	fclose(stdin);

	return 0;
}