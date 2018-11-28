#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;
const int MAXN = 1005;
char str[MAXN];
char tmp[MAXN];
bool used[MAXN];
int main()
{
	int T,cas,i,j;
	scanf("%d",&T);
	for (cas = 1; cas <= T; ++cas)
	{
		scanf("%s",str);
		int len = strlen(str);
		strcpy(tmp,str);
		sort(tmp,tmp+len);	
		for (i = 1; i < len; ++i)
		{
			int mx_index = 0;
			if (str[i] >= str[0])
				mx_index = i;
			char mx_c = str[mx_index];
			for (j = mx_index; j > 0; --j)
				str[j] = str[j-1];
			str[0] = mx_c;
		}
		printf("Case #%d: %s\n",cas,str);
	}
	return 0;
}