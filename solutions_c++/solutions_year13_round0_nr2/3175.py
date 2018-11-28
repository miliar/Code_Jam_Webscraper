#include<stdio.h>

const int MAXSIZE = 100;
const int MAXT = 1000;
const int START=2;
const int LEFT=1;
const int UP=0;
int X,Y;
int A[MAXSIZE][MAXSIZE];
int S[MAXSIZE][MAXSIZE];
int B[MAXSIZE];
int T;
char str[16];

void showa()
{

int l0,l1;
for(l0=0;l0<X;l0++)
{
    for(l1=0;l1<Y;l1++)
	{
	printf("%d ",A[l0][l1]);
 	}
	printf("\n");
 }

}
void show(int X,int Y)
{

int l0,l1;

for(l0=0;l0<X;l0++)
 {
 	for(l1=0;l1<Y;l1++)
	{
	printf("%d",S[l0][l1]);
	}
	printf("\n");
 }

}
int isAllZero()
{

int l0,l1;

for(l0=0;l0<X;l0++)
{
	for(l1=0;l1<Y;l1++)
	{
	if(S[l0][l1] != 1)
		return 0;
	}
}

return 1;

}
void cutRow(int x,int y)
{

int l0;

for(l0=0;l0<X;l0++)
	{
	B[l0]=S[l0][y];
	S[l0][y]=A[x][y];
	}

}

void restoreRow(int x,int y)

{

int l0;

for(l0=0;l0<Y;l0++)
{
	S[l0][y]=B[l0];
}

}

void cutCol(int x,int y)
{
int l0=0;
for(l0=0;l0<Y;l0++)
 {
 B[l0]=S[x][l0];
 S[x][l0]=A[x][y];
 }
}

void restoreCol(int x,int y)
{
int l0=0;
for(l0=0;l0<X;l0++)
	{
	S[x][l0]=B[l0];
	}
}


int scanrow(int);
int scancol(int);
int setdcrow(int);
int setdccol(int);

int search()
{

int l0,l1;
int state=1;

while(state !=0)
{

state=0;

for(l0=0;l0<Y;l0++)
 {
  if(scanrow(l0))
	state+=setdcrow(l0);
 }
for(l0=0;l0<X;l0++)
{
	if(scancol(l0))
		state+=setdccol(l0);
}
//printf("%d\n",state);
}
if(isAllZero()) return 1;
return 0;
}







int scanrow(int y0)
{

int l0;
int t0=0;

for(l0=0;l0<X;l0++)
 {
 if(!S[l0][y0])
   t0=A[l0][y0];
 }
//printf("t0=%d @ %d\n",t0,y0);
 if(t0==0)
  return 0;
 
for(l0=0;l0<X;l0++)
 {
 if(A[l0][y0] != t0 && !S[l0][y0])
  return 0;
 if(S[l0][y0] && A[l0][y0] > t0 && A[l0][y0] !=t0)
  return 0;
 }
//	printf("row:%d okay\n",y0);
 return 1;


}

int scancol(int x0)
{

int l0;
int t0=0;

for(l0=0;l0<Y;l0++)
 {
 if(!S[x0][l0])
   t0=A[x0][l0];
 }

//printf("t0=%d @ col %d.\n",t0,x0);
 if(t0==0)
  return 0;
 
for(l0=0;l0<Y;l0++)
 {
 if(A[x0][l0] != t0 && !S[x0][l0])
  return 0;
 if(S[x0][l0] && A[x0][l0] > t0 && A[x0][l0] != t0)
  return 0;
 }
//printf("col %d okay.\n",x0);
 return 1;


}

int setdcrow(int y0)
{

int l0,r0;

r0=0;

for(l0=0;l0<X;l0++)
{
 if(S[l0][y0]==0)
 {
  S[l0][y0]=1;
  r0++;
 }
 }
 
return r0;
}

int setdccol(int x0)
{

int l0,r0;
r0=0;

for(l0=0;l0<Y;l0++)
 {
  {
  if(S[x0][l0]==0)
	{	
	S[x0][l0]=1;
	r0++;
	}
  }
 }

return r0;
}

void init()
{
int l0,l1;

for(l0=0;l0<MAXSIZE;l0++)
	for(l1=0;l1<MAXSIZE;l1++)
		S[l0][l1]=0;
}

int main(void)
{
	int l0, l1, l2;
	int t1, t2;
	init();

	freopen("./input","r",stdin);
	scanf("%d", &T);
	for(l0 = 1; l0 <= T; l0++)
	{
		
		scanf("%d %d",&X,&Y);
		for(l1=0;l1<X; l1++)
		{
			for(l2=0;l2<Y;l2++)
			{
			scanf("%d ",&t1);
			A[l1][l2]=t1;
			}
		}
//		showa();
		t2 = search();
//		show(X,Y);
		if(t2==1)
		printf("Case #%d: YES\n",l0);
		else
		printf("Case #%d: NO\n",l0);
	
		init();
		

	}
}
