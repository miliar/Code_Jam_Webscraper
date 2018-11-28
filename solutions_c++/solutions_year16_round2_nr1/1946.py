#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;
int num[100], size[100];
char s[5000]; 
int main()
{
	int T;
	scanf("%d", &T);
	
	for (int t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);
		memset(num, 0, sizeof(num));
		scanf("%s", s + 1);
		int len = strlen(s + 1);
		for (int i = 1; i <= len; i++)
		{
			num[s[i] - 'A' + 1] ++;
		}
		 size[0] = num[26], size[2] = num[23];
		 size[4] = num['U' - 'A' + 1], size[6] = num['X' - 'A' + 1];
		 size[8] = num['G' - 'A' + 1], size[5] = num['F' - 'A' + 1] - size[4];
		 size[7] = num['S' - 'A' + 1] - size[6]; size[1] = num['O' - 'A' + 1] - size[0] - size[4] - size[2];
		 size[3] = num['H' - 'A' + 1] - size[8]; size[9] = num['I' - 'A' + 1] - size[6] - size[5] - size[8];
		 for (int i = 0; i <= 9; i++)
		 	for (int j = 1; j <= size[i]; j++) 
			printf("%c", '0' + i);
		printf("\n");		 
	}
}	
