#include <cstdio>
#include <vector>


void solve(int caseNo)
{
	int answer1, answer2;
	int layout1[4][4];
	int layout2[4][4];
	scanf("%d", &answer1);
	int i = 0, j = 0;
	for(i = 0; i < 4; i++){
		for(j = 0; j < 4; j++){
			scanf("%d", &layout1[i][j]);
		}
	}
	scanf("%d", &answer2);
	for(i = 0; i < 4; i++){
		for(j = 0; j < 4; j++){
			scanf("%d", &layout2[i][j]);
		}
	}

	int possibleCards[20] = {0};
	answer1--;
	answer2--;
	for (i = 0; i < 4; i++){
		possibleCards[layout1[answer1][i]]++;
		possibleCards[layout2[answer2][i]]++;
	}
	std::vector<int> answerCard;
	for (i = 1; i <= 16; i++){
		if (possibleCards[i] == 2)
			answerCard.push_back(i);
	}

	if (caseNo > 1)
		printf("\n");
	if (answerCard.size() == 0){
		printf("Case #%d: Volunteer Cheated!", caseNo);
	}
	else if (answerCard.size() > 1){
		printf("Case #%d: Bad Magician!", caseNo);
	}
	else if(answerCard.size() == 1){
		printf("Case #%d: %d", caseNo, answerCard[0]);
	}
}

int main()
{
	int numOfTestCases, i;
	scanf("%d", &numOfTestCases);
	for (i = 0; i < numOfTestCases; i++){
		solve(i+1);
	}
}
