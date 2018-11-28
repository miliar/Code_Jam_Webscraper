#include<set>
#include<map>
#include<cmath>
#include<queue>
#include<stack>
#include<vector>
#include<cctype>
#include<cstdio>
#include<string>
#include<sstream>
#include<cstring>
#include<cstdlib>
#include<fstream>
#include<iterator>
#include<iostream>
#include<algorithm>

using namespace std;

#pragma comment(linker,"/STACK:16777216")
#pragma warning(disable:4786)

#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))
#define myabs(a) ((a)<0?(-(a)):(a))
#define pi acos(-1.0)
#define CLR(a) memset(a,0,sizeof(a))
#define SET(a) memset(a,-1,sizeof(a))
#define pb push_back
#define all(a) a.begin(),a.end()
#define ff first
#define ss second
#define eps 1e-9
#define root 1
#define lft 2*idx
#define rgt 2*idx+1
#define cllft lft,st,mid
#define clrgt rgt,mid+1,ed
#define inf (1<<29)
#define i64 long long
#define MX 1000002

typedef pair<int,int> pii;

int main(){
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int cs,t=1;
	double c,f,x,r,ans,tt;
	cin>>cs;
	while(cs--){
	    cin>>c>>f>>x;
	    r=2;
	    ans=x/2;
	    tt=0;
	    while(1){
	        tt+=c/r;
	        if(tt>ans+eps)break;
	        r+=f;
	        if(ans> (tt + x/r)+eps){
	            ans=tt + x/r;
	        }
	    }
	    printf("Case #%d: %.7lf\n",t++,ans);
	}
	return 0;
}


