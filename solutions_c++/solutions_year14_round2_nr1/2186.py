#include<bits/stdc++.h>
int main()
{
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("my.out", "w", stdout);
	int t1,n,i,l,k,t,p,ans,j,x,z=1;
	char c;
	scanf("%d",&t1);
	while(t1--) {
		ans=0;
		scanf("%d",&n);
		char str[n][109];
		char str1[n][109];
		int array[n][109];
		for(i=0;i<n;i++) {
			scanf("%s",str[i]);
		}
		for(i=0;i<n;i++) {
			k=0;
			p=0;
			l=strlen(str[i]);
			c=str[i][0];
			str1[i][k++]=c;
			t=1;
			for(j=1;j<l;j++) {
				if(str[i][j]!=c) {
					array[i][p++]=t;
					t=1;
					str1[i][k++]=str[i][j];
					c=str[i][j];
				}
				else {
					t++;
				}
			}
			array[i][p]=t;
			str1[i][k]='\0';
		}
		if(strcmp(str1[0],str1[1])!=0) {
			printf("Case #%d: Fegla Won\n",z++);
		}
		else {
			l=strlen(str1[0]);
			for(i=0;i<l;i++) {
				x=abs(array[0][i]-array[1][i]);
				ans+=x;
			}
			printf("Case #%d: %d\n",z++,ans);
		}
	}
	return 0;
}
