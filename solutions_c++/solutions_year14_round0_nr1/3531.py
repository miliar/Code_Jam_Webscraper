#include<stdio.h>
#include<vector>
using namespace std;
int tab1[17],tab2[17];
int main()
{
    int zes;scanf("%d",&zes);
    for (int k=0;k<zes;k++)
    {
	int r1,r2;
	int t1[4][4],t2[4][4];
	scanf("%d",&r1);
	for (int i=0;i<4;i++)
	    for (int j=0;j<4;j++)
	    {
		scanf("%d",&t1[i][j]);
		tab1[t1[i][j]] = i;
	    }
	scanf("%d",&r2);
	for (int i=0;i<4;i++)
	    for (int j=0;j<4;j++)
	    {
		scanf("%d",&t2[i][j]);
		tab2[t2[i][j]]=i;
	    }
	r1--;r2--;
	vector<int> res;
	for (int i=1;i<=16;i++)
	    if(tab1[i] == r1 && tab2[i]==r2) res.push_back(i);
	if(res.size()==0)
	{
	    printf("Case #%d: Volunteer cheated!\n",k+1);
	}
	else if(res.size()==1)
	{
	    printf("Case #%d: %d\n",k+1,res[0]);
	}
	else
	{
	    printf("Case #%d: Bad magician!\n",k+1);

	}


    }
}
