#include <set>
#include <map>
#include <cmath>
#include <stack>
#include <queue>
#include <string>
#include <cstdio>
#include <vector>
#include <cctype>
#include <climits>
#include <sstream>
#include <cstdlib>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
#define mp make_pair
int geti(){int y=0,s=1;char c=getchar();while(!isdigit(c)&&c!='-')c=getchar();if(c=='-')s=-1,c=getchar();while(isdigit(c))y=y*10+(c-'0'),c=getchar();return s*y;}
int dx[] = { -1, -1, -1, 0, 1, 1, 1, 0 };
int dy[] = { -1, 0, 1, 1, 1, 0, -1, -1 };
vector<double>x;
vector<double>y;
vector<bool>visit;
int n;
int main()
{
	//freopen("myfile.txt", "r", stdin);
	freopen("D-large.in", "r", stdin);
	freopen("out.in", "w", stdout);
	int t,k=1;
	double a;
	scanf("%d",&t);
	while(t--){
		scanf("%d",&n);
		y.clear();
		visit.clear();
		visit.resize(n);
		y.resize(n);
		x.clear();
		x.resize(n);
		for(int i=0;i<n;++i)
			cin>>x[i];
		for(int i=0;i<n;++i)
			cin>>y[i];
		int c=0;
		bool f;
		sort(y.begin(),y.end());
		for(int i=0;i<n;++i){
			f=0;
			for(int j=0;j<n;++j)
				if(y[j]>x[i] && !visit[j]){
					visit[j]=1;					
					f=1;
					break;
				}
				if(!f)
					for(int j=0;j<n;++j)
						if(!visit[j]){
							visit[j]=1;
							c++;
							break;
						}
		}
		int c2=0;

		sort(x.begin(),x.end());
		for(int i=0;i<n;++i){
			f=0;
			for(int j=0;j<n;++j)
				if(x[j]>y[i] && visit[j]){
					visit[j]=0;					
					c2++;
					f=1;
					break;
				}
				if(!f)
					for(int j=0;j<n;++j)
						if(visit[j]){
							visit[j]=0;
							break;
						}
		}
		printf("Case #%d: %d %d\n",k++,c2,c);
	}
	return 0;
}
