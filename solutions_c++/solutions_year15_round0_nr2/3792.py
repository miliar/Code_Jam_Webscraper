#include <cstdio>
#include <cstdlib>
#include <vector>
#include <stack>
using namespace std;

int maxFunction(int i, int j) {
	if (i > j) return i;
	return j;
}

int main() {
	FILE *in = fopen("B-small-attempt1.in", "r");
	FILE *out = fopen("2.out", "w");
	int T;
	fscanf(in, "%d", &T);
	int cnt = 0;
	while (cnt < T) {
		int S = 0;
		fscanf(in, "%d", &S);
		vector<int> vec;
		int tmp;
		for (int i = 0; i < S; i++) {
			fscanf(in, "%d", &tmp);
			vec.push_back(tmp);
		}
					
		int time = 0;
		while (true) {
			for (int i = 0; i < vec.size(); i++)
				printf("%d ", vec[i]);
			printf("\n");
			int maxId = 0, max = 0, preMax;
			for (int i = 0; i < vec.size(); i++)
				if (vec[i] > max) {
					preMax = max;
					max = vec[i];
					maxId = i;
				}
		
			int div1 = max / 2, div2 = max - div1;
			int secMax = maxFunction(preMax, maxFunction(div1, div2));
			
			if (max > secMax + 1) {
				vec.erase(vec.begin() + maxId);
				vec.push_back(div1);
				vec.push_back(div2);
			} else {
				stack<int> eStack;
				for (int i = 0; i < vec.size(); i++) {
					vec[i]--;
					if (vec[i] == 0)
						eStack.push(i);
				}
				while (eStack.size() != 0) {
					int tmp = eStack.top();
					vec.erase(vec.begin() + tmp);
					eStack.pop();
				}
			}

			time++;
			if (vec.size() == 0)
				break;
		}
		fprintf(out, "Case #%d: %d\n", cnt + 1, time);
		cnt++;
	}
	fclose(in);
	fclose(out);
}
