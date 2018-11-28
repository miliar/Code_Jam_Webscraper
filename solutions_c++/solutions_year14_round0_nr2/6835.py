#include <iostream>
#include <cstdio>
#include <cmath>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#define S second
#define F first
#define pb push_back
using namespace std;
double C,F,X,T,R,Y;
int n;
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t,test;
	cin>>t;
	test=t;
	while (t--)
	{
		R=2.0;
		scanf("%lf%lf%lf",&C,&F,&X);
		Y=X/R;
		for (int i = 1 ; i <= 100000000; i++)
		{
			Y = min(Y,Y-X/(R+(i-1)*F)+C/(R+(i-1)*F)+X/(R+i*F));
		}
		printf("Case #%d: ",test-t);
		printf("%.7lf\n",Y);

	}

return 0;
}
