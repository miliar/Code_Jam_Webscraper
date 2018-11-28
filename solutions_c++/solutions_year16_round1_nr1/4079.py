#include <stdio.h>
#include <string.h>
char input [1000+10];
char output [2000 + 10];

int main()
{
	int k;
	int T;
	scanf("%d", &T);
	for (int k = 0; k < T; k++)
	{
		char *buf = &output[1004];
		int begin = 1004;
		int end = 1004;

		scanf("%s", input);
		int last_max = 0;
		begin = 1004;
		end = 1004;
		last_max = 0;
		memset(output, '\0', sizeof(output));
		for (int i = 0; i < strlen(input); i++)
		{
			if (input[i] - 'A' >= last_max)
			{
				last_max = input[i]-'A';
				/* Insert at beginning */
				buf[begin] = input[i];
				begin--;
			}
			else
			{
				/* Insert at end */
				buf[++end] = input[i];
			}
			
		}
		buf[++end] = '\0';
		//printf("%d\n", begin);
		//printf("%d\n", end);
		printf("Case #%d: %s\n", (k+1), &buf[begin+1]);
	}
}
