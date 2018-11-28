#include<stdio.h>
#include<stdlib.h>

#define MAX 1009

int main()
{
	int tc,n;
	char s[MAX];
	int standing_till_now,friends_to_invite;
	int i=1,j;

	freopen("large","r",stdin);
	freopen("output","w",stdout);

	scanf("%d",&tc);

	while(i<=tc)
	{
		scanf("%d",&n);
		
		scanf("%s",s);

		j = 1;

		friends_to_invite = 0;
		
		standing_till_now = (s[0]-'0');

		while(s[j]!='\0')
		{
			if(s[j]>'0')
			{
				if(j<=standing_till_now)
				{
					standing_till_now += (s[j]-'0');
				}
				else
				{
					friends_to_invite += (j - standing_till_now);
					standing_till_now += (j - standing_till_now) + (s[j]-'0'); 
				}
			}

			j++;
		}

		printf("Case #%d: %d\n",i,friends_to_invite);
		i++;
	}

}