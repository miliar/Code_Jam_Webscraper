#include<bits/stdc++.h>
using namespace std;
char str[105];
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int p=1;p<=t;p++){
		printf("Case #%d: ", p);
		scanf("%s", str);
		int l=strlen(str), cnt=0;
		for(int i=1;i<l;i++)
			if(str[i]!=str[i-1])
				cnt++;
		if(str[l-1]=='-')
			cnt++;
		printf("%d\n", cnt);
	}
}