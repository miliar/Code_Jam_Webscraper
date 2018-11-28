#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <cmath>
#include <string>
#include <cstring>
#include <cctype>
#include <cstdlib>
using namespace std;
int check(long long int i)
{
	long long int z=0,t=i;
	while (t != 0) {
		z=z*10+t%10;
		t=t/10;
	}
//	printf("z is %d & i is %d \n",z,i);
	if(i==z) {
		return 1;
	}
	else
		return 0;
}
int main()
{
	int q;
	long long int a[100000],count=0;
	long long int i;
	for(i=1;i<=10000000;i++)
	{
		q=check(i);
		if(q==true) {
//			printf("%d ",i);
			q=check(i*i);
			if(q==true) {
//				printf("%lld \n",i*i);
				a[count++]=i*i;
			}
		}
	}
//	cout<<count<<endl;
	int tc;
	scanf("%d",&tc);
        long long int j;
 	for(j=1;j<=tc;j++) {
		long long int c,b;
		scanf("%lld%lld",&c,&b);
		int k=0;
		for(i=0;i<count;i++) {
			if (a[i]>=c&&a[i]<=b) {
				k++;
			}
		}
		printf("Case #%d: %lld\n",j,k);
	}
	return 0;
}

