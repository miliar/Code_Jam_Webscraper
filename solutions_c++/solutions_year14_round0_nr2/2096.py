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
#define min(a,b) ((a) < (b) ? (a) : (b)) 
#define max(a,b) ((a) > (b) ? (a) : (b)) 
using namespace std;
int main()
{
	ios_base::sync_with_stdio(false);
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int cas;
	int ki,i,j;
	double c,f,x,p,r;
	scanf("%d",&cas);
	for(ki=1;ki<=cas;ki++)
	{
		printf("Case #%d: ",ki);
		cin>>c>>f>>x;
		if(x<=c)
		{
			printf("%.7lf\n",x/2);
			continue;
		}
		p=2;
		r=0;
		while(x/p>c/p+x/(p+f))
		{
			r+=c/p;
			p+=f;
		}
		r+=x/p;
		printf("%.7lf\n",r);
	}
	return 0;
}