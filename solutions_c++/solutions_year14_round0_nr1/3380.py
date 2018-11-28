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
int dx[] = { 1, -1, 0, 0, 1, 1, -1, -1 };
int dy[] = { 0, 0, 1, -1, -1, 1, -1, 1 };
vector<vector<int> >x;
int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("out.in","w",stdout);
	int t,n,a,k=1;
	scanf("%d",&t);
	while(t--){
		scanf("%d",&n);
		x.resize(2);
		for(int i=0;i<4;++i)
			for(int j=0;j<4;++j){
				scanf("%d",&a);
				if(i==n-1)
					x[0].push_back(a);
			}
			scanf("%d",&n);
			for(int i=0;i<4;++i)
				for(int j=0;j<4;++j){
					scanf("%d",&a);
					if(i==n-1)
						x[1].push_back(a);
				}

				int c=-1;
				for(int i=0;i<4;++i){
					for(int j=0;j<4;++j)
					if(x[0][i]==x[1][j]){
						if(c==-1)
							c=x[0][i];
						else{
							c=-2;
							break;
						}
					}
					if(c==-2)
						break;
				}
					printf("Case #%d: ",k++);
				if(c==-1)
					printf("Volunteer cheated!\n");
				else
					if(c==-2)
						printf("Bad magician!\n");
					else
						printf("%d\n",c);
				x.clear();

	}

	return 0;
}
