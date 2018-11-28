#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string.h>
#include <cstring>
#include <algorithm>
#include <math.h>
#include  <io.h>
#include  <stdio.h>
#include  <stdlib.h>
#include <string.h>
#include <string>

using namespace std;

int N, M, T;
int mem[1000][1000];

int main()
{
	int i,j,k, tt,r,c;
	freopen("in.txt","r",stdin);
	freopen("out.txt","wt",stdout);
	tt=0;
	scanf("%d", &T);
	while(tt++<T)
	{
		bool cando = true;
		scanf("%d %d", &N, &M);
		for(i=0; i<N; i++)
			for(j=0; j<M; j++)
				scanf("%d", &mem[i][j]);
		for(i=0; i<N; i++)
			for(j=0; j<M; j++)
			{
				bool haveHigher = false;
				for(r=0; r<N; r++)
					if(r!=i && mem[i][j]<mem[r][j])
						haveHigher = true;
				if(haveHigher)
				{
					haveHigher = false;
					for(c=0; c<M; c++)
						if(c!=j && mem[i][j]<mem[i][c])
							haveHigher = true;
				}
				if(haveHigher)
					cando = false;
			}
		if(cando)
			printf("Case #%d: YES\n",tt);
		else
			printf("Case #%d: NO\n",tt);
	}

	return 0;
}
