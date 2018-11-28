#include<iostream>
#include <cmath>
#include <algorithm>
#include<vector>
#include <string>
#include <set>
#include <sstream>
#include<fstream>
#include<cstdio>
using namespace std;
int main()
{
	freopen("B-small-attempt0 (1).in","r",stdin);
freopen("out314.out","w",stdout);
	int cases;
	cin>>cases;
	for(int c1=1;c1<=cases;c1++){
	int a,b,k,ret=0;
	cin>>a>>b>>k;
	for(int i=0;i<a;i++)
		for(int j=0;j<b;j++)
			if((i&j)<k)
				ret++;
	printf("Case #%d: %d\n",c1,ret);
	}
	return 0;
}
