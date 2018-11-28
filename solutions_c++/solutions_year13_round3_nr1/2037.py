#include <stdio.h>
#include <string.h>

#define BUFFER_SIZE 256
#define FILE_NAME "A-small-attempt1"

void split(char *str, int n, int *mNum)
{
	char *p = str;
	while(*p)
	{
		char tmp[100];
		for(int i=n;i<=strlen(str);i++)
		{
			memset(tmp, 0, 100);
			if(i>strlen(p))
				continue;
			strncpy(tmp, p, i);
			if(strlen(tmp)>=n)
			{
				
				int counter = 0;
				for(int j=0;j<strlen(tmp);j++)
				{
					char ch = tmp[j];
					if(ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u')
						counter=0;
					else
						counter++;
					if(counter>=n)
					{
						(*mNum)++;
						break;
					}
				}
			}
		}
		p++;
	}
}

int main()
{
	char buf[BUFFER_SIZE];
	memset(buf, 0, BUFFER_SIZE);
	sprintf(buf, "%s.in", FILE_NAME);
	freopen(buf, "r", stdin);
	memset(buf, 0, BUFFER_SIZE);
	sprintf(buf, "%s.out", FILE_NAME);
	freopen(buf, "w", stdout);

	int case_num, i=0;
	scanf("%d", &case_num);
	while(i<case_num)
	{
		int mNum = 0, n;
		char str[256] = {0};
		scanf("%s %d", str, &n);

		split(str, n, &mNum);

		printf("Case #%d: %d\n", i+1, mNum);
		i++;
	}
	return 0;
}