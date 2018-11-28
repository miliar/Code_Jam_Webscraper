#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <string.h>
#include <stdlib.h>
#include <queue>
#include <time.h>

using namespace std;

#define writeFile(name) freopen(name,"w",stdout)
#define readFile(name) freopen(name,"r",stdin)

using namespace std;

int main(){
	readFile("in.in");
	writeFile("out.out");
	int T;
	cin >> T;
	for (int Z = 0; Z < T; Z++)
	{
		int H,W;
		cin >> H >> W;
		vector<vector<int> > map(H,vector<int>(W,0));
		for (int i = 0; i < H; i++)
		{
			for (int j = 0; j < W; j++)
			{
				int n;
				cin >> n;
				map[i][j] = n;
			}
		}
		bool notWorking = false;
		for (int i = 0; i < H; i++)
		{
			for (int j = 0; j < W; j++)
			{
				bool canWork = true;
				int cur = map[i][j];
				for (int ii = 0; ii < W; ii++)
				{
					if(map[i][ii] > cur){
						canWork = false;
						break;
					}
				}
				bool canWork2 = true;
				for (int ii = 0; ii < H; ii++)
				{
					if(map[ii][j] > cur){
						canWork2 = false;
						break;
					}
				}
				if(!(canWork || canWork2)){
					notWorking = true;
					break;
				}
			}
			if(notWorking)
				break;
		}
		printf("Case #%d: ",Z+1);
		if(notWorking){
			printf("NO\n");
		}
		else{
			printf("YES\n");
		}
	}
}