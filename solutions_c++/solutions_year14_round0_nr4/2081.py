#include <stdio.h>
#include <string.h>
#include <algorithm>
#define print(f,...) printf(f,__VA_ARGS__)
const int MAX=1000;
int T,N;
double Ken[MAX],Naomi[MAX];
int case_num;
void solve()
{
	std::sort(Ken,Ken+N);
	std::sort(Naomi,Naomi+N);
	int k_id_min=0,k_id_max=N-1;
	int n_id_min=0,n_id_max=N-1;
	int D_War=0,N_War=0;
	for (int i = 0; i < N; i++)
	{
		double u=Naomi[n_id_max],v=Ken[k_id_max];
		if (u<v)
		{
			n_id_min++;
			k_id_max--;
		}
		else
		{
			if (u!=v)
			{
				D_War++;
			}
			n_id_max--;
			k_id_max--;
		}
	}
	k_id_min=0,k_id_max=N-1;
	n_id_min=0,n_id_max=N-1;
	for (int i = 0; i < N; i++)
	{
		double k=Naomi[n_id_min];
		while (Ken[k_id_min]<=k&&k_id_min<=k_id_max)
		{
			k_id_min++;
		}
		if (k_id_min>k_id_max)
		{
			N_War=N-n_id_min;
			break;
		}
		n_id_min++;
		k_id_min++;
	}
	print("%d %d\n",D_War,N_War);
}
int main()
{
	scanf("%d",&T);
	for (case_num = 1; case_num <= T; case_num++)
	{
		print("Case #%d: ",case_num);
		scanf("%d",&N);
		for (int i = 0; i < N; i++)
		{
			scanf("%lf",&Naomi[i]);
		}
		for (int i = 0; i < N; i++)
		{
			scanf("%lf",&Ken[i]);
		}
		solve();
	}	
}