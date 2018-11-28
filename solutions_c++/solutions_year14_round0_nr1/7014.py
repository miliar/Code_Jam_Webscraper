#include<stdio.h>
#include<set>
using namespace std;
set<int> st;
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int q,T,i,j,r1,r2,b1[5][5],b2[5][5];
	scanf("%d",&T);
	for(q=1;q<=T;q++)
	{
		scanf("%d",&r1);
		r1--;
		for(i=0;i<4;i++)for(j=0;j<4;j++)scanf("%d",&b1[i][j]);
		scanf("%d",&r2);
		r2--;
		for(i=0;i<4;i++)for(j=0;j<4;j++)scanf("%d",&b2[i][j]);
		st.clear();
		for(i=0;i<4;i++)for(j=0;j<4;j++){if(b1[r1][i]==b2[r2][j])st.insert(b1[r1][i]);}
		if(st.size()==0)printf("Case #%d: Volunteer cheated!\n",q);
		else if(st.size()>1)printf("Case #%d: Bad magician!\n",q);
		else printf("Case #%d: %d\n",q,*st.begin());
	}
	return 0;
}