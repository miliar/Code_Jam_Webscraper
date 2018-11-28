#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<queue>
#include<stack>
#include<cmath>
using namespace std;
typedef pair<int,int> PI;
typedef long long LL;
typedef double D;
#define FI first
#define SE second
#define MP make_pair
#define PB push_back
#define R(I,N) for(int I=0;I<N;I++)
#define F(I,A,B) for(int I=A;I<B;I++)
#define FD(I,N) for(int I=N-1;I>=0;I--)
#define make(A) scanf("%d",&A);
#define MAX 1001
#define INF 1000000001
int n,m,p,odl[MAX],t[MAX][MAX],pop[MAX],popk[MAX],lim[MAX];
vector<int> d[MAX];
struct kra{
	int k,m,d;
//	int wyb;
}k[MAX];
//int iwyb;
priority_queue<PI> kol;
bool D1(int po,int odd){
	R(i,n)odl[i]=lim[i]+1;
	odl[po]=odd;
	while(!kol.empty())kol.pop();
	kol.push(MP(odd,po));
	while(!kol.empty()){
		PI ak = kol.top();
		kol.pop();
		if(ak.FI != odl[ak.SE])continue;
		if(ak.SE == 1){
	/*		int pom = ak.SE ;
			while(pom != 0){
				k[popk[pom]].wyb = iwyb;
				pom = pop[pom];
			}*/
		//	printf("odl = %d\n",ak.FI);
			return 1;
		}
		R(i,d[ak.SE].size()){
			int pom = d[ak.SE][i];
			int od = ak.FI + k[pom].m;
			if( odl[k[pom].k] > od ){
				odl[k[pom].k] = od;
	//			pop[k[pom].k] = ak.SE;
	//			popk[k[pom].k] = pom;
				kol.push(MP(od,k[pom].k));
			}
		}
	}
	return 0;
}
int pp[MAX];
void test(){
	make(n);make(m);make(p);
//	iwyb=0;
	R(i,n)R(j,n)if(i!=j)t[i][j]=INF;
	//printf("%d %d\n",INF, INF+INF);
	R(i,m){
		int a,b	;
		scanf("%d%d%d%d",&a,&b,&k[i].m,&k[i].d);
		a--;b--;
		if(k[i].d< t[a][b])
		t[a][b]=k[i].d;
		k[i].k = b;
//		k[i].wyb = 0;
		d[a].PB(i);
	}
	R(i,n)R(j,n)R(k,n)
		if(t[j][k] > t[j][i] + t[i][k] )
			t[j][k] = t[j][i] + t[i][k];
	R(i,n)lim[i] = t[0][i];
	//R(i,n)printf("%d ",lim[i]);
	//printf("\n");
	int ak = 0,od = 0;
	R(i,p){make(pp[i]);pp[i]--;}
	R(i,p){
		int pom=pp[i];
		//k[pom].wyb = INF;
		od += k[pom].m;
		//iwyb ++;
		ak = k[pom].k;
		//printf(" %d %d %d\n",ak,lim[ak],od);
		if(lim[ak]<od || D1(ak,od) == 0){
			printf("%d\n",pom+1);
			return;
		}
		R(i,n){
			if (lim[i] > od + t[ak][i])
				lim[i] = od + t[ak][i];
		}
	}
	printf("Looks Good To Me\n");
}
main(){
	int _;
	make(_);
	R(i,_){
		printf("Case #%d: ",i+1);
		test();
	}
}