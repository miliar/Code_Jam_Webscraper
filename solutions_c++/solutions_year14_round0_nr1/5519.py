#include <algorithm>
#include <bitset>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <iomanip>
#include <iterator>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <string.h>
#include <utility>
#include <vector>
using namespace std;
#define exp 1e-9
#define si 40
#define inf 0x3f
#define INF 0x3f3f3f3f
#define loop(n) for(int i=0;i<n;i++)
#define period(s,e) for(int i=s;i<=e;i++)


int T, ans1, card1[4][4],ans2, card2[4][4], ans=0;


int solve(){
	int num=0;
	int x1=ans1-1, x2=ans2-1;
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			if(card1[x1][i]==card2[x2][j]){
				ans=card1[x1][i];
				num++;
				break;
			}
		}
	}
	return num;
}

int main() {
//	freopen("out.txt", "w", stdout);
//	freopen("in.in","r",stdin);
	int y;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		scanf("%d",&ans1);
		for(int i=0;i<4;i++){
			scanf("%d%d%d%d",&card1[i][0],&card1[i][1],&card1[i][2],&card1[i][3]);
		}
		scanf("%d",&ans2);
		for(int i=0;i<4;i++){
			scanf("%d%d%d%d",&card2[i][0],&card2[i][1],&card2[i][2],&card2[i][3]);
		}

		y=solve();
		printf("Case #%d: ",t);
		if(y>1){
			printf("Bad magician!\n");
		}else if(y==0){
			printf("Volunteer cheated!\n");
		}else{
			printf("%d\n",ans);
		}
	}

	return 0;
}