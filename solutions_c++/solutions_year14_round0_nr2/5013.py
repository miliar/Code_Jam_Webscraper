//Copyright © 1993-2014 RishabhJain,Inc
#include <iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<climits>
#include<cmath>
#include<vector>
#include<algorithm>
#include<map>
#include<list>
#include<utility>
 
#define sc(a) scanf("%c",&a)
#define pc(a) printf("%c",a)
#define sd(a) scanf("%d",&a)
#define pd(a) printf("%d\n",a)
#define sll(a) scanf("%lld",&a)
#define pll(a) printf("%lld",a)
#define ss(a) scanf("%s",&a)
#define ps(a) cout<<a
#define FOR(a,b,c) for(a=b;a<c;++a)
#define pii pair<int,int>
#define pub(a) push_back(a)
#define pob() pop_back()
#define puf(a) push_front(a)
#define pof() pop_front()
using namespace std;
int main() {
	// your code goes here
	int k,n,i;
	double c,f,x,t,p;
	sd(k);
	FOR(i,1,k+1)
	{
		n=0;
		cin>>c>>f>>x;
		t=x/2;
		while(1)
		{
			p=(c-x)/(2+n*f)+x/(2+(n+1)*f);
			if(p<0)
			{
				t+=p;
				n++;
			}
			else
			break;
		}
		cout<<"Case #"<<i<<": ";
		printf("%0.7f\n",t);
	}
	return 0;
}