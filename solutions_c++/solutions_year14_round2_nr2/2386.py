#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
#include<vector>
#include<set>
#include<map>
#include<algorithm>
#include<cmath>
#include<sstream>
#include<bitset>

using namespace std ;

int main ()
{
	freopen("out.txt","w",stdout);

	int t , a, b ,k , cnt = 0 , c= 0;

	cin>>t;

	while(t--)
	{
		cin>>a>>b>>k;
		c++;
		cnt =0;

		for(int i=0;i<a;i++)
			for(int j=0;j<b;j++)
				if((i & j) <k)
					cnt++;

		printf("Case #%d: %d\n",c,cnt);
	}

	return 0;
}
