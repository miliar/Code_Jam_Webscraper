#include <bits/stdc++.h>
using namespace std;
int c=0;int l;
map<int,int> m;
void fun(int x)
{
	l=x;
	while(x>0)
	{
		int te=x%10;
		x/=10;
		if(m[te]==0)
		{c++;m[te]++;}
		if(c==10)
		return ;
	}
}
int main() {
	// your code goes here
	int i,t,n,test=1,mul;
	scanf("%d",&t);
	while(t--)
	{
		c=0;mul=1;
		scanf("%d",&n);
		printf("Case #%d: ",test++);
		if(n==0) printf("INSOMNIA\n");
		else
		{
			while(c<10) fun(n*(mul++));	
			printf("%d\n",l);
		}
		m.clear();
	}
	return 0;
}