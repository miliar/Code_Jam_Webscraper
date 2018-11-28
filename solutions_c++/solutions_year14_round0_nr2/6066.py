#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<set>
#include<queue>
#include<list>
#include<vector>
#define LL long long
#define INF 0x7fffffff
#define For(i,a,b) for(int i=a; i<b; ++i)
using namespace std;
typedef pair<int,int> ii;
int main(){
		
	int T;
	cin>>T;
	for(int c=1; c<=T; ++c){
		double C, F, X;
		cin>>C>>F>>X;
		double r = F*(X-C)/C;
		double ans=0;
		double i;
		for(i = 2; i<=r; i+=F){
			ans+=C/i;
		}
		ans+=X/i;
		printf("Case #%d: %.7lf\n", c,ans);
	}
	return 0;
}
