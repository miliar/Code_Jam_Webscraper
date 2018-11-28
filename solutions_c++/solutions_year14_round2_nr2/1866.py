#include<iostream>
#include<cstdio>
#include<algorithm>

using namespace std;

int main()
{
    int T;
	scanf("%d",&T);
	for(int c=1;c<=T;c++){
	int a,b,k,ret=0;
	cin>>a>>b>>k;
	for(int i=0;i<a;i++)
		for(int j=0;j<b;j++)
			if((i&j)<k)
				ret++;
	printf("Case #%d: %d\n",c,ret);
	}
}