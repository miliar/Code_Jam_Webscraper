#include <cstdio>
#include <algorithm>
#include <array>
#include <cstring>
using namespace std;

char* noPoint(int R, int C, int x, int y, char RC[100][100]){
	static char s[10]="";
	int index=0;
	for(int i=0;i<10;++i)
		s[i]=0;
	for(int y2=0;y2<R;++y2){
		if(y2==y)
			continue;
		if(RC[x][y2]!='.'){
			if(y>y2){
				s[index]='^';
				++index;
				y2=y;
			}
			else{
				s[index]='v';
				++index;
				break;
			}
		}
	}
	for(int x2=0;x2<C;++x2){
		if(x2==x)
			continue;
		if(RC[x2][y]!='.'){
			if(x>x2){
				s[index]='<';
				++index;
				x2=x;
			}
			else{
				s[index]='>';
				++index;
				break;
			}
		}
	}
	if(s[0]==0)
		s[0]='.';
	return s;
}

void solve(int R, int C, char RC[100][100]){
	int ans=0;
	for(int y=0;y<R;++y){
		for(int x=0;x<C;++x){
			if(RC[x][y]=='.')
				continue;
			char* a=noPoint(R, C, x, y, RC);
			//printf("%d %d %s\n", x, y, a);
			if(a[0]=='.'){
				printf(" IMPOSSIBLE\n");
				return;
			}
			int flag=0;
			for(int i=0;i<5;++i){
				if(a[i]==RC[x][y]){
					flag=1;
					break;
				}
			}
			if(!flag)
				++ans;
		}
	}
	printf(" %d\n", ans);
}

void parse(void){
	int result;
	int R, C;
	char RC[100][100];
	result=scanf("%d%d", &R, &C);
	for(int y=0;y<R;++y){
		for(int x=0;x<C;++x){
			result=scanf("%c", &RC[x][y]);
			if(RC[x][y]=='\n')
				--x;
		}
	}
	solve(R, C, RC);
	static_cast<void>(result);
}

int main(void){
	int test;
	int result=scanf("%d", &test);
	for(int i=1;i<=test;++i){
		printf("Case #%d:", i);
		parse();
	}
	static_cast<void>(result);
	return 0;
}
