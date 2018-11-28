#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<cstdlib>
using namespace std;
struct point{
	double x;
	double y;
	double jiaodu;
	int id;
}map[3005],zhan[3005];
bool que(struct point x,struct point y){
	if(x.jiaodu==y.jiaodu){ 
		if(x.y!=y.y) return x.y<y.y;
		else return x.x<y.x;
	}
	else return x.jiaodu<y.jiaodu;
};
int start,ans[3005];
int main(){
	freopen("E:C-small-attempt1.in","r",stdin);
	freopen("E:C-small-attempt1.out","w",stdout);
	int i,j,m,n,l,xuhao,T,vcase=0,st,vmax;
	double r,ymin,xmin,a,b,c,d,x,y,s;
	scanf("%d",&T);
	while(T--){
		scanf("%d%",&n);
		ymin=INT_MAX;
		xmin=INT_MAX;
		for(i=1;i<=n;i++){
			scanf("%lf%lf",&map[i].x,&map[i].y);
			map[i].id=i;
			ans[i]=n;
		}
		printf("Case #%d:\n",++vcase);
		vmax=1<<n;
		if(n>2){
			for(st=1;st<vmax;st++){
				ymin=INT_MAX;
				xmin=INT_MAX;
				for(i=1;i<=n;i++){
					if( ( (st>>(map[i].id-1) )&1)==0) continue;
					if(map[i].y<ymin ||(map[i].y==ymin && xmin>map[i].x) ){
						ymin=map[i].y;
						xmin=map[i].x;
						xuhao=i;
					}
				}
				map[n+1]=map[xuhao];
				map[xuhao]=map[1];
				map[1]=map[n+1];
				for(i=2;i<=n;i++){
					map[i].jiaodu=atan2(map[i].y-map[1].y,map[i].x-map[1].x);
				}
				sort(map+2,map+n+1,que);
				for(i=2;i<=n;i++){
					if( ( (st>>(map[i].id-1) )&1)==0) continue;
					zhan[2]=map[i];
					break;
				}
				zhan[1]=map[1];
				start=2;
				for(i=3;i<=n;i++){
					if( ( (st>>(map[i].id-1) )&1)==0) continue;
					do{
						if(start>1){
							a=zhan[start].x-zhan[start-1].x;
							b=zhan[start].y-zhan[start-1].y;
							c=map[i].x-zhan[start].x;
							d=map[i].y-zhan[start].y;
							if(a*d-b*c<0)
								start--;
							else
								zhan[++start]=map[i];
						}
						else
							zhan[++start]=map[i];
					}while(a*d-b*c<0);
				}
				int vt=0;
				for(i=1;i<=n;i++){
					if( (st>>(i-1) )&1) vt++;
				}
				for(i=1;i<=start;i++){
					ans[zhan[i].id]=min(ans[zhan[i].id],n-vt);
				}
				for(i=1;i<=n;i++){
					if( ( (st>>(map[i].id-1) )&1)==0) continue;
					if((zhan[start].y-zhan[1].y)*(map[i].x-zhan[1].x)==(map[i].y-zhan[1].y)*(zhan[start].x-zhan[1].x)) ans[map[i].id]=min(ans[map[i].id],n-vt);
				}
			}
			for(i=1;i<=n;i++){
				printf("%d\n",ans[i]);
			}
		}
		else{
			for(i=1;i<=n;i++){
				printf("0\n");
			}
		}
	}
	return 0;
}