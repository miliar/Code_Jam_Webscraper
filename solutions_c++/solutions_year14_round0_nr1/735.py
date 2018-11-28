/*Vladimir Ignatiev 2014*/
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>

using namespace std;

#define rep(A,B) for(int A=0;A<B;++A)
#define repi(A,I,B) for(int A=I;A<B;++A)
#define repd(A,B) for(int A=B-1;A>=0;--A)
#define repdi(A,I,B) for(int A=B-1;A>=I;--A)
#define repall(A,F) for_each(A.begin(),A.end(),F);

int a1, a2, deck1[4][4],deck2[4][4];

int f()
{	
	int res=-1;

	rep(y1,4)
		rep(y2,4)
		{
			if(deck1[a1][y1]==deck2[a2][y2])
			{
				if(res>0) return 0;
				else
					res=deck1[a1][y1];
			}
		}
	return res;
}

int main()
{
	FILE* In=fopen("A.in","r");if(!In) return 1;
	FILE* Out=fopen("A.res","w");if(!Out) return 2;

	int nCount;
	fscanf(In,"%d",&nCount);
	rep(i,nCount)
	{
		fprintf(Out,"Case #%d: ",i+1);
		printf("%d\n",i);

		fscanf(In,"%d",&a1);
		--a1;

		rep(x,4)
		rep(y,4)
		fscanf(In,"%d",&deck1[x][y]);

		fscanf(In,"%d",&a2);
		--a2;

		rep(x,4)
		rep(y,4)
		fscanf(In,"%d",&deck2[x][y]);

		int res=f();
		if(res==0) fprintf(Out,"%s\n","Bad magician!");
		else
			if(res==-1) fprintf(Out,"%s\n","Volunteer cheated!");
			else
				fprintf(Out,"%d\n",res);
	};
	fclose(In);
	fclose(Out);
	return 0;
}