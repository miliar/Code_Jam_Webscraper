#include<iostream>
#include<stdio.h>
#include<iomanip>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
	int T;
	freopen("D-large.in","r",stdin);
	freopen("D.out","w",stdout);
	cin>>T;
	int i;
	int t;
	for(t = 1;t <= T; t ++)
	{
		int N;
		cin >>N;
		vector<double> a(N,0.0);
		vector<double> b(N,0.0);
		for(i = 0;i < N;i ++)
		{
			cin>>a[i];
		}
		for(i = 0;i < N;i ++)
		{
			cin>>b[i];
		}
		sort(a.begin(),a.end());
		sort(b.begin(),b.end());
		int num1 = 0;
		int num2 = 0;
		int pal,par,pbl,pbr;
		pal = 0;
		par = N - 1;
		pbl = 0;
		pbr = N - 1;
		while(pal <= par && pbl <= pbr)
		{
			if(a[pal] > b[pbl])
			{
				num1 ++;
				pal ++;
				pbl ++;
			}
			else
			{
				pal ++;
				pbr --;
			}
		}
		pal = 0;
		par = N - 1;
		pbl = 0;
		pbr = N - 1;
		while(pal <= par && pbl <= pbr)
		{
			if(a[par] < b[pbr])
			{
				num2 ++;
				par --;
				pbr --;
			}
			else
			{
				par --;
				pbl ++;
			}
		}
		num2 = N - num2;
		cout << "Case #"<<t<<": "<<num1<<" "<<num2<<endl;
	}
	return 0;
}