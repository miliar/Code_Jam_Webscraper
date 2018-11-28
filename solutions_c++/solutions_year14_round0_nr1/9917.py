#include <cstdio>
using namespace std;

int t1[4][4];
int t2[4][4];

int intersect(int c1,int c2) {
	int count=0;
	int temp=0;
	for (int i=0;i<4;i++) {
		for(int j=0;j<4;j++) {
			if(t1[c1-1][i]==t2[c2-1][j]) {
				temp=t1[c1-1][i];
				count++;
			}
		}
	}
	if(count==0)
		return 0;
	if(count==1)
		return temp;
	if(count>1)
		return -1;
}

int counter = 0;
void make() {
	printf("Case #%d: ", ++counter);
	int c1 = 0, c2 = 0;
	scanf("%d", &c1);
    for(int i=0; i<4; ++i) {
        for (int j=0; j<4; ++j) {
            scanf(" %d", &t1[i][j]);
        }
    }
    scanf("%d", &c2);
    for(int i=0; i<4; ++i) {
        for (int j=0; j<4; ++j) {
            scanf(" %d", &t2[i][j]);
        }
    }
    
    int check=intersect(c1,c2);
    if (check>=1)
    	printf("%d\n", check);
    if (check==0)
    	printf("%s\n", "Volunteer cheated!");
    if (check==-1)
    	printf("%s\n", "Bad magician!");
	return;	
}



int main() {
    int t; scanf("%d", &t);
    while(t--) {
        make();
    }
    return 0;
}
