#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <set> 
using namespace std;

int main()
{
	freopen("D-small-attempt1.in","r",stdin);
	freopen("D-small-attempt1.out","w",stdout);
	int T,caseT=1;
	bool flag=0;
	cin>>T;
	while (T--){
		flag=0;
		int x,r,c;
		cin>>x>>r>>c;
		if (x>=7)
			flag=1;
		if ((r*c)%x!=0)
			flag=1;
		double temp=ceil(sqrt(x));
		if (x%(int)temp==0)
			temp=x/temp;
		if ((temp>r||temp>c))
			flag=1;
		if (x>r&&x>c)
			flag=1;
		int m=min(r,c);
		int mm=max(r,c);
		if (x-m+1>=mm-1&&x>=4)
			flag=1;
		cout<<"Case #"<<(caseT++)<<": "<<(flag?"RICHARD":"GABRIEL")<<endl;

	}
	return 0;
}