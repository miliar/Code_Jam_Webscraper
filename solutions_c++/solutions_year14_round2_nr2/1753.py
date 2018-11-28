#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
main()
{
	int tc,cs=0;
	cin>>tc;
	while(tc)
    {
    cs++;
    int a,b,k,reslt=0;
	cin>>a>>b>>k;
	for(int i=0;i<a;i++)
		for(int j=0;j<b;j++)
			if((i&j)<k)
				reslt++;
	printf("Case #%d: %d\n",cs,reslt);
	tc--;
	}
}
