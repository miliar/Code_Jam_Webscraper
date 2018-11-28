#include<cstdio>
#include<cstring>
#include<vector>
using namespace std;

#define pb push_back

int main()
{
	int t, ans1, ans2, g1[5][5], g2[5][5], can[20];

	scanf("%d", &t);
	for(int tc=1; tc<=t; ++tc)
	{
		scanf("%d", &ans1);
		for(int i=0; i<4; ++i)
			for(int j=0; j<4; ++j)
				scanf("%d", &g1[i][j]);
		scanf("%d", &ans2);
		for(int i=0; i<4; ++i)
			for(int j=0; j<4; ++j)
				scanf("%d", &g2[i][j]);
		--ans1; --ans2;

		vector<int> out;
		memset(can, 0, sizeof(can));
		for(int j=0; j<4; ++j) can[g1[ans1][j]] = 1;
		for(int j=0; j<4; ++j)
			if(can[g2[ans2][j]])
				out.pb(g2[ans2][j]);
		
		printf("Case #%d: ", tc);
		if(out.empty()) puts("Volunteer cheated!");
		else if(out.size() > 1) puts("Bad magician!");
		else printf("%d\n", out[0]);
	}

	return 0;
}
