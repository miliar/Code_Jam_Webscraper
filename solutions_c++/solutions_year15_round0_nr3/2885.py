#include <stdio.h>
#include <stdlib.h>
#define gc getchar_unlocked

using namespace std;
int a[4][4]={{1,2,3,4}
	    ,{2,-1,4,-3},
	     {3,-4,-1,2},
	     {4,3,-2,-1}};

int get(char c)
{
	if(c=='i')
		return 2;
	if(c=='j')
		return 3;
	if(c=='k')
		return 4;
}
int main()
{
	int t,l,row,col,cnt,ans; 
	long int x;
	long long int len;
	char s[10001];
	scanf("%d",&t);
	for(int x1=1;x1<=t;++x1)
	{
		cnt=0;
		scanf("%d",&l);
		scanf("%ld",&x);
		scanf("%s",s);
		len=x*l;
		row=get(s[0]);
		for(int i=1;i<len;++i)
		{
			col=get(s[i%l]);
			ans=a[(int)abs(row)-1][(int)abs(col)-1];
			if(row<0)
			{
				if(ans<0)
					ans=abs(ans);
				else
					ans=0-ans;
			}
			if(cnt==0 && ans==2)
			{
				++cnt;
				row=get(s[++i%l]);
			}
			else if(cnt==0 && row==2)
			{
				++cnt;
				row=get(s[i%l]);
			}
			else if(cnt==1 && ans==3)
			{
				cnt++;
				row=get(s[++i%l]);
			}
			else if(cnt==1 && row==3)
			{
				cnt++;
				row=get(s[i%l]);
			}
			else
				row=ans;
		}
		if(cnt==2 && (ans==4 || row==4))
			printf("Case #%d: YES\n",x1);
		else
			printf("Case #%d: NO\n",x1);
	}
	return 0;
}
