#include <cstdio>
#include <ctime>
#include <cstdlib>
#include <vector>
using namespace std;

int R, N, M, K;

int num[128];
vector<int> gs;

void print(const vector<int>& v)
{
    for(int i = 0; i < v.size(); i++)
	printf("%d", v[i]);
    printf("\n");
}

int main()
{
    srand(time(NULL));
    int T;
    scanf("%d", &T);
    for(int tn = 1; tn <= T; tn++)
    {
	printf("Case #%d:\n", tn);

	scanf("%d%d%d%d", &R, &N, &M, &K);

	gs.resize(N);

	while(R--)
	{
	    for(int i = 0; i < K; i++)
		scanf("%d", num + i);

	    vector<vector<int> > cad;
	    for(int i = 2; i <= M; i++)
		for(int j = i; j <= M; j++)
		    for(int k = j; k <= M; k++)
		    {
			gs[0] = i;
			gs[1] = j;
			gs[2] = k;
                        
		        bool table[256] = {};
			for(int z = 7; z >= 0; z--)
			{
			    int t = 1;
			    for(int x = 0; x < 3; x++)
				if(z & (1 << x))
				    t *= gs[x];
			    table[t] = true;
			}
			bool check = true;
			for(int x = 0; x < K; x++)
			    if(!table[num[x]])
			    {
				check = false;
				break;
			    }
			if(check)
			    cad.push_back(gs);
		    }

              print(cad[rand() % cad.size()]);
	}

    }
    return 0;
}
