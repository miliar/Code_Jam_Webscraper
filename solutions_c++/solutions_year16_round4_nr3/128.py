#include<stdio.h>
#include<algorithm>
using namespace std;
int UF[1100];
int FIND(int a){
	if(UF[a]<0)return a;
	return UF[a]=FIND(UF[a]);
}
void UNION(int a,int b){
	a=FIND(a);b=FIND(b);if(a==b)return;UF[a]+=UF[b];UF[b]=a;
}
int p[1100];
int num[110][110];
int main(){
	int T;scanf("%d",&T);
	for(int t=1;t<=T;t++){
		int a,b;scanf("%d%d",&a,&b);
		for(int i=0;i<1100;i++)UF[i]=-1;
		for(int i=0;i<2*(a+b);i++){
			scanf("%d",p+i);
			p[i]--;
		}
		int w=b*2+1;
		bool flag=false;
		printf("Case #%d:\n",t);
		for(int i=0;i<(1<<(a*b));i++){
			for(int j=0;j<1100;j++)UF[j]=-1;
			for(int j=0;j<a*b;j++){
				int row=j/b;
				int col=j%b;
				if(i&(1<<j)){
					UNION(row*2*w+col*2+1,row*2*w+w+col*2+2);
					UNION(row*2*w+w+col*2,row*2*w+w*2+col*2+1);
				}else{
					UNION(row*2*w+col*2+1,row*2*w+w+col*2);
					UNION(row*2*w+w+col*2+2,row*2*w+w*2+col*2+1);
				}
			}
			for(int j=0;j<a*2+1;j++){
			//	for(int k=0;k<b*2+1;k++)printf("%d ",FIND(j*w+k));
			//	printf("\n");
			}
			bool ok=true;
			for(int j=0;j<2*(a+b);j++){
				for(int k=0;k<2*(a+b);k++){
					int r1,r2,c1,c2;
					if(p[j]<b){r1=0;c1=p[j]*2+1;}
					else if(p[j]<a+b){r1=(p[j]-b)*2+1;c1=b*2;}
					else if(p[j]<a+b+b){r1=a*2;c1=(b-1-(p[j]-a-b))*2+1;}
					else{r1=(a-1-(p[j]-a-b-b))*2+1;c1=0;}
					
					if(p[k]<b){r2=0;c2=p[k]*2+1;}
					else if(p[k]<a+b){r2=(p[k]-b)*2+1;c2=b*2;}
					else if(p[k]<a+b+b){r2=a*2;c2=(b-1-(p[k]-a-b))*2+1;}
					else{r2=(a-1-(p[k]-a-b-b))*2+1;c2=0;}
				
				
					if(j/2==k/2){
			//		printf("%d %d %d %d: %d %d\n",r1,c1,r2,c2,FIND(r1*w+c1),FIND(r2*w+c2));
						if(FIND(r1*w+c1)!=FIND(r2*w+c2))ok=false;
					}else{
						if(FIND(r1*w+c1)==FIND(r2*w+c2))ok=false;
					}
				}
			}
			if(ok){
				for(int j=0;j<a;j++){
					for(int k=0;k<b;k++){
						if(i&(1<<(j*b+k)))printf("\\");
						else printf("/");
					}
					printf("\n");
				}
				flag=true;
				break;
			}
		}
		if(!flag){
			printf("IMPOSSIBLE\n");
		}
	}
}