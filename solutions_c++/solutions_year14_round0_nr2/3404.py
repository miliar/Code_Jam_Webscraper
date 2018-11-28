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
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.in","w",stdout);
	int t,k=1;
	double s,sum,c,f,x;
	scanf("%d",&t);
	while(t--){
		cin>>c>>f>>x;
		double w,r=2;
		sum=x/r;
		w=c/r;
		r+=f;
		while(1){
			if(sum<w+x/r)
				break;
			sum=w+x/r;
			w=w+c/r;
			r+=f;
		}
		printf("Case #%d: %.7f\n",k++,sum);
	}
	return 0;
}
