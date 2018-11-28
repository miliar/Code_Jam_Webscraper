/* Standing Ovation
 * CodeJam 2015
 * Google
 * Date : 11/04/2015
 */
#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<cstring>

using namespace std;
const int MAX = 1002;

int friendsInvited(char *s,int n)
{
	int currentlyStanding,friendsInvited;
	currentlyStanding = 0;
	friendsInvited = 0;
	for(int i=0;i<=n;i++)
	{
		if(s[i] != '0')
		{
			if(currentlyStanding >= i)
			{
				currentlyStanding += s[i] - '0';
			}
			else
			{
				//adding friends
				friendsInvited += i - currentlyStanding;
				currentlyStanding += (s[i] - '0') + friendsInvited;
			}
		}
//		cout<<"i :"<<i<<" CS : "<<currentlyStanding<<" FI:"<<friendsInvited<<endl;
	}
	return friendsInvited;
}

int main(void)
{
	int t,sMax;
	char s[MAX];
	
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		scanf("%d",&sMax);
		scanf("%s",s);
		printf("Case #%d: %d\n",i,friendsInvited(s,sMax));
	}

	return 0;
}
/********************************* END OF PROGRAM **************************/
