#include<cstdio>
using namespace std;

int T[4][4], T2[4][4], no1, no2;

int main(){
	int Z;
	scanf("%d", &Z);
	for(int z = 1; z <= Z; ++z){
		
		scanf("%d", &no1);no1--;
		for(int i = 0; i < 4; ++i)
			for(int j = 0; j < 4; ++j)
				scanf("%d", &T[i][j]);
		scanf("%d", &no2);no2--;
		for(int i = 0; i < 4; ++i)
			for(int j = 0; j < 4; ++j)
				scanf("%d", &T2[i][j]);
				
		int match = 0, numb = -1;
		for(int i = 0; i < 4; ++i)
			for(int j = 0; j < 4; ++j)
				if(T[no1][i]==T2[no2][j]){
					match ++;
					numb = T[no1][i];
				}
		
		printf("Case #%d: ", z);
		if(match == 0)
			printf("Volunteer cheated!\n");
		if(match == 1)
			printf("%d\n", numb);
		if(match > 1)
			printf("Bad Magician!\n");
	}
	return 0;
}
