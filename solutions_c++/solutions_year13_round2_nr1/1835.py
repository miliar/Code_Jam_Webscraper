/*
 * osmos.cpp
 *
 *  Created on: May 5, 2013
 *      Author: stephenfebrian
 */
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<long long> vll;
vector<int> viS;
int res2;

int main()
{
	freopen("osmos.in","r",stdin);
	freopen("osmos.out","w",stdout);
	int T,N;
	long long slf;
	long long S;
	scanf("%d",&T);
	for(int i=0;i<T;i++)
	{
		vll.clear();
		viS.clear();
		res2= 0;
		scanf("%lld",&slf);
		scanf("%d",&N);
		for(int j=0;j<N;j++)
		{
			scanf("%lld",&S);
			vll.push_back(S);
		}
		sort(vll.begin(), vll.end());
		int res = 0;
		for(int j=0;j<N;j++)
		{
			if(slf > vll[j])
			{
				slf+=vll[j];
			}
			else
			{
				if(slf == 1)
				{
					res = (N-j);
					break;
				}
				res2++;
				viS.push_back(res+(N-j));
				while(slf <= vll[j])
				{
					slf+=(slf-1);
					res++;
				}
				slf+=(vll[j]);
			}
		}
		if(viS.size() > 0)
		{
			sort(viS.begin(),viS.end());
			if(res > viS[0]) res = viS[0];
		}
		printf("Case #%d: %d\n",i+1,res);
	}
	fclose(stdout);
}
