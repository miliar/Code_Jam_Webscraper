#include <cstdio>

using namespace std;

const unsigned int DIM = 4;

int main(){
	unsigned int T = 0;
	scanf("%u", &T);
	for(unsigned int case_no = 1; case_no <= T; case_no++){
		unsigned int arrange_1[DIM][DIM] = {{0}};
		unsigned int arrange_2[DIM][DIM] = {{0}};
		unsigned int answer_1 = 0;
		unsigned int answer_2 = 0;

		scanf("%u", &answer_1);
		answer_1--;

		for(unsigned int r = 0; r < DIM; r++){
			for(unsigned int c = 0; c < DIM; c++){
				scanf("%u", &arrange_1[r][c]);
			}	
		}

		scanf("%u", &answer_2);
		answer_2--;

		for(unsigned int r = 0; r < DIM; r++){
			for(unsigned int c = 0; c < DIM; c++){
				scanf("%u", &arrange_2[r][c]);
			}	
		}

		unsigned int match_count = 0;
		unsigned int last_match = 0;
		for(unsigned int i1 = 0; i1 < DIM; i1++){
			for(unsigned int i2 = 0; i2 < DIM; i2++){
				if(arrange_1[answer_1][i1] == arrange_2[answer_2][i2]){
					match_count++;
					last_match = arrange_1[answer_1][i1];
				}
			}
		}
		if(match_count == 0){
			printf("Case #%u: Volunteer cheated!\n", case_no);
		}else if(match_count > 1){
			printf("Case #%u: Bad magician!\n", case_no);
		}else if(match_count == 1){
			printf("Case #%u: %u\n", case_no, last_match);
		}
	}

	return 0;
}