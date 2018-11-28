#include<algorithm>
#include<cmath>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<map>
#include<queue>
#include<stack>
#include<vector>
using namespace std;

#define	gi(a)		scanf("%d",&a)
#define	Int(a)		int a;ri(a);
#define Pair		pair <int,int>
#define mp		make_pair
#define ll		long long
#define INF		2147483647
#define clr(a)		memset(a,0,sizeof(a))
#define dbg(x) 		cerr<<#x<<" ="<<(x)<<endl
#define max(a,b)	(a>b)?a:b
#define min(a,b)	(a<b)?a:b
#define min3(a,b,c)	(a<min(b,c))?a:min(b,c)
#define pb		push_back

template <class T>
inline void ri(T &i){
	bool minus=false;
	char c;
	for(c=getchar();(c<'0'||c>'9')&&(c!='-');
		      c=getchar());
	if(c=='-')
		      {minus=true;c='0';}
	for(i=0;c>='0'&&c<='9';c=getchar())
		      i=(i<<3)+(i<<1)+(c-48);
	if(minus)i=(~i)+1;
}
int main(){
	int i,j,k;
	int m,n;
	int C=1;
	Int(t);
	while(t--){
		char grid[4][4];
		bool incomplete=false;
		for(i=0;i<4;i++){
			scanf("%s",grid[i]);
			for(j=0;j<4;j++)
				if(grid[i][j]=='.')
					incomplete=true;
		}
		bool Xwon=false,Ywon=false,tmp,tmp2;
		for(i=0;i<4;i++){
			tmp=true;
			tmp2=true;
			for(j=0;j<4;j++){
				tmp &= ((grid[i][j]=='X')||(grid[i][j]=='T'));
				tmp2 &= ((grid[i][j]=='O')||(grid[i][j]=='T'));
			}
			Xwon|=tmp;
			Ywon|=tmp2;
		}
		for(i=0;i<4;i++){
			tmp=true;
			tmp2=true;
			for(j=0;j<4;j++){
				tmp &= ((grid[j][i]=='X')||(grid[j][i]=='T'));
				tmp2 &= ((grid[j][i]=='O')||(grid[j][i]=='T'));
			}
			Xwon|=tmp;
			Ywon|=tmp2;
		}
		tmp=tmp2=true;
		for(i=0;i<4;i++){
			tmp &= ((grid[i][i]=='X')||(grid[i][i]=='T'));
			tmp2 &= ((grid[i][i]=='O')||(grid[i][i]=='T'));
		}
		Xwon|=tmp;
		Ywon|=tmp2;
		tmp=tmp2=true;
		for(i=0;i<4;i++){
			tmp &= ((grid[i][3-i]=='X')||(grid[i][3-i]=='T'));
			tmp2 &= ((grid[i][3-i]=='O')||(grid[i][3-i]=='T'));
		}
		Xwon|=tmp;
		Ywon|=tmp2;
		if(Xwon){
			printf("Case #%d: X won\n",C);
		}
		else if(Ywon){
			printf("Case #%d: O won\n",C);
		}
		else if(incomplete){
			printf("Case #%d: Game has not completed\n",C);
		}
		else
			printf("Case #%d: Draw\n",C);
		C++;
	}
	return 0;
}
