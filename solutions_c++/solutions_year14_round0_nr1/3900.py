#include<stdio.h>
#include<stdlib.h>

using namespace std;

int main(void){
	int n;
	scanf("%d\n",&n);
	for (int w = 1;w <= n ;w ++){
		int v[5],row,s[5],q[5];
		scanf("%d\n",&row);
		for (int j = 1; j < 5; j++)
				if (row == j) scanf(" %d %d %d %d\n",&v[1],&v[2],&v[3],&v[4]);
				else scanf(" %d %d %d %d\n",&s[1],&s[2],&s[3],&s[4]);
		scanf("%d\n",&row);	
		for (int j = 1; j < 5; j++)
				if (row == j) scanf(" %d %d %d %d\n",&q[1],&q[2],&q[3],&q[4]);
				else scanf(" %d %d %d %d\n",&s[1],&s[2],&s[3],&s[4]);
		int count = 0;
		int sol;
		for (int i = 1; i < 5; i++)
			for (int j = 1; j < 5; j++)
				if (q[i] == v[j]){
					count++;
					sol = q[i];
				}
		printf("Case #%d:",w);
		if (1 == count)
			printf(" %d\n",sol);	
		else if (0 == count) printf(" Volunteer cheated!\n");
			else printf(" Bad magician!\n");
	}
}
