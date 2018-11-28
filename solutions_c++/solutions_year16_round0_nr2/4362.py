#include<cstdio>
#include <cstring>

int main()
{
	char str[110];
	int ti,tc;
	
	scanf("%d", &tc);
	for (ti = 1; ti <=tc;++ti) {
		scanf("%s",str);
		int n = strlen(str),i,j;
		//printf("input is %s len %d\n", str,n);
		int count = 0;
		for (i= n-1;i>=0;--i) {
			if (str[i] == '-') {
				count++;
				for (j=i;j>=0;--j) {
					if (str[j]=='-')
						str[j]='+';
					else
						str[j]='-';
								
				}
			}
		}
		printf("Case #%d: %d\n",ti, count);
	}
	
}
