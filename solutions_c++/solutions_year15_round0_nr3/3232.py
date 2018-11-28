#include <stdio.h>
#include <algorithm>
#include <queue>
using namespace std;

enum ComplexNum
{
	E1,
	Ei,
	Ej,
	Ek
};

int prod[4][4]={
	{E1,Ei,Ej,Ek},
	{Ei,E1,Ek,Ej},
	{Ej,Ek,E1,Ei},
	{Ek,Ej,Ei,E1}
};
int sign[4][4]={
	{1,1,1,1},
	{1,-1,1,-1},
	{1,-1,-1,1},
	{1,1,-1,-1}
};

char buf[10004];
int main()
{
	//freopen("C-small-attempt1.in", "rt", stdin);
	//freopen("Cs.out", "wt", stdout);

	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;++t)
	{
		int L,X;
		scanf("%d%d%s",&L,&X,buf);

		int cur_prod=E1,cur_target=Ei;
		int s=1;

		for(int x=0;x<X;++x)
			for(int l=0;l<L;++l)
			{
				int d=buf[l]-'i'+Ei;
				s=s*sign[cur_prod][d];
				cur_prod=prod[cur_prod][d];

				if(cur_prod==cur_target)
				{
					if(cur_target<Ek) ++cur_target,cur_prod=E1;
				}
			}
			printf("Case #%d: %s\n", t, (s==1&&cur_prod==Ek&&cur_target==Ek)?"YES":"NO");
	}

	return 0;
}