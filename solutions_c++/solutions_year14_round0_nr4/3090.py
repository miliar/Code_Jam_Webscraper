#include<iostream>
#include<cstdio>
#include<climits>
#include<string>
#include<cstring>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<cmath>
#include<queue>
#include<utility>
#include<fstream>
using namespace std;

#define inp(a) scanf("%d",&a)
#define out(a) printf("%d\n",a)
#define inpll(a) scanf("%lld",&a)
#define outll(a) printf("%lld\n",a)

#define swap(a,b) {a=a+b;a=a-b;b=a-b;} 
#define VI vector<int>
#define VLL vector<long long int>
#define PQI priority_queue<int>
#define PQLL priority_queue<long long int>
#define VP vector<pair<int,int> >

#define ll long long int
#define mod 1000000007
 
#define mp make_pair 
#define X first
#define Y second
#define pb push_back
#define rep(i,a,b) for(i=a;i<b;i++)


/*inline void in(int *n)
{
    *n = 0;
    int ch = getchar_unlocked();
    while(ch < '0' || ch > '9') 
    {
        ch = getchar_unlocked();
    }
    while(ch >= '0' && ch <= '9')
        (*n) = ((*n)<<3) + ((*n)<<1) + ch - '0', ch = getchar_unlocked();
}*/
/*bool compare(const pair<ll,ll>& p,const pair<ll,ll> &q){
	return p.X<q.X;
}*/
int i,j,k,n,t,w;
double a[1005],b[1005];
int main(){
	ifstream inputit("41.txt");
	ofstream outputit("example1.txt");
	inputit>>t;
	w=1;
	while(w<=t){
		int mark[1005]={0};
		//inp(n);
		inputit>>n;
		rep(i,0,n) inputit>>a[i];//scanf("%lf",&a[i]);
		rep(i,0,n) inputit>>b[i];//scanf("%lf",&b[i]);
		sort(a,a+n); sort(b,b+n);
		/*rep(i,0,n) cout<<a[i]<<" ";
		cout<<'\n';
		rep(i,0,n) cout<<b[i]<<" ";
		cout<<'\n';*/
		int flag=1,cnt1,cnt2;
		for(i=n-1,j=n-1,cnt1=0;j>=0;){
			if(a[i]<b[j]){
				j--;
			}
			else{
				j--; i--; cnt1++;
			}
		}
		
		cnt2=0;
		for(i=n-1,j=n-1;i>=0;i--){
			if(b[j]>a[i]){
				j--; 
				cnt2++;
			}
		}
		outputit<<"Case #"<<w<<": "<<cnt1<<" "<<n-cnt2<<endl;
		//printf("Case #%d: %d %d\n",w,cnt1,n-cnt2);
		w++;
	}
	return 0;
}
