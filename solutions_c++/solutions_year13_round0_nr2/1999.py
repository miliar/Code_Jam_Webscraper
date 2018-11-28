#include <stdio.h>
#include <algorithm>
#define max(x,y) x>y?x:y
#define min(x,y) x<y?x:y
#define INFINITO 1<<30


int m,n;
int r;

struct Square{
	Square(){}
	Square(int a,int b, int c):i(a),j(b),size(c){}
	int i,j,size;
};

bool operator <(const Square& a,const Square& b){
	if(a.size==b.size){
		if(a.i==b.i){
			return a.j<b.j;
		}
		return a.i<b.i;
	}
	return a.size<b.size;
} 
int at;
int maximoL[1000],maximoC[1000];
Square quadrados[1000000];


bool possivel(){
	for(int k=0;k<at;k++){
		int i=quadrados[k].i;
		int j=quadrados[k].j;
		int l=quadrados[k].size;
		//printf("%d %d %d\n",i,j,l);
		if(maximoL[i]>l && maximoC[j]>l){
			return false;
		}

	}
	return true;
}

int main(){
	int t;
	scanf("%d",&t);
	for(int xxx=0;xxx<t;xxx++){
		scanf("%d %d",&n,&m);
		at=0;
		for(int i=0;i<n;i++){
			maximoL[i]=0;
		}
		for(int i=0;i<m;i++){
			maximoC[i]=0;
		}
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				scanf("%d",&r);
				quadrados[at++]=Square(i,j,r);
				maximoL[i]=max(maximoL[i],r);
				maximoC[j]=max(maximoC[j],r);
			}
		}

/*		for(int i=0;i<n;i++){
			printf("%d\n",maximoL[i]);
		}
		puts("");
		for(int i=0;i<m;i++){
			printf("%d\n",maximoC[i]);
		}
*/
		std::sort(quadrados,quadrados+at);
		if(possivel()){
			printf("Case #%d: YES\n",xxx+1);
		}
		else{
			printf("Case #%d: NO\n",xxx+1);
		}






	}


}

