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
#define MX 102

typedef pair<int,int> pii;

int mat[MX][MX],n,m,a[MX][MX];
bool vi[MX][MX];

bool extendPossible(int x,int y,int dx,int dy,int val){
    if(x>=n || y>=m)return true;
    if(mat[x][y]>val)return false;
    return extendPossible(x+dx,y+dy,dx,dy,val);
}

void extend(int x,int y,int dx,int dy,int val){
    if(x>=n || y>=m)return;
    a[x][y]=val;
    extend(x+dx,y+dy,dx,dy,val);
}

bool possible(){
    int x,y,mx,i,j;
    while(1){
        mx=0;
        for(i=0;i<n;i++)for(j=0;j<m;j++)if(!vi[i][j] && mx<mat[i][j]){mx=mat[i][j];x=i;y=j;}
        if(!mx)break;
        vi[x][y]=1;
        if(extendPossible(x,0,0,1,mx))extend(x,0,0,1,mx);
        if(extendPossible(0,y,1,0,mx))extend(0,y,1,0,mx);
    }
    /*
    for(i=0;i<n;i++){
        for(j=0;j<m;j++)cout<<a[i][j]<<" ";
        cout<<endl;
    }
    */
    for(i=0;i<n;i++)for(j=0;j<m;j++)if(a[i][j]!=mat[i][j])return false;
    return true;
}

int main(){
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int cs,i,j,t=1;
	cin>>cs;
	while(cs--){
	    cin>>n>>m;
	    for(i=0;i<n;i++){
	        for(j=0;j<m;j++){
	            cin>>mat[i][j];
	            a[i][j]=100;
	            vi[i][j]=0;
	        }
	    }
	    if(possible())printf("Case #%d: YES\n",t++);
	    else printf("Case #%d: NO\n",t++);
	}
	return 0;
}


