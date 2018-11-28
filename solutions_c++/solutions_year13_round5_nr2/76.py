#include<cstdio>
#include<algorithm>
using namespace std;

int o[11],a[10],x[10],y[10];
int xmult(int a,int b){return x[a]*y[b]-x[b]*y[a];}
int sgn(int a){return a>0?1:(a<0?-1:0);}
int xmult(int a,int b,int c,int d){
	return a*d-b*c;
}
bool touch(int a,int b,int c,int d){
	if(max(x[a],x[b])<min(x[c],x[d])
	|| max(y[a],y[b])<min(y[c],y[d])
	|| min(x[a],x[b])>max(x[c],x[d])
	|| min(y[a],y[b])>max(y[c],y[d])
	)return false;
	int x1,x2,x3,y1,y2,y3;
	x1 = x[a] - x[d];y1 = y[a] - y[d];
	x2 = x[c] - x[d];y2 = y[c] - y[d];
	x3 = x[b] - x[d];y3 = y[b] - y[d];
	if(sgn(xmult(x1,y1,x2,y2)) * sgn(xmult(x2,y2,x3,y3))<0)
		return false;
	x1 = x[c] - x[b];y1 = y[c] - y[b];
	x2 = x[a] - x[b];y2 = y[a] - y[b];
	x3 = x[d] - x[b];y3 = y[d] - y[b];
	if(sgn(xmult(x1,y1,x2,y2)) * sgn(xmult(x2,y2,x3,y3))<0)
		return false;
	return true;
}
int main(){
	int ti =1;
	int T,n;
	for(scanf("%d",&T);T--;++ti){
		scanf("%d",&n);
		for(int i=0;i<n;++i){
			scanf("%d%d",x+i,y+i);
			o[i] = i;
		}
		int ans= -1;
		o[n]=0;
		do{	int t=0;
			for(int i=0;i<n;++i){
				t+= xmult(o[i],o[i+1]);
			}
			t = abs(t);
			if(t<=ans)continue;
			bool ok = true;
			for(int i=0;i<n && ok;++i)
				for(int j=i+2;j<n-(i==0) && ok;++j)
					if(touch(o[i],o[i+1],o[j],o[j+1]))
						ok= false;
			if(ok){
				ans = t;
				for(int i=0;i<n;++i)a[i] = o[i];
			}
		}while(next_permutation(o+1,o+n));
		printf("Case #%d:",ti);
		for(int i=0;i<n;++i)printf(" %d",a[i]);
		puts("");
	}
}
