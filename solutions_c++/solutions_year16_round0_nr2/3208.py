#include <stdio.h>
#include <string.h>

#define MINUS false
#define PLUS true

int T;
char arr[110];
bool status;
int ans;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	
	scanf("%d", &T);
	for(int cs = 1; cs <= T; cs++)
	{
		memset(arr, 0, sizeof(int) * 20);
		scanf("%s", arr);
		arr[0] == '-' ? status = MINUS : status = PLUS;
		ans = 0;

		int i = 0;
		while(arr[i] != '\0')
		{
			while(arr[i] == arr[i+1])
			{
				i++;
			}

			if(arr[i+1] == '\0')
			{
				if(status == PLUS && arr[i] == '+')
				{
					break;
				}
				else if(status == MINUS && arr[i] == '-')
				{
					ans++;
					break;
				}
				else
				{
					ans += 2;
					break;
				}
			}
			else
			{
				status = !status;
				ans++;
				i++;
			}
		}
		
		printf("Case #%d: %d \n", cs, ans);
	}
}