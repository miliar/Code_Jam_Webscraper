#include <cstdio>
#include <vector>

using namespace std;

const int MAXX=100,MAXH=100;

int map[MAXX][MAXX];
int X,Y;
bool vux[MAXX],vuy[MAXX];

void pb(){
	scanf("%d%d",&Y,&X);
	for (int y=0;y<Y;y++)
		for (int x=0;x<X;x++)
			scanf("%d",&map[x][y]);
	for (int h=MAXH-1;h>=1;h--){
		fill(vux,vux+MAXX,false);
		fill(vuy,vuy+MAXX,false);
		for (int x=0;x<X;x++)
			for (int y=0;y<Y;y++)
				if (map[x][y]>h){
					vux[x]=true;
					vuy[y]=true;
				}
		for (int x=0;x<X;x++)
			for (int y=0;y<Y;y++)
				if (map[x][y]<=h && vux[x] && vuy[y]){
					puts("NO");
					return;
				}

	}
	puts("YES");
}

int main(){
	int T;
	scanf("%d",&T);
	for (int i=0;i<T;i++){
		printf("Case #%d: ",i+1);
		pb();
	}
	return 0;
}
