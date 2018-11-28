#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
	if (argc != 2) {
		printf("Invalid input\n");
		getchar();
		return 1;
	}

	freopen(argv[1], "r", stdin);

	char outname[255];
	sprintf(outname, "out-%s", argv[1]);
	freopen(outname, "w", stdout);

	int cases;
	scanf("%d\n", &cases);

	int table[101][101];

	int hmax[101];
	int vmax[101];

	int value;
	bool vd, hd;
	int n, m;
	char line[1024];
	for (int i = 0 ; i < cases ; ++i) {
		scanf("%d %d\n", &n, &m);

		for (int j = 0 ; j < n ; ++j) {
			for (int k = 0 ; k < m ; ++k) {
				scanf("%d", &table[j][k]);
			}
		}

		for (int j = 0 ; j < m ; ++j) {
			vmax[j] = table[0][j];
		}

		// compute hmax & vmax
		for (int j = 0 ; j < n ; ++j) {
			hmax[j] = table[j][0];
			for (int k = 0 ; k < m ; ++k) {
				if (hmax[j] < table[j][k]) hmax[j] = table[j][k];
				if (vmax[k] < table[j][k]) vmax[k] = table[j][k];
			}
		}

		for (int j = 0 ; j < n ; ++j) {
			for (int k = 0 ; k < m ; ++k) {
				vd = hd = true;

				value = table[j][k];

				if (value >= hmax[j] || value >= vmax[k]) continue;

				goto failed;
			}
		}
		printf("Case #%d: YES\n", i+1);
		continue;

failed:
		printf("Case #%d: NO\n", i+1);
	}

	return 0;
}