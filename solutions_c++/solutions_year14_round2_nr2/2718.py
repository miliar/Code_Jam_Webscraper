
#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	//freopen("11.in","r",stdin);
	//freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	for(int c1=1;c1<=t;c1++){
	int a,b,k,ret=0;
	cin>>a>>b>>k;
	for(int i=0;i<a;i++)
		for(int j=0;j<b;j++)
			if((i&j)<k)
			{
				ret++;
			}
				
	printf("Case #%d: %d\n",c1,ret);
	}
	return 0;
}
