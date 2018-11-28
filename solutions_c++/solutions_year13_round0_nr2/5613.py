#include <string.h>
#include <queue>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <fstream>
using namespace std;
#define S(n) 		scanf("%d",&n)
#define SL(n) 		scanf("%lld",&n)
#define FORALL(i,a,b) 	for(int i=a;i<b;i++)
#define ALL(a)   	a.begin(), a.end()
#define IN(a,b) 	((b).find(a) != (b).end())
#define SZ(a) 		((int)(a.size()))
#define MP            	make_pair
#define VI 		vector<int>
#define VPI 		vector<pair<int,int> >
#define DREP(a)      	sort(all(a)); a.erase(unique(all(a)),a.end())
#define INDEX(arr,ind) 	(lower_bound(all(arr),ind)-arr.begin())
#define LL 		long long
vector<vector<int> > v;
int a,b;
bool checkColumnMin(int row,int column)
{
	int curMin=v[row][column];
	FORALL(i,0,a)
	{
		if(i!=row)
		{
			if(v[i][column]>v[row][column]) return false;
		}
	}
	return true;
}
void debug(vector<vector<int> > v)
{
	for(int i=0;i<v.size();i++)
	{
		for(int j=0;j<v[i].size();j++)
		{
			cout<<v[i][j]<<" ";
		}
		cout<<endl;
	}
}
int findmin(int i)
{
	int mi=100000,pos=-1;
	FORALL(j,0,b)
	{
		if(v[i][j]<mi)
		{
			pos=j;
			mi=v[i][j];
		}
	}
	return pos;
}
int main()
{
	int t;
	ifstream fin("file.in");
	fin>>t;
	int index=0;
	while(t--)
	{
		fin>>a>>b;
		v.clear();v.resize(a);
		FORALL(i,0,a)
		{
			v[i].resize(b);
			FORALL(j,0,b)
			{
				fin>>v[i][j];
			}
		}
		//debug(v);
		bool rowPossible=true,columnPossible=true,resultPossible=true;
		FORALL(i,0,a)
		{
			int mi=findmin(i);
			int it=v[i][mi];
			//cout<<mi<<" "<<it<<endl;
			FORALL(k,0,b)
			{
				if(v[i][k]==it)
				{
					FORALL(j,0,b)
					{
						if(v[i][j]>v[i][mi])
						{
							rowPossible=false;
							break;
						}
						else rowPossible=true;
					}
					columnPossible=checkColumnMin(i,k);
					/*if(index==4 && i==2)
					{
						cout<<i<<" "<<mi<<endl;
						cout<<rowPossible<<" "<<columnPossible<<endl;
					}*/
					if(rowPossible || columnPossible)
					{
						resultPossible=true;
						rowPossible=false;
						columnPossible=false;
					}
					else
					{
						resultPossible=false;
						break;
					}
				}
			}
			if(!resultPossible) break;
		}
		if(!resultPossible)
		{
			cout<<"Case #"<<++index<<": NO\n";
		}
		else
		{
			cout<<"Case #"<<++index<<": YES\n";
		}
	}

	return 0;
}
