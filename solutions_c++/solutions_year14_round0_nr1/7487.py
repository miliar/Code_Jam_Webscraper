#include <cstdio>
#include <iostream>
#include <fstream>
//#include <cstdio>

using namespace std;

int main()
{
	int t, n, temp, x;
	int arr[4];
	ofstream out("out.txt");

	scanf("%d", &t);

	for (int k = 0; k < t; ++k) {
		scanf("%d", &n);

		for (int i = 0; i < 4; ++i) {
			if(i+1 == n) {
				for (int j = 0; j < 4; ++j) {
					scanf("%d", &arr[j]);
				}
			} else {
				for (int j = 0; j < 4; ++j) {
					scanf("%d", &temp);
				}
			}
		}
		scanf("%d", &n);
		int ans = -1;
		int l = 0;

		for (int i = 0; i < 4; ++i) {
			if(i+1 == n) {
				for (int j = 0; j < 4; ++j) {
					scanf("%d", &temp);
					if(arr[0] == temp) {
						ans = arr[0];
						++l;
					}
					else if(arr[1] == temp) {
						ans = arr[1];
						++l;
					}
					else if(arr[2] == temp) {
						ans = arr[2];
						++l;
					}
					else if(arr[3] == temp) {
						ans = arr[3];
						++l;
					}
				}
			} else {
				for (int j = 0; j < 4; ++j) {
					scanf("%d", &temp);
				}
			}
		}

		if(ans == -1) {
			//out << "Case #" << k+1 << ": Volunteer cheated!\n";
			printf("Case #%d: Volunteer cheated!\n", k+1);
		} else if(l > 1) {
			//out << "Case #" << k+1 << ": Bad magician!\n";
			printf("Case #%d: Bad magician!\n", k+1);
		} else {
			//out << "Case #" << k+1 << ": " << ans << "\n";
			printf("Case #%d: %d\n", k+1, ans);
		}
	}
	return 0;
}
