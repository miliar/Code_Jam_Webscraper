#include <iostream>
#include<cstdio>
#include<set>
using namespace std;
set <int> s;
set<int>::iterator it;
int main() {
	// your code goes here
	int t;
	scanf("%d",&t);
	for(int j=1;j<=t;j++)
	{
		s.clear();
		long int n,sum=0,dsum;
		bool flag=0;
		scanf("%ld",&n);
		for(int i=1;i<=100;i++)
		{
			sum+=n;
			dsum=sum;
			while(dsum){
				s.insert(dsum%10);
				dsum/=10;
			}
			if(s.size()==10){
				flag=1;
				break;
			}
		}
		if(flag)
		{
			printf("Case #%d: %ld\n",j,sum);
		}
		else{
			printf("Case #%d: INSOMNIA\n",j);
		}
	}
	return 0;
}