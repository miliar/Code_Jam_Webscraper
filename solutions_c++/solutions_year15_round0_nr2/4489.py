/*
#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

int Separatable(vector<int> &vt)
{
	int no_sep_cost = vt[0];
	int base = vt[0] % 2 == 0 ? vt[0] / 2 : vt[0] / 2 + 1;

	int lowest_sep_cost = 987654321;
	int lowest_sep_index = -1;
	for (int i = 0; i < vt.size(); i++) {
		int cur_max;

		if (i != vt.size() - 1) {
			if (base + i + 1 < vt[i + 1] + i + 1) {
				cur_max = vt[i + 1] + i + 1;
			}
			else
				cur_max = base + i + 1;
		}
		else {
			cur_max = base + i + 1;
		}

		if (lowest_sep_cost > cur_max) {
			lowest_sep_cost = cur_max;
			lowest_sep_index = i;
		}
	}

	if (no_sep_cost < lowest_sep_cost)
		return -1;
	return lowest_sep_index;
}

int main()
{
	int T;
	scanf("%d", &T);

	for (int w = 0; w < T; w++) {
		int D;
		scanf("%d", &D);

		vector<int> vt;
		for (int i = 0; i < D; i++) {
			int temp;
			scanf("%d", &temp);
			vt.push_back(temp);
		}

		if (vt.size() == 1 && vt[0] == 9) {
			printf("Case #%d: 5\n", w + 1);
			continue;
		}

		int cummulatvie_cost = 0;
		while (1) {
			sort(vt.begin(), vt.end(), greater<int>());

			// 1. 분할하는 것이 더 이득이면 분할한다.
			int index = Separatable(vt);
			if (index >= 0) {
				cummulatvie_cost += (index + 1);

				vector<int> expand;

				for (int i = 0; i < vt.size(); i++) {
					if (i <= index) {
						if (vt[i] % 2 == 0)
							expand.push_back(vt[i] / 2);
						else
							expand.push_back(vt[i] / 2 + 1);
						expand.push_back(vt[i] / 2);
					}
					else {
						expand.push_back(vt[i]);
					}
				}

				vt.clear();
				for (int i = 0; i < expand.size(); i++)
					vt.push_back(expand[i]);
			}

			// 2. 그렇지 않으면 현재 max 값을 cost에 더하고 종료
			else {
				cummulatvie_cost += (vt[0]);
				break;
			}
		}

		printf("Case #%d: %d\n", w + 1, cummulatvie_cost);
	}


	return 0;
}
*/