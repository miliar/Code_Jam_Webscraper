#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;

struct Block {
	Block(double mass, char player) : mass(mass), player(player) {}
	double mass;
	char player;
};

int main()
{
	int t, n, y, z;
	double w;
	scanf("%d", &t);

	for (int i = 1; i <= t; i++) {
		scanf("%d", &n);
		vector<Block> blocks;
		blocks.reserve(2 * n);
		for (int j = 0; j < n; j++) {
			scanf("%lf", &w);
			blocks.push_back(Block(w, 'N'));
		}
		for (int j = 0; j < n; j++) {
			scanf("%lf", &w);
			blocks.push_back(Block(w, 'K'));
		}
		sort(blocks.begin(), blocks.end(), [](const Block& a, const Block& b) {
			return a.mass < b.mass;
		});

		y = 0;
		z = 0;
		for (int i = 2 * n - 1, c = 0; i >= 0; i--) {
			c += (blocks[i].player == 'N') ? 1 : -1;
			z = max(z, c);
			y = min(y, c);
		}
		y = n + y;

		printf("Case #%d: %d %d\n", i, y, z);
	}
}
