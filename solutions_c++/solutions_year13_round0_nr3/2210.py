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
#define cllft lft,st,mid,s,e
#define clrgt rgt,mid+1,ed,s,e
#define inf (1<<29)
#define i64 long long
#define MX 1000002

typedef pair<int,int> pii;

vector<int> a;

bool palin(i64 n){
    char a[20],b[20];
    sprintf(a,"%lld",n);
    strcpy(b,a);
    reverse(b,b+strlen(b));
    return strcmp(a,b)==0;
}

int main(){
	freopen("C-large-1.in","r",stdin);
	freopen("out.txt","w",stdout);
	i64 i,x,y,xx,yy;
	int cs,t=1,res;
	for(i=1;i<=10000000;i++)if(palin(i) && palin(i*i))a.pb(i);
	//cout<<a.size()<<endl;
	cin>>cs;
	while(cs--){
	    cin>>x>>y;
	    xx=sqrt(x);
	    if(xx*xx!=x)xx++;
	    yy=sqrt(y);
	    res=upper_bound(all(a),yy)-lower_bound(all(a),xx);
	    printf("Case #%d: %d\n",t++,res);
	}
	return 0;
}


