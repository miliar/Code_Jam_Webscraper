// MagicTrickCPP.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


int _tmain(int argc, _TCHAR* argv[])
{
		int t;
	scanf("%d", &t);
	for(int tt = 1; tt <= t; tt++){
		bool card[20] = {};
		int row, r[5], kk;
		scanf("%d", &row);
		for(int i=1; i<=4; i++) for(int j=0; j<4; j++) if(i == row) { scanf("%d", &r[j]); card[r[j]] = 1; } else scanf("%d", &kk);
		scanf("%d", &row);
		int ans = 0, num;
		for(int i=1; i<=4; i++)
			{for(int j=0; j<4; j++)
				{if(i == row) {
					scanf("%d", &r[j]);
					if(card[r[j]])
						{
							ans++; 
							num = r[j];
						}
				} 
				else
					scanf("%d", &kk);
		}
		}
		if(!ans)
			printf("Case #%d: Volunteer cheated!\n", tt);
		else if(ans == 1) printf("Case #%d: %d\n", tt, num);
		else printf("Case #%d: Bad magician!\n", tt);
	}
}