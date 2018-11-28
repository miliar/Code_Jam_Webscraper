#include<stdio.h>
#include<algorithm>
#include<math.h>
using namespace std;
double x[2100];
double y[2100];
double z[2100];
int UF[2100];
int FIND(int a){
	if(UF[a]<0)return a;return UF[a]=FIND(UF[a]);
}
void UNION(int a,int b){
	a=FIND(a);b=FIND(b);if(a==b)return;
	UF[a]+=UF[b];UF[b]=a;
}
double dist(int a,int b){
	return sqrt((x[a]-x[b])*(x[a]-x[b])+(y[a]-y[b])*(y[a]-y[b])+(z[a]-z[b])*(z[a]-z[b]));
}
pair<double,pair<int,int> > edge[1100000];
int main(){
	int T;scanf("%d",&T);
	for(int t=1;t<=T;t++){
		int a,b;scanf("%d%d",&a,&b);
		for(int i=0;i<a;i++){
			double g1,g2,g3;
			scanf("%lf%lf%lf%lf%lf%lf",x+i,y+i,z+i,&g1,&g2,&g3);
		}
		printf("Case #%d: ",t);
		int sz=0;
		for(int i=0;i<a;i++)for(int j=i+1;j<a;j++){
			edge[sz++]=make_pair(dist(i,j),make_pair(i,j));
		}
		for(int i=0;i<a;i++)UF[i]=-1;
		std::sort(edge,edge+sz);
		for(int i=0;i<sz;i++){
			UNION(edge[i].second.first,edge[i].second.second);
			if(FIND(0)==FIND(1)){
				printf("%.12f\n",edge[i].first);break;
			}
		}
	}
}