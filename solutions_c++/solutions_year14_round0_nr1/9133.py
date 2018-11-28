#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <sstream>
#include <fstream>
#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <cmath>
#include <deque>
#include <stack>
#include <functional>
#include <numeric>
#include <utility>
#include <iomanip>
#include <ctime>

using namespace std;

#define maxn 110
#define datat int
#define ansdatat int

int n, row_a, row_b, before[maxn][maxn], after[maxn][maxn];

void init_deal(){
}

int main(){
	
	int tttt;
	scanf("%d", &tttt);
	for(int ttt = 1;ttt<=tttt;ttt++){

		scanf("%d", &row_b);
		row_b--;
		for (int i = 0; i<4; i++)
		for (int j = 0; j<4; j++)
		{
			scanf("%d", &before[i][j]);
		}

		scanf("%d", &row_a);
		row_a--;
		for (int i = 0; i<4; i++)
		for (int j = 0; j<4; j++)
		{
			scanf("%d", &after[i][j]);
		}


		int tot = 0, ans_num = -1;
		for (int i = 0; i<4; i++)
			for (int j =0; j<4; j++)
			if(before[row_b][i] == after[row_a][j])
			{
				tot++;
				ans_num = before[row_b][i];
			}


		printf("Case #%d: ",ttt);
		string ans = "";
		if (tot == 0)
		{
			ans = "Volunteer cheated!";
		}
		else
		if (tot > 1)
		{
			ans = "Bad magician!";
		}

		if(ans == ""){
			printf("%d\n", ans_num);
		}
		else{
			cout<<ans<<endl;
		}

	}
	

	return 0;
};

