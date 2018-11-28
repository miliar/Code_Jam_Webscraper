#include <iostream>
#include <cstdio>
#include <map>
using namespace std;
int T;
int f_a, s_a;

int main(int argc, const char * argv[])
{
    scanf("%d", &T);
	for (int t = 0; t < T; t++) {
		map<int,int> check;
        scanf("%d", &f_a);
        for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				int num;
				scanf("%d", &num);
				if (i+1 ==f_a) check[num]++;
            }
        }
        scanf("%d", &s_a);
        for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				int num;
				scanf("%d", &num);
				if (i+1 ==s_a) check[num]++;
            }
        }
		map<int, int>::iterator it = check.begin();
		int count = 0;
        int ans = 0;
		while (it !=check.end()) {
			if (it->second == 2) {
				count++;
				ans = it->first;
			}
			it++;
		}
        if (count == 1) {
            printf("Case #%d: %d\n", t+1, ans);
        } else if (count == 0) {
            printf("Case #%d: Volunteer cheated!\n", t+1);
        } else {
            printf("Case #%d: Bad magician!\n", t+1);
        }
    }
    return 0;
}

