#include<cstdio>

using namespace std;

int T,r1,r2;
int c[4][2];
void discardrow()
{
	int t1;
	scanf("%d %d %d %d",&t1,&t1,&t1,&t1);
}
void readrow(int k)
{
	scanf("%d %d %d %d",&c[0][k],&c[1][k],&c[2][k],&c[3][k]);
}

int main()
{
	scanf("%d",&T);
	for(int run=1;run<=T;++run){
		scanf("%d",&r1);
		if(r1==1)readrow(0); else discardrow();
		if(r1==2)readrow(0); else discardrow();
		if(r1==3)readrow(0); else discardrow();
		if(r1==4)readrow(0); else discardrow();
		scanf("%d",&r2);	
		if(r2==1)readrow(1); else discardrow();
		if(r2==2)readrow(1); else discardrow();
		if(r2==3)readrow(1); else discardrow();
		if(r2==4)readrow(1); else discardrow();
		int d=0,e;
		for(int i=0;i<4;++i)
			for(int j=0;j<4;++j)
			if(c[i][0]==c[j][1]){d++;e=c[i][0];}
		if(d==0)printf("Case #%d: Volunteer cheated!\n",run);
		if(d==1)printf("Case #%d: %d\n",run,e);
		if(d>1)printf("Case #%d: Bad magician!\n",run);
	}
	return 0;
}
