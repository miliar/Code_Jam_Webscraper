#include <iostream>
#include <stdio.h>
using namespace std;
int card1[5][5],card2[5][5];
int i,j,T,f,s,t,count,ans;
int main()
{
	
	//FILE * fout = fopen("A-small-attempt0.out","w");
	freopen("A-small-attempt2.in","r",stdin);
	freopen("A-small-attempt2.out","w",stdout);
	cin>>T;
	for(t=1; t<=T; t++)
	{
		ans = count = 0;
		cin>>f;
		for(i=1; i<5; i++)
			for(j=1; j<5; j++)
				cin>>card1[i][j];
		cin>>s;
		for(i=1; i<5; i++)
			for(j=1; j<5; j++)
				cin>>card2[i][j];
		for(i=1; i<5; i++)
		{		for(j=1; j<5; j++)
			{	
				if(card1[f][i] ==  card2[s][j])
				{
					count++;
					ans = card1[f][i];
				}
			}
		}
		if(!count) printf("Case #%d: Volunteer cheated!\n",t);
		else if(count>1) printf("Case #%d: Bad magician!\n",t);
		else printf("Case #%d: %d\n",t,ans);

	}	
	

}