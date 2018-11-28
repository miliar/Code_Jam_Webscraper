#include <cstdio>
#include <cstring>

using namespace std;

int main()
{
	int t,T,i,cnt,cntt;
	char pan[200],cur;

	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		scanf("%s",pan);
		for(cnt=0,i=strlen(pan)-1,cur='+';i>=0;i--)
		{
			if(pan[i]!=cur)
				cnt++;
			cur=pan[i];
		}
		for(cntt=1,i=0,cur='-';pan[i]!='\0';i++)
		{
			if(pan[i]!=cur)
				cntt++;
			cur=pan[i];
		}
		if(cntt<cnt)
			cnt=cntt;

		printf("Case #%d: %d\n",t,cnt);
	}
	return 0;
}
