#include<stdio.h>
#include<string>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<iostream>
#include <cassert>
#include<map>
#include<queue>
#include<stack>
#include<time.h>
#include<math.h>
#include<set>
using namespace std;
#define INF 0x3f3f3f3f
#define DINF 1e100
#define EPS 1e-15
#define PII acos(-1)
#define LL long long
#define Pii pair<int,int>
#define For(i,n) for(int i=0;i<n;i++)
#define ileer(n) scanf("%d",&n)
#define fleer(n) scanf("%f",&n)
#define MK make_pair
#define PB push_back
#define llenar(arr,val) memset(arr,val,sizeof(arr))

int main(){
	
	int t;
	ileer(t);
	For(c,t){
		int n;
		ileer(n);
		string g;
		cin>>g;
		int parados,can=0;
		parados=g[0]-'0';
		for(int i=1;i<g.size();i++){
			int act=g[i]-'0';
			if(parados<i){ can+=(i-parados); parados+=(i-parados);}
			parados+=act;
		}
		printf("Case #%d: %d\n",c+1,can);
	}
	
	
}