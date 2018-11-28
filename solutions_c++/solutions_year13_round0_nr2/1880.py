/*-------------------------------------------------------------*/
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <queue>
#include <cmath>
#include <fstream>
#include <stdio.h>
#include <stack>
#include <memory.h>

using namespace std;

#define memset0(x) memset((x),0,sizeof(x)) // 0
#define memsetN(x) memset((x),-1,sizeof(x))  // 0xffffffff = -1
#define memsetM(x) memset((x),0x3f,sizeof(x)) // 0x3f3f3f3f = 1061109567
typedef long long llg;

template<class T>inline void OUTLN(T &arr,int len){
	for(int i=0;i < len;i++)
		cout << arr[i] << " ";
	cout << endl;
}

#define MOD 1000000009
#define EPS 1e-6

/*--------------------------------------------------------------*/

const int maxn=100+2;

int mat[maxn][maxn];
int rm[maxn];
int cm[maxn];
int r,c;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	//freopen("in.txt","r",stdin);
	int T;
	cin >> T;
	int ca=1;
	while(T--){
		memset0(rm);
		memset0(cm);
		scanf("%d%d",&r,&c);
		for(int i=0;i < r;i++)
			for(int j=0;j < c;j++){
				scanf("%d",&mat[i][j]);
				rm[i] = max(rm[i],mat[i][j]);
				cm[j] = max(cm[j],mat[i][j]);
			}
		bool flag=true;
		for(int i=0;i < r;i++){
			if(!flag) break;
			for(int j=0;j < c;j++){
				if(mat[i][j] < rm[i] && mat[i][j] < cm[j]){
					flag=false;
					break;
				}
			}
		}
		const char *str=(flag?"YES":"NO");
		printf("Case #%d: %s\n",ca++,str);
	}
	return 0;
}
