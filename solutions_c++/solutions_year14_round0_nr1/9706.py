#include <iostream>
#include <string>
using namespace std;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin>>t;
	for (int z = 1; z <= t; z++) {
		printf("Case #%d: ", z);
		int p,q;
		int a[4][4], b[4][4];
		cin>>p;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				cin>>a[i][j];
		cin>>q;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				cin>>b[i][j];
		int s[17] = {0};
		p--;
		q--;

		for (int i = 0; i < 4; i++) {
			s[a[p][i]]++;
		}
		for (int i = 0; i < 4; i++) {
			s[b[q][i]]++;
		}
		int ans = 0;
		for (int i = 1; i <= 16; i++) {
			if (s[i] == 2) {
				if (ans != 0) {
					ans = -1;
					printf("Bad magician!\n");
					break;
				} else {
					ans = i;
				}
			}
		}
		if (ans == -1)continue;
		if (ans == 0)
			printf("Volunteer cheated!\n");
		else 
			printf("%d\n", ans);
	}
	fclose(stdout);
	return 0;
}