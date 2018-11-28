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
using namespace std;
int pat[200][200];
int mx1[200];
int mx2[200];
int main()
{
	int n;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin>>n;
	for(int i=0; i<n; i++)
	{
		string ans="YES";
		bool ok=true;
		int N, M;
		cin>>N>>M;
		for(int j=0; j<N; j++)
		{
			mx1[j]=0;
			for(int z=0; z<M; z++)
			{
				cin>>pat[j][z];
				if(pat[j][z]>mx1[j]) mx1[j]=pat[j][z];
			}
		}
		for(int z=0; z<M; z++)
		{
			mx2[z]=0;
			for(int j=0; j<N; j++)
				if(pat[j][z]>mx2[z]) mx2[z]=pat[j][z];
		}
		for(int j=0; j<N; j++)
		{
			for(int z=0; z<M; z++)
				if(mx1[j]>pat[j][z]&&mx2[z]>pat[j][z])
					ans="NO";
		}
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
}