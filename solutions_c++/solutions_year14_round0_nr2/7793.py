									/*	In the name of God	*/
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <iostream>
#include <sstream>
#include <bitset>
#include <map>
#include <set>
#include <queue>
#include <stack>

#define rep(i,n) for((i)=0;(i)<(n);(i)++)
typedef long long ll;

using namespace std;


int main(){
	int tc,i,j;
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	
	scanf("%d",&tc);
	for (int tci = 1; tci <= tc; tci++)
	{
		double c,f,x,t,r,ans;
		scanf("%lf %lf %lf",&c,&f,&x);
		t=0;
		r=x/2;
		for (int k = 0; k < x+1; k++)
		{
			t+=c/(2+k*f);
			ans=t+x/(2+(k+1)*f);
			if (ans<r)
				r=ans;
		}
		printf("Case #%d: ",tci);
		printf("%.7lf",r);
		printf("\n");
	}
	
	return 0;
}