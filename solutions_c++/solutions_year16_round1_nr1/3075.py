#include<bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	scanf("%d", &t);
	string s;
	for(int x = 1; x <= t; x++)
	{
		cin>>s;

		int l = s.length();
		
		int st=1000, e=1001;
		char a[2500];
		a[1000] = s[0];
		for(int i = 1; i < l; i++)
		{
			if(s[i] >= a[st])
			{
				//printf("df  %c\n", s[i]);
				st--;
				a[st] = s[i];
			}
			else
			{
				a[e++] = s[i];
			}
		}

		printf("Case #%d: ", x);
		for(int i = st; i < e; i++)
			printf("%c", a[i]);
		printf("\n");
	}
	return 0;
}