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

int i,j,k,n,t,a[20][20],b[20][20],m,w;
int main(){
	inp(t);
	w=1;
	while(w<=t){
		int mark1[100]={0},mark2[100]={0};
		inp(n);
		n-=1;
		rep(i,0,4){
			rep(j,0,4){
				inp(k);
				if(i==n) mark1[k]=1;
			}
		} 
		
		inp(m);
		m-=1;
		rep(i,0,4){
			rep(j,0,4){
				inp(k);
				if(i==m) mark2[k]=1;
			}
		}
		
		int cnt=0,idx=1;
		rep(i,1,17){
			if(mark1[i]==1){
				if(mark2[i]==1) {
					cnt++; idx=i;
				}
			} 
		} 
		 
		if(cnt==1) printf("Case #%d: %d\n",w,idx);
		else if(cnt>1) printf("Case #%d: Bad magician!\n",w);
		else printf("Case #%d: Volunteer cheated!\n",w);
		w++;
	}
	return 0;
}
