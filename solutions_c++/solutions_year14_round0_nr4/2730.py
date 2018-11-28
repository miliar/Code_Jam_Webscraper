#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;

vector<double>naomi;
vector<double>ken;
int n;

int war()
{
	int i, j;
	int k[1000]={0};
	
	j = 0;
	for(i=0;i<n;i++)
	{
		while(j<n)
		{
			if(!k[j] && ken[j] > naomi[i])
			{
				k[j] = 1;
				break;
			}
			j++;
		}
	}
	int c = 0;
	for(i=0;i<n;i++)if(k[i] == 0)c++;
	return c;
}

int dwar()
{
	int c = 0, i;
	int n_f[1000]={0};
	int process = 0;
	int last = n-1;
	int n_start = 0;
	
	if(n==1)
	{
		if(naomi[0] > ken[0])return 1;
		return 0;
	}
	
//printf("KEN: ");for(int i=0;i<n;i++)printf("%.3lf ", ken[i]);printf("\n");
//printf("NOI: ");for(int i=0;i<n;i++)printf("%.3lf ", naomi[i]);printf("\n");
	while(process != n)
	{
		for(i=0;i<n;i++)
		{
			if(!n_f[i] && naomi[i] > ken[last])
			{
				last--;
				n_f[i] = 1;
				c++;
				process++;
				break;
			}			
		}
		if(i == n)
		{
			n_start++;
			last--;
			process++;
		}
	}
	return c;
}

int main()
{
	int i, cases, cas, w, dw;
	double x;
	
	scanf("%d", &cases);
	for(cas = 1; cas <= cases; cas++)
	{
		naomi.clear();
		ken.clear();
		scanf("%d", &n);
		for(i=0;i<n;i++)
		{
			scanf("%lf", &x);
			naomi.push_back(x);
		}
		for(i=0;i<n;i++)
		{
			scanf("%lf", &x);
			ken.push_back(x);
		}
		
		w = dw = 0;
		
		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());
		
		w = war();
		dw = dwar();
		printf("Case #%d: %d %d\n", cas, dw, w);
	}
	return 0;
}