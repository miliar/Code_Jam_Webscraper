#include<iostream>
#include<map>
#include<string>
#include<string.h>
#include<vector>
#include<stdio.h>
#include <cstdio>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <sstream>
#include <cmath>
#include <bitset>
#include <utility>
#include <set>
#include <functional>
#include <math.h>
#define LL long long int
#define ii pair< int,int >
#define iii pair< int , ii > 
#define vi vector<int>
#define vii vector<ii>
#define II pair< LL , LL >
#define III pair< LL  , LL > 
#define vI vector<LL>
#define rI(B) scanf("%d",&B)
#define wI(B) printf("%d",B)
#define R(i) freopen(i,"r",stdin)
#define W(i) freopen(i,"w",stdout)
#define R_W R("A-large.in"),W("o.txt");
#define FOR(i,f,t) for(int i=f;i<t;i++)
#define r(e) for(int i=0;i<e;i++)
#define EPS 1e-9
using namespace std;
int main(){
	R_W;
	int t;
	cin>>t;
	int cases=1;
	while(t--)
	{
		string in;
		int k;
		cin>>in>>k;
		int ans=0;
		bool noSolution=false;
		r(in.size())
		{
			if(in[i]=='-')
			{
				ans++;
				int j=0;
				for(;j<k && i+j<in.size();j++)
				{
					if(in[i+j]=='-') in[i+j]='+';
					else in[i+j]='-';
				}
				if(j<k){
					noSolution=true;
					printf("Case #%d: IMPOSSIBLE\n",cases++);
					break;
				}
			}
		}
		if(noSolution) continue;
		printf("Case #%d: %d\n",cases++,ans);
	}
	return 0;
}