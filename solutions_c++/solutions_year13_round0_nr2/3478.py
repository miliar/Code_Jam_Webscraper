#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <string>
#include <vector>
#include <fstream>
#include <map>
using namespace std;
const int INF = -1u>>1;
const double eps = 1e-8;
int n,m;
const int MAXN = 111;
int a[MAXN][MAXN];

int main()
{
	ifstream in;
	ofstream out;
	in.open("D:\\B-large.in");
	out.open("D:\\B0.out");
	int T;
	cin>>T;
	//in>>T;
	for(int cas=1;cas<=T;cas++)
	{
		scanf("%d%d",&n,&m);
		//in>>n>>m;
		for(int i=0;i<n;++i)
		{
			for(int j=0;j<m;++j)
			{
				scanf("%d",&a[i][j]);
				/in>>a[i][j];
			}/
		}
		bool flag = true;
		for(int i=0;i<n;++i)
		{
			for(int j=0;j<m;++j)
			{
				bool flag1 = true,flag2 = true;
				for(int k=0;k<m;++k)
				{
					if(a[i][j] < a[i][k]) flag1 = false;
				}
				for(int k=0;k<n;++k)
				{
					if(a[i][j] < a[k][j]) flag2 = false;
				}
				if(flag1 || flag2)
				{
				}
				else
				{
					flag = false;
					break;
				}
			}
			if(!flag) break;
		}
		if(!flag) printf("Case #%d: NO\n",cas);
		else printf("Case #%d: YES\n",cas);
		//if(!flag) out<<"Case #"<<cas<<": NO"<<endl;
		//else out<<"Case #"<<cas<<": YES"<<endl;
	}
  return 0;
}

