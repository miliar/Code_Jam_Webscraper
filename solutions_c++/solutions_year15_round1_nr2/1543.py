#include <cstdio>
#include <algorithm>
#include <iostream>
#include <stack>
#include <vector>
#include <bits/stdc++.h>
using namespace std;
#define maxn 1000009
int a[maxn];
long long gcd(long long a,long long b){
	if(a==0)return b;
	return gcd(b%a,a);
}
struct number1{
    int x;
    int id;
    bool operator < (const number1 &a) const {
    	if(x==a.x)return id>a.id;
        return x>a.x;//最小值优先
    }
}dd;
int main()
{
	freopen("B-small-attempt2.in","r",stdin);
	freopen("t.out","w",stdout);
	int T;
	int cs=1;
	cin>>T;
	while(T--){
		int b,n;
		cin>>b>>n;
		long long g=0,lc=1;
		cin>>a[0];
		lc=g=a[0];
		for(int i=1;i<b;i++)scanf("%d",&a[i]),g=gcd(a[i],g),lc=lc*a[i]/g;
		int N=0;
		for(int i=0;i<b;i++){
			N+=lc/a[i];
		}
		n=n%N;
		if(n==0)n=N;
		 priority_queue<number1> q;
		for(int i=0;i<b;i++){
			dd.x=0;
			dd.id=i+1;
			q.push(dd);
		}
		int ans=0;
		while(n){
			dd=q.top();
			q.pop();
			dd.x+=a[dd.id-1];
			q.push(dd);
			n--;
			if(n==0){
				ans=dd.id;
			}
		}
		printf("Case #%d: %d\n",cs++,ans);
	}
}