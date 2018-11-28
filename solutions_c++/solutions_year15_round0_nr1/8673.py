#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include <vector>
using namespace std;
int main()
{
	   freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
	int n;
	int g  = 0;
	scanf("%d",&n);
	while(n--){
		g++;
		
		int a;
		char c[1024];
		scanf("%d",&a);
		scanf("%s",c);
		
		int sum = 0;
		int sum1 = 0;
		for(int i = 0;i<=a;i++){
			int temp = c[i]-'0';
			if(sum < i && temp>0){
				sum1 += i-sum;
				sum+=i-sum;
			}
			sum+=temp;
		//	cout<<sum<<endl;
		}
		
		printf("Case #%d: %d\n",g,sum1);
	}
	return 0;
}

