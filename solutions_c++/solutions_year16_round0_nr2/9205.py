

#include<cstdio>
#include<cmath>
#include<cstring>
#include<string>
#include<iostream>
#include<algorithm>

using namespace std;

int main()
{
	freopen("B-large.in","r",stdin);
	//freopen("B-large.txt","w",stdout);
	int t,r;
	char s[101],cur;
	scanf("%d",&t);
	for(int i=1;i<=t;i++){
		scanf("%*c%s",s);
		r=1;
		cur=s[0];
		for(int i=1;i<strlen(s);i++)
			if(s[i]!=cur){
				r++;
				cur=s[i];
			}
		if(s[strlen(s)-1]=='-')
			printf("Case #%d: %d\n",i,r);
		else
		printf("Case #%d: %d\n",i,r-1);
	}
	return 0;
}
