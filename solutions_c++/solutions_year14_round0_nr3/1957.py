#include <vector>
#include <algorithm>
#include <cstdio>
#define MAXR 5
#define MAXC 5
#define MAXM 150
using namespace std;

int d[8];
bool disc[MAXR*MAXC];
int r,m,c,win,n,t;
vector <int> q;


void printt()
{
	for(int i=0; i<r*c; i++)
	{
		if(i == win)
			printf("c");
		else if(q[i] == true)
			printf("*");
		else
			printf(".");
		if((i+1) % c == 0)
			printf("\n");
	}
}

int abs(int a)
{
	if (a<0)
		return -a;
	return a;
}
void printtdisc()
{
	for(int i=0; i<r*c; i++)
	{
		printf("%d", disc[i]);
		if((i+1) % c == 0)
			printf("\n");
	}
}

void printtq()
{
	for(int i=0; i<r*c; i++)
	{
		printf("%d", q[i]);
		if((i+1) % c == 0)
			printf("\n");
	}
}



bool isvalid(int x)
{
	return x>=0 && x<r*c;
}

bool isneigh(int a, int b)
{
	int x1,x2,y1,y2;
	x1 = a/c;
	x2 = b/c;
	y1 = a%c;
	y2 = b%c;
	if(abs(x1-x2) <= 1 && abs(y1-y2) <= 1)
		return true;
	//printf("uppppps\n");
	return false;
}

int neigh(int x)
{
	int wyn = 0;
	for(int i=0; i<8; i++)
		if( isvalid(x+d[i]) && isneigh(x, x+d[i]) && q[x+d[i]] == 1)
			wyn++;
	return wyn;
}

void discover(int x)
{
	disc[x] = true;
	if(neigh(x) == 0)
		for(int i=0; i<8; i++)
			if(isvalid(x+d[i]) && isneigh(x, x+d[i]) && !disc[x+d[i]] && !q[x+d[i]])
			{
			//	printf("from %d: %d (%d)\n", x, x+d[i], d[i]);
				discover(x+d[i]);
			}
}

void lost()
{
	printf("Case #%d:\nImpossible\n", t);
}

void won()
{
	printf("Case #%d:\n", t);
	printt();
}

bool solve()
{
	for(int i=0; i<r*c; i++)
		disc[i] = false;
	win = -1;
	for(int i=0; i<r*c; i++)
		if(q[i] == false && neigh(i) == 0)
		{
			win = i;
			//printf("win = %d\n", win);
			break;
		}
	if(win == -1)
	{
		//printf("!!!!!!");
		if(r*c - m > 1)
			return false;
		else
		{
			win = 0;
			return true;
		}
	}
	//printf("?%d\n", win);
	discover(win);
	int cnt = 0;
	for(int i=0; i<r*c; i++)
		if(disc[i] == true)
			cnt++;
	if(cnt < r*c - m)
		return false;
	else
		return true;
}

void compute()
{
	for(int i=r*c-1; r*c-i-1 < m; i--)
		q[i] = true;
	do
	{
		//printf("?!?!\n"); 
		//printt();

		//while(1);
		if(solve())
		{
			won();
			//printtdisc();
			return;
		}
		//printt();
		//puts("");
		//printtq();
		//printf("_________________________\n");
	} while(next_permutation(q.begin(), q.end()));

	lost();
	return;
}

int main()
{
	scanf("%d", &n);
	t = 0;
	while(t++ < n)
	{
		q.clear();
		scanf("%d%d%d", &r, &c, &m);
		q.resize(r*c, 0);
		/*for(int i=0; i<r*c; i++)
			if(i<m)
				q.push_back(1);
			else
				q.push_back(0);
		*/
		d[0] = -1;
		d[1] = 1;
		d[2] = c;
		d[3] = -c;
		d[4] = c-1;
		d[5] = c+1;
		d[6] = -c-1;
		d[7] = -c+1;
		if(c==1)
			d[2]=d[3]=d[4]=d[5]=d[6]=d[7]= -2*MAXR*MAXC;
		if(c==2)
			d[4]=d[7] = -2*MAXR*MAXC;
		
		compute();
		/*
		printf("!");
		for(int i=0; i<r*c; i++)
		printf("%d ", neigh(i));
		*/
	}
}