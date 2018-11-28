#include <stdio.h>
#include <iostream>
#include <vector>
#include <map>
#include <string>

using namespace std;

bool check(vector<int> p, int n, int total, int index) {
	int i;
	p[index]--;
	for (i = 0; i < n; i++) {
		if ((p[i] / (float)total) >= 0.5) {
			return false;
		}
	}
	return true;
}

int main() {
	int t, c;
	int i, n, total;
	vector<int> p = vector<int>(26, 0);
	string output;

	c = 1;
	scanf("%d", &t);
	while (t--) {
		output = " ";
		total = 0;
		scanf("%d", &n);
		for (i = 0; i < n; i++) {
			scanf("%d", &p[i]);
			total += p[i];
		}
		int index, max, index2, max2;
		while (true) {
			index2 = index = -1;
			max2 = max = 0;
			for (i = 0; i < n; i++) {
				if (max <= p[i]) {
					if (max > max2) {
						max2 = max;
						index2 = index;
					}
					index = i;
					max = p[i];
				}
			}
			if (max == 0)
				break;
			else {
				char aux, temp;
				if (check(p, n, total - 1, index)) {
					p[index]--;
					total--;
					aux = ('A' + index);
					if (output.size() == 0)
						output = aux;
					else
						output = output + " " + aux;
				} else {
					if (total == 3) {
						aux = 'A' + index;
						p[index]--;
						total -= 1;
						if (output.size() == 0)
							output = aux + temp;
						else
							output = output + " " + aux;
					}
					else {
						temp = 'A' + index2;
						aux = 'A' + index;
						p[index2]--;
						p[index]--;
						total -= 2;
						if (output.size() == 0)
							output = aux + temp;
						else
							output = output + " " + aux + temp;
					}
				}
				
				
			}
		}

		cout << "Case #" << c << ": ";
		c++;
		bool flag = true;
		for (i = 0; i < output.size(); i++) {
			if (output[i] == ' ' && flag) {
				continue;
			}
			flag = false;
			cout << output[i];
		}
		cout << endl;
	}

	return 0;
}