#include "bits/stdc++.h"
using namespace std;
int main() {
	freopen("A-small-attempt1.in", "r", stdin);
	int Case;
	cin >> Case;
	FILE *fp = fopen("output.text","w");
	for (int tc = 1; tc <= Case; tc++) {
		int N;
		cin >> N;
		if (N == 0) {
			fprintf(fp,"Case #%d: INSOMNIA\n", tc);
			continue;
		}
		int num;
		bool cnt[10];
		memset(cnt, 0, sizeof(cnt));
		int idx = 1;
		string temp;
		while (true) {
			num = idx*N;
			idx++;;
			temp = to_string(num);
			int len = temp.length();
			for (int i = 0; i < len; i++)
				cnt[temp[i] - '0'] = true;
			int flag = 0;
			for (int i = 0; i < 10; i++)
				if (cnt[i])
					flag++;
			if (flag == 10) {
				fprintf(fp,"Case #%d: %d\n", tc, num);
				break;
			}
		}
	}
	return 0;
}