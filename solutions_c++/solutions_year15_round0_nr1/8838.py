//Problem A. Standing Ovation

#include <cstdio>

int main() {
	int T;
	scanf("%d", &T);
	char shyCountList[1000 + 5];
	for (int caseIndex = 1; caseIndex <= T; caseIndex++) {
		int maxShyValue;
		scanf("%d", &maxShyValue);
		scanf("%s", shyCountList);
		
		char *s = shyCountList;
		while (*s != 0) { *s -= '0'; s++; }

		int needInvitedTotalCount = 0;
		int standUpCount = shyCountList[0];
		for (int shy = 1; shy <= maxShyValue; shy++) {
			if (shyCountList[shy] >= 0) {
				if (standUpCount < shy) {
					int needInvitedCount = shy - standUpCount;
					needInvitedTotalCount += needInvitedCount;
					standUpCount += needInvitedCount;
				}
				standUpCount += shyCountList[shy];
			}
		}

		printf("Case #%d: %d\n", caseIndex, needInvitedTotalCount);
	}
	return 0;
}
