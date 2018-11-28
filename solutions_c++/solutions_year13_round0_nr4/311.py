#include <cstdio>
#include <vector>
#include <cstring>
using namespace std;

const int MAXN = 20, MAXS = (1<<MAXN)+50, MAXK = 210;
int used[ (MAXS+31)>>5 ];
vector <int> preo[MAXS];
int prek[MAXK], res[MAXK];

int req[MAXN+5], TMAX;
vector <int> box[MAXN+5], mask[MAXN+5][MAXN+5];

void precal(int now, int nows, int cho)
{
	if(now == TMAX)
	{
		mask[TMAX-1][cho].push_back( nows );
		return ;
	}
	
	precal(now+1, nows|(1<<now), cho+1);
	precal(now+1, nows, cho);
}
int main()
{
	int T, K, N;
	scanf("%d", &T);
	
	TMAX = 1;
	while(TMAX <= MAXN)
	{
		precal(0, 0, 0);
		++TMAX;
	}
	
	for(int tc = 1; tc <= T; tc++)
	{
		scanf("%d%d", &K, &N);
		memset(prek, 0, sizeof(prek));
		
		for(int i = 0; i < K; i++)
		{
			int v;
			scanf("%d", &v);
			++prek[ v ];
		}
		
		for(int i = 0; i < N; i++)
		{
			int nn, vv;
			scanf("%d%d", &req[i], &nn);
			box[i].clear();
			while(nn--)
			{
				scanf("%d", &vv);
				box[i].push_back( vv );
			}
		}
		
		int upper = 1<<N;
		memset(used, 0, sizeof(used));
		memset(preo, -1, sizeof(preo));
		
		used[0] = 1;
		int maxV = 0;
		
		for(int num = 0; num < N; num++)		
		for(int ns = 0; ns < mask[N-1][num].size(); ns++)
		{
			int i = mask[N-1][num][ns];
			if(used[i>>5] & (1<<(i&31)))
			{
				//			printf("GO! %d !!\n", i);
				//key precalculation
				for(int j = 1; j < MAXK; j++)
					res[j] = prek[j];
					
				for(int j = 0; j < N; j++)
					if((i & (1<<j)))
					{
						--res[ req[j] ];
						for(int k = 0; k < box[j].size(); k++)
							++res[ box[j][k] ];
					}				
					
				/*for(int j = 0; j < MAXK; j++)
					if(res[j])
						printf("GGG %d - %d\n", j, res[j]);*/
				
				for(int j = 0; j < N; j++)
					if( (i & (1<<j)) == 0 && res[ req[j] ])
					{
						int news = i|(1<<j);
						vector <int> vl = preo[i];
						vl.push_back( j );
						
						if( (used[ news>>5 ] & (1<<(news&31))) == 0 ) preo[ news ] = vl;
						else if(vl < preo[ news ]) preo[news] = vl;
						used[ news>>5 ] |= (1<<(news&31));
					}
			}
		}
		
		if( preo[upper-1].size() == 0) printf("Case #%d: IMPOSSIBLE\n", tc);
		else 
		{			
			printf("Case #%d:", tc);
			for(int i = 0; i < preo[upper-1].size(); i++)
				printf(" %d", preo[upper-1][i]+1);
			printf("\n");
		}
		fflush(stdout);
	}
	
	return 0;
}