#include<cstdio>
#include<cstring>
#include<vector>
#include<queue>
#include<algorithm>
#include<cmath>
#include<climits>
#include<string>
#include<set>
#include<map>
#include<iostream>
using namespace std;
#define rep(i,n) for(int i=0;i<((int)(n));i++)
#define reg(i,a,b) for(int i=((int)(a));i<=((int)(b));i++)
#define irep(i,n) for(int i=((int)(n))-1;i>=0;i--)
#define ireg(i,a,b) for(int i=((int)(b));i>=((int)(a));i--)
typedef long long int lli;
typedef pair<int,int> mp;
#define fir first
#define sec second
#define IINF INT_MAX
#define LINF LLONG_MAX
#define eprintf(...) fprintf(stderr,__VA_ARGS__)
#define pque(type) priority_queue<type,vector<type>,greater<type> >
#define memst(a,b) memset(a,b,sizeof(a))


int w,h,n;
vector<mp> dat;

bool iscr(mp pa,mp pb){
	if(pa.fir>pb.fir)swap(pa,pb);
	//printf("(%d %d) (%d %d)\n",pa.fir,pa.sec,pb.fir,pb.sec);
	if(pa.sec>pb.fir && pb.sec>pa.sec)return true;
	else return false;
}

typedef pair<int,mp> mmp;

char ans[110][110];

int dy[4]={1,0,-1,0};
int dx[4]={0,-1,0,1};



bool canov(int y,int x,int d,int a){
	//printf("canov? %d %d %d %d\n",y,x,d,a);
	char c = '/';
	if((d+a)%2==1)c = '\\';
	if(ans[y][x]==-1)ans[y][x]=c;
	else if(ans[y][x]!=c)return false;
	return true;
}

void itop(int k,int &y,int &x,int &d){
	if(k<=w){
		y=0; x=k; d=0;
	}
	else if(k<=w+h){
		y=k-w; x=w+1; d=1;
	}
	else if(k<=w+h+w){
		y=h+1; x=w+1-(k-w-h); d=2;
	}
	else{
		y=h+1-(k-w-h-w); x=0; d=3;
	}
}

bool isout(int y,int x){
	if(y<0 || x<0)return true;
	if(y>h+1 || x>w+1)return true;
	return false;
}


bool solve(){
	int ls = dat.size();
	rep(i,ls){
		rep(j,i){
			if(iscr(dat[i],dat[j]))return false;
		}
	}
	
	vector<mmp> v;
	rep(i,ls){
		mp pa = dat[i];
		int d = (n+pa.sec-pa.fir)%n;
		if(d>n-d){
			d = n-d;
			swap(pa.fir,pa.sec);
		}
		v.push_back(mmp(d,pa));
	}
	sort(v.begin(),v.end());
	
	memset(ans,-1,sizeof(ans));
	rep(i,v.size()){
		mp pa = v[i].sec;
		//printf("v[%d] .. %d (%d %d)\n",i,v[i].fir,pa.fir,pa.sec);
		int p = pa.fir,q=pa.sec;
		int nx,ny,gx,gy;
		int d;
		itop(q,gy,gx,d);
		itop(p,ny,nx,d);
		
		/*
		printf("(%d %d)\n",p,q);
		printf("%d %d %d\n",ny,nx,d);
		printf("%d %d\n",gy,gx);
		*/
		
		while(nx!=gx || ny!=gy){
		//rep(qqq,20){
			
			
			//printf("%d %d %d\n",ny,nx,d);
			if(isout(ny,nx))return false;
			/*
			reg(y,1,h){
				reg(x,1,w){
					printf("%c ",ans[y][x]==-1?'.':ans[y][x]);
				}
				printf("\n");
			}*/
			
			
			
			int td = (d+3)%4;
			int ty = ny + dy[d];
			int tx = nx + dx[d];
			if(canov(ty,tx,d,1)){
				ny = ty; nx = tx; d = td;
			}
			else{
				td = (d+1)%4;
				ty = ny + dy[d];
				tx = nx + dx[d];
				if(canov(ty,tx,d,0)){
					ny = ty; nx = tx; d = td;
				}
				else return false;
			}
		}
	}
	
	reg(y,1,h){
		reg(x,1,w){
			if(ans[y][x]==-1)ans[y][x]='/';
		}
	}
	return true;
}

/*
1
1 3
1 8 2 7 3 4 5 6

1
16 1
29 30 34 3 19 24 28 27 21 20 13 14 7 6 1 2 31 32 16 17 4 5 25 26 8 9 11 12 18 15 22 23 33 10

*/

int main(void){
	int qn;
	scanf("%d",&qn);
	reg(i,1,qn){
		scanf("%d%d",&h,&w);
		dat.clear();
		n = (w+h)*2;
		rep(j,h+w){
			int a,b;
			scanf("%d%d",&a,&b);
			if(a>b)swap(a,b);
			dat.push_back(mp(a,b));
		}
		printf("Case #%d:\n",i);
		if(solve()){
			reg(y,0,h+1)ans[y][0]=ans[y][w+1]='\0';
			reg(x,0,w+1)ans[0][x]=ans[h+1][x]='\0';
			
			reg(y,1,h){
				printf("%s\n",ans[y]+1);
			}
		}
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}




