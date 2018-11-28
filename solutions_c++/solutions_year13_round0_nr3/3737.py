#include <set>
#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

set<double> palins;

double loc[] = {0, 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000, 100000000000,
		1000000000000, 10000000000000, 100000000000000};

bool ispal(string& str)
{
	for (int i = 0; i < str.length()/2; i++)
		if (str[i] != str[str.length()-i-1])
			return false;
	return true;
}

int main()
{
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("fas.out", "w", stdout);

	// generate all palindromes
	// 1D 2D
	for (int d1 = 1; d1 <= 9; d1++) {
		palins.insert(d1);
		palins.insert(d1*10 + d1);
	}
	// 3D 4D
	for (int d1 = 1; d1 <= 9; d1++)
		for (int d2 = 0; d2 <= 9; d2++) {
			palins.insert(d1*100 + d2*10 + d1);
			palins.insert(d1*1000 + d2*100 + d2*10 + d1);
		}
	// 5D 6D
	for (int d1 = 1; d1 <= 9; d1++)
		for (int d2 = 0; d2 <= 9; d2++)
			for (int d3 = 0; d3 <= 9; d3++) {
				palins.insert(d1*10000 + d2*1000 + d3*100 + d2*10 + d1);
				palins.insert(d1*100000 + d2*10000 + d3*1000 + d3*100 + d2*10 + d1);
			}
	// 7D 8D
	for (int d1 = 1; d1 <= 9; d1++)
		for (int d2 = 0; d2 <= 9; d2++)
			for (int d3 = 0; d3 <= 9; d3++)
				for (int d4 = 0; d4 <= 9; d4++) {
					palins.insert(d1*loc[7] + d2*loc[6] + d3*loc[5] + d4*loc[4] + d3*loc[3] + d2*loc[2] + d1);
					palins.insert(d1*loc[8] + d2*loc[7] + d3*loc[6] + d4*loc[5] + d4*loc[4] + d3*loc[3] + d2*loc[2] + d1);
				}
	// 9D 10D
	/*for (int d1 = 1; d1 <= 9; d1++)
		for (int d2 = 0; d2 <= 9; d2++)
			for (int d3 = 0; d3 <= 9; d3++)
				for (int d4 = 0; d4 <= 9; d4++)
					for (int d5 = 0; d5 <= 9; d5++) {
						palins.insert(d1*loc[9] + d2*loc[8] + d3*loc[7] + d4*loc[6] + d5*loc[5] + d4*loc[4] + d3*loc[3] + d2*loc[2] + d1);
						palins.insert(d1*loc[10] + d2*loc[9] + d3*loc[8] + d4*loc[7] + d5*loc[6] + d5*loc[5] + d4*loc[4] + d3*loc[3] + d2*loc[2] + d1);
					}
	// 11 12
	for (int d1 = 1; d1 <= 9; d1++)
		for (int d2 = 0; d2 <= 9; d2++)
			for (int d3 = 0; d3 <= 9; d3++)
				for (int d4 = 0; d4 <= 9; d4++)
					for (int d5 = 0; d5 <= 9; d5++)
						for (int d6 = 0; d6 <= 9; d6++) {
							palins.insert(d1*loc[11] + d2*loc[10] + d3*loc[9] + d4*loc[8] + d5*loc[7] + d6*loc[6] + d5*loc[5] + d4*loc[4] + d3*loc[3] + d2*loc[2] + d1);
							palins.insert(d1*loc[12] + d2*loc[11] + d3*loc[10] + d4*loc[9] + d5*loc[8] + d6*loc[7] + d6*loc[6] + d5*loc[5] + d4*loc[4] + d3*loc[3] + d2*loc[2] + d1);
						}*/
	
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		char a[102], b[102];
		scanf("%s %s", a, b);

		int la = strlen(a), lb = strlen(b);
		if (la <= 12 && lb <= 12) {
			double da = atof(a), db = atof(b);
			set<double>::iterator current = palins.lower_bound(da);
			set<double>::iterator end = palins.upper_bound(db);
			long long solution = 0;
			while (current != end) {
				double curr = sqrt(*current);
				if ((curr == ((long long)curr)) && (palins.count(curr) != 0))
					solution++;
				current++;
			}
			printf("Case #%d: %lld\n", t, solution);
		} else {
			string current = a;
			string end = b;
			long long solution = 0;
			while ((current.length() < lb) || (current.length() == lb && current.compare(end) <= 0)) {
				if (ispal(current))
					solution++;

				int addindex = current.length()-1;
				while (addindex >= 0 && current[addindex] == '9')
					addindex--;
				if (addindex == -1) {
					for (int i = 0; i < current.length(); i++)
						current[i] = '0';
					current.insert(0, "1");
				} else {
					current[addindex] = current[addindex] + 1;
					for (int i = addindex + 1; i < current.length(); i++)
						current[i] = '0';
				}
			}
			printf("Case #%d: %lld\n", t, solution);
		}
	}
	return 0;
}