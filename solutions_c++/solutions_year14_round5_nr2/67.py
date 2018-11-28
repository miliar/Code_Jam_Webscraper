#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

int HP[111];
int Gold[111];

int F[111][2222];

int main(void)
{
	int T = 0;
	int TK = 0;
	scanf("%d",&T);
	while(T--)
	{
		printf("Case #%d: ",++TK);
		int herAtk = 0;
		int towerAtk = 0;
		int N = 0;
		scanf("%d %d %d",&herAtk,&towerAtk,&N);
		for(int i = 0;i < N;i++) scanf("%d %d",&HP[i],&Gold[i]);
		memset(F,0xCC,sizeof(F));
		F[0][1] = 0;
		for(int i = 0;i < N;i++)
		{
			int shizuku = HP[i]/towerAtk + (HP[i]%towerAtk != 0);
			for(int j = 0;j < 1111;j++)
			{
				// tower first
				for(int k = 0;k*towerAtk <= HP[i];k++)
				{
					if(HP[i]-k*towerAtk <= 0) break;
					int need = (HP[i]-k*towerAtk) / herAtk + ((HP[i]-k*towerAtk)%herAtk != 0);
					int give = k;
					if(give + j >= need)
					{
						F[i+1][give + j - need] = max(F[i+1][give + j - need], F[i][j]+Gold[i]);
					}
				}

				F[i+1][j+shizuku] = max(F[i+1][j+shizuku], F[i][j]); // not
			}
		}
		int ans = 0;
		for(int j = 0;j < 1111;j++) ans = max(ans,F[N][j]);
		printf("%d\n",ans);
	}
	while(getchar() != EOF);
	return 0;
}
