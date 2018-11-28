#include <cstdio>
using namespace std;

int main() {
	int t;
	scanf("%d", &t);
	
	for(int c = 1; c <= t; c++){
		int row;
		int cards[16] = {0, 0, 0, 0,
		                 0, 0, 0, 0,
		                 0, 0, 0, 0,
		                 0, 0, 0, 0};
		
		scanf("%d", &row);
		
		for(int y = 0; y < 4; y++){
			for(int x = 0; x < 4; x++){
				int card;
				scanf("%d", &card);
				if(y == row - 1) cards[card - 1]++;
			}
		}
		
		int solutions = 0;
		int solution;
		
		scanf("%d", &row);
		
		for(int y = 0; y < 4; y++){
			for(int x = 0; x < 4; x++){
				int card;
				scanf("%d", &card);
				if(y == row - 1 && cards[card - 1] == 1){
					solutions++;
					solution = card;
				}
			}
		}
		
		printf("Case #%d: ", c);
		
		switch(solutions){
			case 0: printf("Volunteer cheated!\n"); break;
			case 1: printf("%d\n", solution); break;
			default: printf("Bad magician!\n");
		}
	}
	
	return 0;
}