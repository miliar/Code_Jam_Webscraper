#include <cstdio>
using namespace std;
int main()
{
	int t,T,r,c,x;
	int a[4][4][4]={{{0,1,1,1},{0,0,1,1},{0,1,1,1},{0,0,1,1}},{{0,0,1,1},{0,0,1,1},{0,0,0,1},{0,0,1,1}},{{0,1,1,1},{0,0,0,1},{0,1,0,1},{0,0,0,0}},{{0,0,1,1},{0,0,1,1},{0,0,0,0},{0,0,1,0}}};
	FILE * fr=fopen("D-small-attempt0.in","r");
	FILE * fw=fopen("D.out","w");
	fscanf(fr,"%d",&t);
	T=t;
	while(t--)
	{
		fscanf(fr,"%d %d %d",&x,&r,&c);
		if(a[r-1][c-1][x-1])
			fprintf(fw, "Case #%d: RICHARD\n",(T-t));
		else
			fprintf(fw, "Case #%d: GABRIEL\n",(T-t));
	}
	fclose(fr);
	fclose(fw);
}