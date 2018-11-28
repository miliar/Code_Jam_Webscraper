#include <vector>
#include <algorithm>
#include <stdio.h>
using namespace std;
/*unsigned int cheat_play(vector<double>::iterator n, vector<double>::iterator k, int size) {
	int ret = 0;
	/*sort(n->begin(), n->end());
	sort(k->begin(), k->end());*/
	/*if ()
	for (int i = 0; i < size; ++i) {
		for (int j = 0; j < size-1; ++j)
		if (n[i] > k[j]) {
			ret++;
			break;
		}
	}
	return ret;
}*/
unsigned fair(vector<double>::iterator n, vector<double> k, unsigned size) {
	unsigned ret = 0;
	for (int i = 0; i < size; i++) {
		bool flag = false;
		for (int j = 0; j < size; j++)
		if (n[i] < k[j]) {
			k[j] = 0;
			flag = true;
			break;
		};
		if (!flag) ret++;
	}
	return ret;
}
unsigned cheat(vector<double>::iterator n, vector<double> k, unsigned size) {
	unsigned ret = 0;
	for (int i = 0; i < size; i++) {
		for (int j = 0; j < size; j++)
		if (n[i] > k[j]) {
			ret++;
			k[j] = 2;
			break;
		}
	}
	return ret;
}
int main(int argc, char* argv[])
{
	vector<double> n;
	vector<double> k;
	double blockWeight;
	unsigned int blocksNum;
	unsigned int N;
	scanf("%d", &N);
	for (unsigned int i = 1; i <= N; i++)
	{
		scanf("%d", &blocksNum);
		for (unsigned int j = 0; j < blocksNum; j++)
		{
			scanf("%lf", &blockWeight);
			n.push_back(blockWeight);
		}
		for (unsigned int j = 0; j < blocksNum; j++)
		{
			scanf("%lf", &blockWeight);
			k.push_back(blockWeight);
		}
		sort(n.begin(), n.end());
		sort(k.begin(), k.end());
		printf("Case #%d: %d %d\n", i, cheat(n.begin(), k, blocksNum), fair(n.begin(), k, blocksNum));
		n.clear();
		k.clear();
	}
	return 0;
}

