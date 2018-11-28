#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstdio>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <string.h>
#include <cassert>

using namespace std;

#define GI ({int t;scanf("%d",&t);t;})
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define sz size()
#define INF (int)1e9

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<vector<int> > VVI;
typedef pair<int,int> PII;

int ispal(LL i){  LL x=i,r,s;r=0;s=0;while(x!=0){r=x%10;s=s*10+r;x=x/10;}x=i;
                    int f=1;while(x!=0){ if(x%10!=s%10){f=0;break;}x=x/10;s=s/10;}
                    return f;
     }
int main(){
	
	freopen("xxx.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int Kase=GI;
	LL i,j,a,b,c;
    LL p[10000];memset(p,0,sizeof(p));
	j=0;for(i=1;i<=10000000;i++)if(ispal(i) && ispal(i*i)){ //cout<<i<<" "<<i*i<<endl;
    p[j++]=i*i;}
	//for(i=0;i<j;i++)cout<<p[i]<<" ";cout<<j;
	FOR(kase,1,Kase+1){
		cin>>a>>b;
		printf("Case #%d: ",kase);
        c=0;for(i=0;i<=j;i++)if(p[i]>=a && p[i]<=b)c++;
        cout<<c<<endl;		
	}
	return 0;
}
