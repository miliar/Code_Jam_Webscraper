#include <iostream>
#include <cstdio>
#include <set>

using namespace std;

int X, R, C;

bool solve()
{
	if(X>C && X>R)
	{
		return false;
	}
	int tmp = ((X+1)/2);
	if(tmp>R || tmp>C)
	{// it is for X=3 with single row or single columns
		return false;
	}
	if((C*R)%X)
	{
		return false;
	}
	if(X<4)
	{
		return true;
	}
	if(X==4)
	{
		if(C<3 || R<3)
		{
			return false;
		}
		if((R*C)<12)
		{//unnecessary
			return false;
		}
		return true;
	}
	if(X>6)
	{
		return false;
	}
	return false;
}

int main()
{
	FILE *in,*out;
//	char line[1000];
	int T, t;
	int i, j;
	in = fopen("D.in","r");
	out = fopen("D.out","w+");
//	fgets(line,999,in);
//	sscanf(line,"%d",&T);
	fscanf(in,"%d ",&T);
	for(t = 1; t <= T; t++)
	{
		fscanf(in,"%d %d %d ",&X, &R, &C);
		fprintf(out, "Case #%d: %s\n", t, (solve()?"GABRIEL":"RICHARD"));
	}
	fclose(in);
	fclose(out);
}
