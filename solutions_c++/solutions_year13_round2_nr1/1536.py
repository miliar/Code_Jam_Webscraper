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

typedef unsigned long long ul;
typedef long double ld;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<vector<int> > VVI;
typedef pair<int,int> PII;
long long a[1000010];
int main(){
	
	freopen("alarge.txt","r",stdin);
	freopen("outlarge.txt","w",stdout);
	int Kase=GI;
	long long x,n,i,c,s,j,y;
	FOR(kase,1,Kase+1){
		cin>>x>>n;
		
        for(i=0;i<n;i++)cin>>a[i];
        sort(a,a+n);
        //for(i=0;i<n;i++)cout<<a[i]<<" ";
        c=n;s=0;j=0;
        vector<int> b;
        for(i=0;i<n;i++){if(a[i]<x)x+=a[i];else { y=s+(n-i);b.push_back(y);j++;if(x==1)break;
        while(x<=a[i]){x+=x-1;s++;} x+=a[i]; b.push_back(s+n-i-1);j++;} }
        if(s!=0){b.push_back(s);j++;}
        if(j==0)c=0;else { for(i=0;i<j;i++)if(b[i]<c)c=b[i];}
        printf("Case #%d: ",kase);
        cout<<c<<endl;		b.clear();
	}
	return 0;
}
