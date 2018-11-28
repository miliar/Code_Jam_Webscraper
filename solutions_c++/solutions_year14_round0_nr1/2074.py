#include<iostream>
#define rep(i,n) for (int i=0;i<n;i++)
#define For(i,a,b) for (int i=a;i<=b;i++)
using namespace std;
int pos1[20],pos2[20],a[4][4],b[4][4];
int ans1,ans2;
int caseNum=0;
void init(){
	scanf("%d",&ans1);
	--ans1;
	rep(i,4)
		rep(j,4)
		{
			int temp;
			scanf("%d",&temp);
			a[i][j]=temp;
			pos1[temp]=i*4+j;
		}
	scanf("%d",&ans2);
	--ans2;
	rep(i,4)
		rep(j,4)
		{
			int temp;
			scanf("%d",&temp);
			b[i][j]=temp;
			pos2[temp]=i*4+j;
		}
}

void mainProcess()
{
	int findCnt=0,ansNum=0;
	rep(i,4)
	{
		rep(j,4)
			if (a[ans1][i]==b[ans2][j])
			{
				ansNum=a[ans1][i];
				++findCnt;
			}
	}
	++caseNum;
	if (findCnt == 0)
		printf("Case #%d: Volunteer cheated!\n",caseNum);
	else
	{
		if (findCnt == 1)
			printf("Case #%d: %d\n",caseNum,ansNum);
		else 
			printf("Case #%d: Bad magician!\n",caseNum);
	}
}

int main(){
	int test;
	scanf("%d",&test);
	rep(testnum,test)
	{
		init();
		mainProcess();
	}
	return 0;
}
