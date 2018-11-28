#include<bits/stdc++.h>

#define f(i,a,b) for(int (i)=(a);(i)<(b);++(i))
#define x first
#define y second
#define mp make_pair
#define pb push_back
#define INF 1000000000

using namespace std;

typedef pair<int,int> pii;
int main()
{
	ifstream fin("B-large.in");
	ofstream fout("B.out");
	int cases;
	fin>>cases;
	for(int cas=1;cas<=cases;++cas)
	{
		fout<<"Case #"<<cas<<": ";
		int n;
		fin>>n;
		int a[n];
		f(i,0,n) fin>>a[i];
		int cost[n];
		f(i,0,n) cost[i]=0;
		f(i,0,n)
		{
			f(j,0,i)
			{
				if(a[j]>a[i]) cost[i]+=1;
			}
		}

		int tcost=0;
		pii vals[n];
		f(i,0,n)
		{
			vals[i]=mp(a[i],i);
		}
		sort(vals,vals+n);

		f(i,0,n) 
		{
			tcost+=min(cost[vals[i].y],n-1-i-cost[vals[i].y]);
		}
		fout<<" "<<tcost;
		fout<<'\n';
	}
	return 0;
}
