#include <iostream>
#include <string.h>
#include <math.h>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <stdio.h>
#include <string>
#include <cctype>
#include <ctime>
#include <strstream>
typedef long long ll;
#define EPS 1e-8
using namespace std;
#define N 10005
int n,x;
int main()
{
	ios_base::sync_with_stdio(false);
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int cas;
	int ki,i,j,sum;
	scanf("%d",&cas);
	map<int,int>::iterator it1;
	map<int,int>::reverse_iterator it2;
	map<int,int> ma;
	for(ki=1;ki<=cas;ki++)
	{
		printf("Case #%d: ",ki);
		cin>>n>>x;
		for(i=0;i<n;i++)
		{
			cin>>j;
			ma[j]++;
		}
		sum=0;
		while(!ma.empty())
		{
			it1=ma.begin();
			if(ma.size()==1)
			{
				if(it1->first+it1->first<=x)
					sum+=(it1->second+1)/2;
				else sum+=it1->second;
				ma.erase(it1);
				continue;
			}
			it2=ma.rbegin();
			if(it1->first+it2->first<=x)
			{
				if(it1->second>it2->second)
				{
					sum+=it2->second;
					it1->second-=it2->second;
					ma.erase(--(it2.base()));
				}
				else if(it1->second<it2->second)
				{
					sum+=it1->second;
					it2->second-=it1->second;
					ma.erase(it1);
				}
				else
				{
					sum+=it1->second;
					ma.erase(--(it2.base()));
					ma.erase(ma.begin());
				}
			}
			else
			{
				sum+=it2->second;
				ma.erase(--(it2.base()));
				
			}
		}
		cout<<sum<<endl;
		fflush(stdout);
	}
	return 0;
}