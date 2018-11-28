#include <stdio.h>

struct testcases{
	int maxShyness;
	char personCount[1001];
};

int getMinFriendsCount(int d_maxShyness, char* c_personCount){
	int minfriendCnt = 0;
	int* personStanding = new int[d_maxShyness + 1];
	int tmp_personCntperShyness = 0, diff = 0;

	personStanding[0] = c_personCount[0] - '0';
	for (int ii = 1; ii <= d_maxShyness; ii++){
		diff = 0;
		tmp_personCntperShyness = c_personCount[ii] - '0';
		if (tmp_personCntperShyness && (ii > personStanding[ii - 1])){
			diff = ii - personStanding[ii - 1];
			minfriendCnt += diff;
		}
		personStanding[ii] = personStanding[ii - 1] + diff + tmp_personCntperShyness;
	}

	return minfriendCnt;
}

int main(){
	int d_numOfTestcases;
	int d_maxShyness;
	char c_personCount[1001];

	int minFriendsCount;

	FILE* inFile = NULL;
	fopen_s(&inFile, "in.txt", "r");

	FILE* outFile = NULL;
	fopen_s(&outFile, "out.txt", "w");

	fscanf_s(inFile, "%d", &d_numOfTestcases);

	for (int ii = 0; ii < d_numOfTestcases; ii++){
		fscanf_s(inFile, "%d", &d_maxShyness);
		fscanf_s(inFile, "%s", &c_personCount);

		minFriendsCount = getMinFriendsCount(d_maxShyness, c_personCount);
		fprintf(outFile, "Case #%d: %d\n", ii + 1, minFriendsCount);
	}
	return 0;
}