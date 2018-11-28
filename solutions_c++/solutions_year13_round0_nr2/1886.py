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

int main(){
	
	freopen("blarge.txt","r",stdin);
	freopen("bout.txt","w",stdout);
	int Kase=GI;
	int n,m,a[111][111],mx,c,i,j;
	FOR(kase,1,Kase+1){
		cin>>n>>m;
		printf("Case #%d: ",kase);
        mx=0;
        for(i=0;i<n;i++)  { mx=0; for(j=0;j<m;j++){ cin>>a[i][j];if(mx<a[i][j])mx=a[i][j];}a[i][m]=mx;}
        for(j=0;j<m;j++) { mx=0;for(i=0;i<n;i++){ if(mx<a[i][j])mx=a[i][j];} a[n][j]=mx;}
        c=0;for(i=0;i<n;i++) for(j=0;j<m;j++) if(a[i][j]<a[i][m] && a[i][j]<a[n][j]){c=1;break;}
        if(c==0)cout<<"YES";else cout<<"NO";cout<<endl;
	}
	return 0;
}
