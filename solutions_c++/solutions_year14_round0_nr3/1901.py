#include <stdio.h>
#include <memory.h>

int n,m,r;

bool flag;
int a[30];

bool map[10][10];
bool check[10][10];

int cp;

int d_y[8]={0,1,1,1,0,-1,-1,-1},d_x[8]={1,1,0,-1,-1,-1,0,1};

void input()
{
	scanf("%d %d %d",&n,&m,&r);
}

bool zerocheck(int y, int x)
{
	int i;
	for(int i=0; i<8; i++) {
		if(map[y+d_y[i]][x+d_x[i]]) return false;
	}
	return true;
}

bool func(int y, int x)
{
	int front=0,rear=1,q[30][2];
	q[rear][0]=y;
	q[rear][1]=x;
	check[y][x]=true;
	while(front<rear) 
	{
		front++;
		y=q[front][0];
		x=q[front][1];
		if(zerocheck(y,x)) {
			for(int i=0; i<8; i++) {
				int ty=y+d_y[i];
				int tx=x+d_x[i];
				if(ty>0 && ty<=n && tx>0 && tx<=m && !map[ty][tx] && !check[ty][tx])
				{
					rear++;
					q[rear][0]=ty;
					q[rear][1]=tx;
					check[ty][tx]=true;
				}
			}
		}
	}
	return (rear == n*m-r);
}

bool click_check()
{
	memset(map,0,sizeof(map));
	for(int i=1; i<=r; i++) map[(a[i]-1)/m+1][(a[i]-1)%m+1]=true;
	for(int i=1; i<=n; i++) {
		for(int j=1; j<=m; j++) {
			if(!map[i][j]) {
				memset(check,0,sizeof(check));
				if(func(i,j)) {
					cp=(i-1)*m+j;
					return true;
				}
			}
		}
	}
	return false;
}

void go_check(int lev, int i)
{
	if(flag) return;
	if(lev>r) {
		if(click_check()) {
			for(int i=1; i<=n; i++) {
				for(int j=1; j<=m; j++) {
					if((i-1)*m+j==cp) printf("c");
					else {
						if(map[i][j]) printf("*");
						else printf(".");
					}
				}
				printf("\n");
			}
			flag=true;
		}
		return;
	}

	for(;i<=n*m;i++) {
		a[lev]=i;
		go_check(lev+1,i+1);
	}
}

void process()
{
	flag=false;
	go_check(1,1);
	if(!flag) printf("Impossible\n");

}

int main()
{
	freopen("C-small-attempt0.in","rt",stdin);
	freopen("C-small-attempt0.out","wt",stdout);
	int t;
	scanf("%d",&t);
	for(int i=1; i<=t; i++) {
		printf("Case #%d:\n",i);
		input();
		process();
	}
}