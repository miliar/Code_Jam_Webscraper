#include<iostream>
#include<algorithm>
#include<list>
using namespace std;

int X,R,C;

const int count3 = 6;
int t3[count3][3][3]=
{
	{
		{1,1,1},
		{0,0,0},
		{0,0,0}
	},
	{
		{1,0,0},
		{1,0,0},
		{1,0,0}
	},
	{
		{1,1,0},
		{1,0,0},
		{0,0,0}
	},
	{
		{1,1,0},
		{0,1,0},
		{0,0,0}
	},
	{
		{1,0,0},
		{1,1,0},
		{0,0,0}
	},
	{
		{0,1,0},
		{1,1,0},
		{0,0,0}
	}
};
const int count4 = 19;
int t4[count4][4][4]=
{
	{//0
		{1,1,0,0},
		{1,1,0,0},
		{0,0,0,0},
		{0,0,0,0}
	},
	{//1
		{1,1,0,0},
		{1,0,0,0},
		{1,0,0,0},
		{0,0,0,0}
	},
	{//2
		{1,1,0,0},
		{0,1,0,0},
		{0,1,0,0},
		{0,0,0,0}
	},
	{//3
		{1,0,0,0},
		{1,0,0,0},
		{1,1,0,0},
		{0,0,0,0}
	},
	{//4
		{0,1,0,0},
		{0,1,0,0},
		{1,1,0,0},
		{0,0,0,0}
	},
	{
		{0,0,1,0},
		{1,1,1,0},
		{0,0,0,0},
		{0,0,0,0}
	},
	{
		{1,0,0,0},
		{1,1,1,0},
		{0,0,0,0},
		{0,0,0,0}
	},
	{//7
		{1,1,1,0},
		{0,0,1,0},
		{0,0,0,0},
		{0,0,0,0}
	},
	{//8
		{1,1,1,0},
		{1,0,0,0},
		{0,0,0,0},
		{0,0,0,0}
	},
	{//9
		{1,0,0,0},
		{1,1,0,0},
		{1,0,0,0},
		{0,0,0,0}
	},
	{
		{0,1,0,0},
		{1,1,0,0},
		{0,1,0,0},
		{0,0,0,0}
	},
	{//11
		{0,1,0,0},
		{1,1,1,0},
		{0,0,0,0},
		{0,0,0,0}
	},
	{
		{1,1,1,0},
		{0,1,0,0},
		{0,0,0,0},
		{0,0,0,0}
	},
	{//13
		{0,1,0,0},
		{1,1,0,0},
		{1,0,0,0},
		{0,0,0,0}
	},
	{
		{1,0,0,0},
		{1,1,0,0},
		{0,1,0,0},
		{0,0,0,0}
	},
	{//15
		{0,1,1,0},
		{1,1,0,0},
		{0,0,0,0},
		{0,0,0,0}
	},
	{
		{1,1,0,0},
		{0,1,1,0},
		{0,0,0,0},
		{0,0,0,0}
	},
	{//17
		{1,0,0,0},
		{1,0,0,0},
		{1,0,0,0},
		{1,0,0,0}
	},
	{//18
		{1,1,1,1},
		{0,0,0,0},
		{0,0,0,0},
		{0,0,0,0}
	}
};


bool flag[10][10];
int p[100];
bool a[100];

bool canSet(int index,int i,int j,int level)
{
	for(int x = 0; x < level; x++)
		for(int y = 0; y < level; y++)
		{
			if(level==3 && t3[index][x][y])
				if(x+i>=R || y+j >= C || flag[x+i][y+j]) return false;
			if(level==4 && t4[index][x][y])
				if(x+i>=R || y+j >= C || flag[x+i][y+j]) return false;
		}
	return true;
}
void set(int index,int i,int j,bool value,int level)
{
	for(int x = 0; x < level; x++)
		for(int y = 0; y < level; y++)
		{
			if(level == 3 && t3[index][x][y])	flag[x+i][y+j]=value;
			if(level == 4 && t4[index][x][y])	flag[x+i][y+j]=value;
		}
}



bool check()
{
	for(int i= 0; i < R; i++)
		for(int j = 0; j < C; j++)
			if(!flag[i][j]) return false;
	return true;
}

void go(int level,int count, int i,int j)
{
	if(j == C) 
	{
		i++;
		j=0;
	}
	if(i==R && check())
	{
		for(int i = 0; i < count; i++) 
		{
		//	if(p[i]) printf("%d ",i);
			if(p[i]) a[i] = true;
		}
		//printf("\n");
		return;
	}
	if(i == R) return;
	if(flag[i][j]) 
	{
		go(level,count, i,j+1);
		return;
	}
	for(int z = 0; z < count; z++)
	{
		if(!canSet(z,i,j,level)) continue;
		p[z]++;
		set(z,i,j,true,level);
		go(level,count,i,j+1);
		p[z]--;
		set(z,i,j,false,level);
	}
}

void init()
{
	for(int i = 0; i <100; i++) a[i]=false;
}

void solve(int test)
{
	init();
	scanf("%d%d%d",&X,&R,&C);
	if(R< C) swap(R,C);
	if(X == 1) 
	{
		printf("Case #%d: GABRIEL\n",test);
		return;
	}
	if(X == 2) 
	{
		if(R%2==0 ||C%2==0)	printf("Case #%d: GABRIEL\n",test);
		else printf("Case #%d: RICHARD\n",test);
		return;
	}
	if(X==3)
	{
		go(3,count3,0,0);
		bool answer = (a[0]||a[1]) && (a[2] || a[3] || a[4] ||a[5]);
		if(answer) printf("Case #%d: GABRIEL\n",test);
		else printf("Case #%d: RICHARD\n",test);
		return;
	}
	if(R<=3||C <=2) printf("Case #%d: RICHARD\n",test);
	else
	{
		
		printf("Case #%d: GABRIEL\n",test);
	}



}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	int i,T;
	scanf("%d",&T);
	for(i=1; i <=T; i++) solve(i);
	return 0;
}