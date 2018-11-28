#include<bits/stdc++.h>
using namespace std;

int mark(int n, bool digit[])
{
	int count = 0;
	while(n)
	{
		if(!digit[n%10]++) {
			count++;
		}
		n/=10;
	}
	return count;
}

int main()
{
    freopen("inputalarge.in","r",stdin);
    freopen("output.txt","w",stdout);
	int t;
	scanf("%d", &t);
	for(int i=1; i<=t; i++) {
		int n;
		scanf("%d",&n);
		if(!n)
			printf("Case #%d: INSOMNIA\n",i);
		else {
			int num = n;
			bool digit[10] = {false};
			int count = mark(n, digit);
			//cout<<count<<endl;
			int j = 2;
			while( count<10 && j<100) {
				num+=n;
				count+=mark(num, digit);
                j++;
			}
			printf("Case #%d: %d\n", i, num);
		}
	}
	return 0;
}
