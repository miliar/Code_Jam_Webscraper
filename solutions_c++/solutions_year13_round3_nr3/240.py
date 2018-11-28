#include "stdio.h"
#include "stdlib.h"
#include <vector>
#include <list>
#include <queue>
#include <string>
using namespace std;

struct Attack
{
	int d, w, e, s;
	bool operator < (Attack& a)
	{
		if( d != a.d )
		{
			return d < a.d;
		}
		return false;
	}
};

bool check(int h[800], Attack& a)
{
	for(int i=a.w; i<a.e; ++i)
	{
		if( h[i+400] < a.s )
			return false;
	}

	return true;
}

void set(int h[800], Attack& a)
{
	for(int i=a.w; i<a.e; ++i)
	{
		if( h[i+400] < a.s )
			h[i+400] = a.s;
	}
}

int main()
{
	int h[800];

	char str[10][10];
	int N;
	scanf("%d",&N);
	gets(str[0]);
	for(int I=1; I<=N; ++I)
	{
		vector<Attack> va;
		printf("Case #%d: ", I);
		int tribes;
		scanf("%d", &tribes);
		int i,j,k;
		for(i=0; i<tribes; ++i)
		{
			int di, wi, ni, si, ei, ddi, dpi, dsi;
			scanf("%d%d%d%d%d%d%d%d", &di, &ni, &wi, &ei, &si, &ddi, &dpi, &dsi);
			//generate
			for(j=0; j<ni; ++j)
			{
				Attack a;
				a.w = wi;
				a.e = ei;
				a.s = si;
				a.d = di;
				va.push_back(a);

				di += ddi;
				wi += dpi;
				ei += dpi;
				si += dsi;
			}
		}
		for(i=0; i<800; ++i)
		{
			h[i] = 0;
		}
		sort( va.begin(), va.end() );
		int successful = 0;
		for(i=0; i<va.size(); ++ i)
		{
			int start_index = i;
			int dd = va[i].d;
			if( !check( h, va[i] ) )
				successful++;
			while( i+1<va.size() && va[i+1].d == dd)
			{
				++i;
				if( !check( h, va[i] ) )
					successful++;
			}
			for(j=start_index; j<=i; ++j)
				set(h, va[j]);
		}
		printf("%d\n", successful);
	}
	return 0;
}

