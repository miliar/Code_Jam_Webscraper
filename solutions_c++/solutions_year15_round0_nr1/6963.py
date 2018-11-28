#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <map>
#include <cmath>
#include <string>
#include <cstring>
#include <queue>
#include <stack>
#include <set>
#include <bitset>
#include <time.h>
#define pi acos(-1)
#define inf 0x7fffffff
#define llinf 0x7fffffffffffffffLL
#define eps 0.000001
#define lp(i,n) for(int i=0;i<n;i++)
#define lpb(i,n) for(int i=1;i<=n;i++)
#define fr(i,j,k) for(int i=j;i<k;i++)
#define smap(p,ma) for(p=ma.begin();p!=ma.end();p++)
#define MA(a,b) ((a)>(b)?(a):(b))
#define MI(a,b) ((a)<(b)?(a):(b))
#define PB push_back
#define FIR first
#define SEC second
#define MP make_pair
#define PQ priority_queue
#define MSET multiset
#define NPS string::npos
#define debug
#define DB double
#define MOD 5767169 
#define LL long long int 
#define _max 15
using namespace std;
int T;
string s;
int d,sum;
main(){
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	int o,tp;
	lpb(i,T){
		o=0;
		scanf("%d",&d);
		cin>>s;
		sum = s[0]-'0';
		for(int j=1;j<d+1;j++){
			tp = s[j]-'0'; if(j>sum)o+=j-sum,sum=j;
			sum+=tp;	
		}
		printf("Case #%d: %d\n",i,o);
	}
	
}


