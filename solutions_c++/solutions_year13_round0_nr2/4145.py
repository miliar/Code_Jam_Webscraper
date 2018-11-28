#include <stdio.h>
#include <string.h>
#include <cmath>

using namespace std;

long long ipow(long long a, long long b);
long long digit(long long a, long long b);
bool is_fair_and_square(long long a, bool b, long long c, long long d);
long long length(long long x);


int main(int argc, char** argv){

		int T;
		int h[101][101];


		int cmax[101];
		int rmax[101];

		scanf(" %d",&T);

		for(int t=1;t<=T;t++)
		{
			printf("Case #%d: ",t);
			int N,M;
			scanf(" %d %d", &N, &M);

			for(int i=0;i<N;i++){
			for(int j=0;j<M;j++)
			{

				scanf(" %d",&h[i][j]);
			}}
			// Find largest in each row
			for(int i=0;i<N;i++)
			{
				rmax[i]=0;
				for(int j=0;j<M;j++)
				{
					if(h[i][j]>rmax[i]) rmax[i]=h[i][j];
				}
			}

			// Find largest in each column
			for(int j=0;j<M;j++)
			{
				cmax[j]=0;
				for(int i=0;i<N;i++)
				{
					if(h[i][j]>cmax[j]) cmax[j]=h[i][j];
				}
			}

			int possible=true;
			// Every square must be either the largest in its row or in its column
			for(int i=0;i<N;i++){
			for(int j=0;j<M;j++)
			{
				if(h[i][j]<cmax[j] && h[i][j]<rmax[i]) possible=false;
			}}

			if(possible)
			{
				printf("YES\n");
			} else {
				printf("NO\n");
			}
		}
			
		return 0;
}
