#include <bits/stdc++.h>
using namespace std;

#define fr(i,a,b) for(int i = a; i < b; i++)
#define fre(i,a,b) for(int i = a; i <= b; i++)
#define frd(i,a,b) for(int i = a; i > b; i--)
#define fred(i,a,b) for(int i = a; i >= b; i--)
#define pb push_back
#define SET(a,v) memset(a,v,sizeof a)

#define INF 1e8
#define N 1100

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<vi> vvi;

int t,n,temp;

int bff[N];
int arr[N];
bool mark[N];
int ans;

void go(int pos){
	if (pos > ans){
		int p,l,r;
		bool ok = 1;
		if (pos > 1) fr(i,0,pos){
			p = arr[i];
			l = (i-1+pos)%pos;
			r = (i+1+pos)%pos;
			//printf("n:%d pos:%d i:%d r:%d l:%d\n",n,pos,i,r,l);
			if (bff[p] != arr[l] && bff[p] != arr[r]){
				ok = 0;
				break;
			}
		}
		if (ok){
			ans = pos;
			//fr(i,0,pos) printf("%d ",arr[i]);
			//puts("");
		}
	}
	
	if (pos == n) return;
	
	fre(i,1,n){
		if(!mark[i]){
			mark[i] = 1;
			arr[pos] = i;
			go(pos+1);
			mark[i] = 0;
		}
	}
	
}

void solve(){
	ans = 0;
	
	SET(mark,0);
	go(0);
	printf("%d\n",ans);
}

int main(){
	scanf("%d",&t);
	fr(t2,0,t){
		printf("Case #%d: ",t2+1);
		scanf("%d",&n);
		fre(i,1,n) scanf("%d",&bff[i]);
		solve();		
	}

	return 0;
}