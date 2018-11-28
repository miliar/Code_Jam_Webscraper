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

double a[MX],b[MX];
bool vi[MX];

int main(){
	freopen("D-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int n,i,ra,rb,cs,t=1,j;
	cin>>cs;
	while(cs--){
	    cin>>n;
	    for(i=0;i<n;i++)cin>>a[i];
	    for(i=0;i<n;i++)cin>>b[i];
	    sort(a,a+n);
	    sort(b,b+n);
	    //for(i=0;i<n;i++)cout<<a[i]<<" ";
	    //cout<<endl;
	    //for(i=n-1;i>=0;i--)cout<<b[i]<<" ";
	    //cout<<endl;
	    ra=0;
	    j=0;
	    for(i=0;i<n;i++){
	        if(a[i]>b[j]){
	            ra++;
	            j++;
	        }

	    }
	    rb=0;
	    CLR(vi);
	    reverse(a,a+n);
	    for(i=0;i<n;i++){
	        for(j=0;j<n;j++){
	            if(vi[j])continue;
	            if(b[j]>a[i]){
	                vi[j]=1;
	                break;
	            }
	        }
	        if(j==n){
	            rb++;
	            for(j=0;j<n;j++){
	                if(!vi[j])break;
	            }
	            vi[j]=1;
	        }
	    }
	    printf("Case #%d: %d %d\n",t++,ra,rb);
	}
	return 0;
}


