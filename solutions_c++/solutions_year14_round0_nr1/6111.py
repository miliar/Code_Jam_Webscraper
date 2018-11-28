/*
	iafir
*/
#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <utility>
using namespace std;

int tc,row1[4],row2[4],nsame,nrow,r1,r2,t;

int main()
{
//	freopen("in.txt","r",stdin);
//	freopen("out.txt","w",stdout);
	scanf("%d",&tc); t=1;
	while(t<=tc)
	{
		scanf("%d",&nrow);
		for(int i=0; i<4; i++)
		{
			if(i+1 == nrow)
				scanf("%d%d%d%d",&row1[0],&row1[1],&row1[2],&row1[3]);
			else
				scanf("%*d%*d%*d%*d");
		}
		scanf("%d",&nrow);
		for(int i=0; i<4; i++)
		{
			if(i+1 == nrow)
				scanf("%d%d%d%d",&row2[0],&row2[1],&row2[2],&row2[3]);
			else
				scanf("%*d%*d%*d%*d");
		}
		sort(row1,row1+4);
		sort(row2,row2+4);
		r1 = r2 = nsame = 0;
		while(r1<4 && r2<4)
		{
			if(row1[r1]<row2[r2])
				r1++;
			else if(row1[r1]>row2[r2])
				r2++;
			else
			{
				nrow = r1; r1++; r2++; nsame++;
			}
		}
		if(nsame==0)
			printf("Case #%d: Volunteer cheated!\n",t);
		else if(nsame==1)
			printf("Case #%d: %d\n",t,row1[nrow]);
		else
			printf("Case #%d: Bad magician!\n",t);
		t++;
	}
	
	return 0;
}
