#include <cstdio>
#include <cstring>
#include <map>
#include <vector>
#include <queue>
#include <string>
#include <iostream>
#include <unordered_map>
using namespace std;

const int N = 4;
int array1[N];
int row;

int main()
{
    freopen("C:\\Users\\Administrator\\Desktop\\A-small-attempt0.in", "r", stdin);
    freopen("C:\\Users\\Administrator\\Desktop\\1.out", "w", stdout);
    int T; scanf("%d", &T);
    for (int t = 1; t <= T; ++t)
    {
        printf("Case #%d: ", t);
        vector<int> res;
        int num;
        scanf("%d", &row);
        for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				scanf("%d", &num);
				if (i == row-1)
					array1[j] = num;
			}
		}
        scanf("%d", &row);
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				scanf("%d", &num);
				if (i == row-1) {
					for (int k = 0; k < N; ++k)
						if (num == array1[k])
							res.push_back(num);
				}
			}
		}
		if (res.size() == 1)
			printf("%d\n", res[0]);
		else if (res.size() == 0)
			printf("Volunteer cheated!\n");
		else
			printf("Bad magician!\n");
    }
    return 0;
}
