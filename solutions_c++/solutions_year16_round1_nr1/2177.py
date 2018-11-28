#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<algorithm>
#include<math.h>
#include<vector>
#include<string.h>

using namespace std;
char str[1005];

int main()
{
	//freopen("A-small-attempt0.in", "rt", stdin);
	//freopen("test.in", "rt", stdin);
	freopen("A-large.in", "rt", stdin);
	freopen("a-large.out", "wt", stdout);
	int inp, kase, i, j, k, n, tmp;
	scanf("%d", &inp);
	for(kase = 1; kase <= inp; kase++)
	{
		scanf("%s", str);
		//fprintf(stderr, "%s\n", str);
		string res = "";
		res = res +  str[0];
		int len = strlen(str);
		for(i = 1; i < len; i++)
		{
			//fprintf(stderr, "%s\n", res.c_str());
			if(str[i] >= res[0])
			{
				string s = "";
				s += str[i];
				res = s + res;
			}
			else
			{
				res = res + str[i];
			}
		}
		printf("Case #%d: %s\n", kase, res.c_str());
	
		
	}
	return 0;
}
