#include <cstdio>

#define MAX 20

using namespace std;

int t, firstRow, secondRow, countTwo;
int T[MAX][MAX];
int R[MAX];

int main()
{
	scanf("%d", &t);
	int n=t;
	while(t--) {
		countTwo=0;
		for(int i = 1; i <= 16; ++i)
			R[i]=0;
		
		scanf("%d", &firstRow);
		for(int i = 1; i <= 4; ++i) {
			for(int j = 1; j <= 4; ++j) {
				scanf("%d", &T[i][j]);
				if(firstRow==i)
					R[T[i][j]]++;
			}
		}

		scanf("%d", &secondRow);
		for(int i = 1; i <= 4; ++i) {
			for(int j = 1; j <= 4; ++j) {
				scanf("%d", &T[i][j]);
				if(secondRow==i)
					R[T[i][j]]++;
			}
		}

		for(int i = 1; i <= 16; ++i) {
			if(R[i]==2)
				countTwo++;
		}

		if(countTwo==1) {
			for(int i = 1; i <= 16; ++i)
				if(R[i]==2)
					printf("Case #%d: %d\n", n-t,i);
		}
		else if(countTwo>1)
			printf("Case #%d: Bad magician!\n", n-t);
		else
			printf("Case #%d: Volunteer cheated!\n", n-t);
	}
	
	return 0;
}