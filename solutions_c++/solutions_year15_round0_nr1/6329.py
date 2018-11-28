#include <stdio.h>
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int totalCases, shyMax;	scanf("%d", &totalCases);
	char temp, waste;
	for (int caseNo = 1; caseNo <= totalCases; ++caseNo)
	{
		int required = 0, standing = 0;
		scanf("%d", &shyMax);
		int *number = new int[shyMax+1];
		scanf("%c", &waste);
		for (int shyness = 0; shyness <= shyMax; ++shyness){
			scanf("%c", &temp);
			number[shyness] = int(temp - '0');
		}
		for (int shyness = 0; shyness <= shyMax; ++shyness) {
			if (shyness>standing) {
				required += (shyness-standing);
				standing = shyness;
			}
			standing += number[shyness];
		}
		printf("Case #%d: %d\n", caseNo, required);
	}
	return 0;
}