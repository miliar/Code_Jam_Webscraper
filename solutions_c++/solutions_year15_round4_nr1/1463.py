#include <bits/stdc++.h>
#define loop(i,a,b) for(i=a;i<b;i++)
#define rev(i,a,b) for(i=a;i>=b;i--)
#define itloop(i,a) for(i=a.begin();i!=a.end();i++)
#define x first
#define y second
#define pushb(a) push_back(a)
#define pushf(a) push_front(a)
#define popb()   pop_back()
#define popf()   pop_front()
#define setmem(a,val) memset(a,val,sizeof(a))
#define LEN 105

using namespace std;
typedef long long int large;
typedef pair<int,int> ii;

int R,C,m[LEN][LEN],rcref[LEN*LEN],rclen;
ii rc[LEN*LEN];
char line[2*LEN];

bool thisat(int i, int j, int d){
	if     (d==0 && rc[i].x==rc[j].x && rc[j].y<rc[i].y) return true;
	else if(d==1 && rc[i].y==rc[j].y && rc[j].x<rc[i].x) return true;
	else if(d==2 && rc[i].x==rc[j].x && rc[j].y>rc[i].y) return true;
	else if(d==3 && rc[i].y==rc[j].y && rc[j].x>rc[i].x) return true;
	return false;
}

bool anyat(int i, int d){
	int j;
	loop(j,0,rclen) if(thisat(i,j,d)) return true;
	return false;
}
bool any(int i){
	int d;
	loop(d,0,4) if(anyat(i,d)) return true;
	return false;
}

large solve(){
	int i,j,ans=0;
	loop(i,0,rclen){
		if(anyat(i,rcref[i])) continue;
		if(any(i)) ++ans;
		else return -1;
	}
	return ans;
}

// l,u,r,d

int main(){
	int ntc,test=1,r,c,ans,i;
	//freopen("pegman.txt","r",stdin);
	freopen("large.in","r",stdin);
	//freopen("large.out","w",stdout);
	scanf("%d",&ntc);
	while(ntc--){
		scanf("%d %d",&R,&C);
		rclen=0;
		loop(r,0,R){
			scanf("%s",line);
			loop(c,0,C){
				m[r][c]= (line[c]=='<'? 0: (line[c]=='^'? 1: (line[c]=='>'? 2: (line[c]=='v'? 3: -1))));
				if(m[r][c]>=0) rc[rclen].x=r, rc[rclen].y=c, ++rclen;
			}
		}
		loop(i,0,rclen) rcref[i]=m[rc[i].x][rc[i].y];
		ans = solve();
		if(ans==-1)	printf("Case #%d: IMPOSSIBLE\n",test++);
		else printf("Case #%d: %lld\n",test++,ans);
	}
	return 0;
}

