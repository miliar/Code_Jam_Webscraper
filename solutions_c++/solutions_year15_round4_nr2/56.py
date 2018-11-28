#include<stdio.h>
int tcn,tc;
int n;
double v,x;
double c[110];
double r[110];
int chk[110];
bool same(double x,double y){
	if(x+0.00001>y&&y+0.00001>x)return true;
	return false;
}
int main(){
	int i,p;
	double d,ts,q;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&tcn);
	for(tc=1;tc<=tcn;tc++){
		scanf("%d%lf%lf",&n,&v,&x);
		for(i=0;i<n;i++){
			scanf("%lf%lf",&r[i],&c[i]);
		}
		printf("Case #%d: ",tc);
		for(i=0;i<n;i++){
			if(x<c[i]||same(x,c[i]))break;
		}
		if(i==n){
			printf("IMPOSSIBLE\n");
			continue;
		}
		for(i=0;i<n;i++){
			if(x>c[i]||same(x,c[i]))break;
		}
		if(i==n){
			printf("IMPOSSIBLE\n");
			continue;
		}
		for(i=0;i<n;i++){
			chk[i]=0;
		}
		while(1){
			d=0;
			for(i=0;i<n;i++){
				if(chk[i]==1)continue;
				if(!same(c[i],x))break;
				d+=r[i];
			}
			if(i==n){
				printf("%.9lf\n",v/d);
				break;
			}
			d=0;
			ts=0;
			for(i=0;i<n;i++){
				if(chk[i]==1)continue;
				d+=r[i];
				ts+=r[i]*c[i];
			}
			if(ts/d>x){
				p=-1;
				for(i=0;i<n;i++){
					if(chk[i]==1)continue;
					if(p==-1||c[i]>c[p])p=i;
				}
				chk[p]=1;
				q=(ts-d*x)/(c[p]-x);
				if(q>r[p])continue;
				ts-=c[p]*q;
				d-=q;
				printf("%.9lf\n",v/d);
				break;
			}
			else{
				p=-1;
				for(i=0;i<n;i++){
					if(chk[i]==1)continue;
					if(p==-1||c[i]<c[p])p=i;
				}
				chk[p]=1;
				q=(ts-d*x)/(c[p]-x);
				if(q>r[p])continue;
				ts-=c[p]*q;
				d-=q;
				printf("%.9lf\n",v/d);
				break;
			}
		}
	}
}
