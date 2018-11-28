#include<iostream>
#include<stdio.h>
using namespace std;
main()
{
	int o,i;
	cin>>o;
	for(i=1;i<=o;i++){
	int a,b,k,count=0;
	cin>>a>>b>>k;
	for(int i=0;i<a;i++)
		for(int j=0;j<b;j++)
			if((i&j)<k)
				count++;

	printf("Case #%d: %d\n",i,count);
	}
}
