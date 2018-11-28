#include <cstdio>
int main(int argc, char* argv[])
{
	if (argc > 1)
		freopen(argv[1], "r", stdin);
	else
		return 0;
	int t, a, rc, mtch, arr[16], tmp[4];
	scanf("%d", &t);
	for (int cse = 1; cse <= t; cse++)
	{
		mtch = 0;
		scanf("%d", &a);
		a = (a - 1) * 4;
		for (int j = 0; j < 16; j++)
			scanf("%d", &arr[j]);
		for (int j = 0; j < 4; j++)
			tmp[j] = arr[a + j];
		scanf("%d", &a);
		for (int j = 0; j < 16; j++)
			scanf("%d", &arr[j]);
		a = (a - 1) * 4;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				if (tmp[i] == arr[a + j])
				{
					mtch++;
					rc = tmp[i];
				}
		printf("case #%d: ", cse);
		if (mtch > 1)
			printf("Bad magician!\n");
		else if (mtch)
			printf("%d\n", rc);
		else
			printf("Volunteer cheated!\n");
	}
	return 0;
}