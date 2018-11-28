#include <iostream>
#include <vector>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <algorithm>
#include <string>
#include <cstring>

using namespace std;

int MaxInt(int p, int q)
{
	int ret = 0;
	while (p!=0 && q!=0 && p!=1 && q!=1)
	{
		if (p>q)
		{
			p=p%q;
			if (p==0)
			{
				return q;
			}
		}
		else if(p<q)
		{
			q=q%p;
			if (q==0)
			{
				return p;
			}
		}
	}
	if (p==1 || q==1)
	{
		return 1;
	}
	//return q;
}

void solve(int CaseNum)
{
	int P, Q;
	scanf("%d/%d",&P,&Q);
	int factor =  MaxInt(P,Q);
	P/=factor;
	Q/=factor;
	//cout << "New PQ" << P  << Q << endl;
	int start = 1;
	int i = 0;
	while (Q>start)
	{
		i++;
		start*=2;
	}
	int j = 0;
	int PStart = 1;
	while(P>=PStart)
	{
		j++;
		PStart*=2;
	}
	//cout << P << PStart << j << endl;
	if (Q==start)
	{
		cout << "Case #" << CaseNum << ": " << i-j+1 << endl; 
	}
	else
	cout << "Case #" << CaseNum <<  ": impossible" << endl;
	return;
}

int main()
{
	int caseNum = 0;
	cin >> caseNum ;
	for (int i = 0; i < caseNum ; i++)
	{
		solve(i+1);
	}
 return 0;
}