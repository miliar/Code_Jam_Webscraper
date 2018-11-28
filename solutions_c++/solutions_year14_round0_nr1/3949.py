#include <cstdio>
using namespace std;

char t1[4];//[4];
char t2[4];//[4]


void make() {
	int match=-1;
	int cards[4];
	int a1, a2;
	int tmp;
    int c1 = 0, c2 = 0;
	scanf("%d", &a1);
    for(int i=0; i<4; ++i) {
        for (int j=0; j<4; ++j) {
			if (i==(a1-1)) {
				scanf("%d", &t1[j]);
			}
			else {
				scanf("%d", &tmp);
			}
        }
    }

	scanf("%d", &a2);
    for(int i=0; i<4; ++i) {
        for (int j=0; j<4; ++j) {
			if (i==(a2-1)) {
				scanf("%d", &t2[j]);
			}
			else {
				scanf("%d", &tmp);
			}
        }
    }
	
	for (int i=0; i<4; ++i) {
		for (int j=0;j<4; ++j) {
			if (t1[i]==t2[j]) {
				match++;
				cards[match]=t1[i];
			}
		}
	}

    if (match == 0) {
        printf("%d\n",cards[0]);
    } else if (match >= 1) {
        printf("Bad magician!\n");
    } else if (match==-1) {
		printf("Volunteer cheated!\n");
	}
    return;
}

int main() {
	int counter = 0;
    int t; scanf("%d", &t);
    while(t--) {
		printf("Case #%d: ", ++counter);
        make();
    }
    return 0;
}
