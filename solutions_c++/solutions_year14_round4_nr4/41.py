#include<bits/stdc++.h>
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
#define make(A) scanf("%d",&A)
#define ALFA 'z'-'a'+1
#define MAX 101
const int P = 1000 * 1000 * 1000 +7;
int n,m;
int ma;
LL sil[MAX*2],odw[MAX*2];
LL pot(LL a,int w){
	LL r=1;
	while(w){
		if(w&1){
			r*=a;
			r%=P;
		}
		w/=2;
		a*=a;
		a%=P;
	}
	return r;
}
void pre(){
	sil[0] = 1;
	F(i,1,MAX*2)
		sil[i] = sil[i-1] * i % P;
	R(i,MAX*2)
	 odw[i] = pot(sil[i],P-2);
	/*R(i,6){
		printf("%lld %lld\n",sil[i],odw[i]);
	}*/
}
LL z(LL a,LL b){
	if(b>a || b<0)return 0;
	return sil[a] * odw[a-b] %P * odw[b] %P;
}
struct w{
	w* t[ALFA];
	bool cz;
	w(){
		cz = 0;
		for(int i=0;i<ALFA;i++)
			t[i]=0;
	}
	~w(){
		for(int i=0;i<ALFA;i++)
			if(t[i]!=0)
				delete t[i];
	}
};
void dod(w* &a,char* s){
	if(a == 0){
		a = new w();
	}
	if(*s == 0){
		a->cz = 1;
		return;
	}
	dod(a->t[*s-'A'],s+1);
}
LL wyn;
LL licz(vector<int>& j,int k){
	//printf("licz %d =",k);
	LL ret = 1;
	R(i,j.size()){
		ret *= z(k,j[i]);
		ret %= P;
	}
	//printf("%lld\n",ret);
	return ret;
}
int dfs(w* a){
	int sum=a->cz;
	vector<int> j;
	if(a->cz)j.PB(1);
	bool cz1 = 0;
	R(i,ALFA){
		if(a->t[i]!=0){
			int pom = dfs(a->t[i]);
			if(pom == -1)cz1 = 1;
			sum += pom;
			j.PB(pom);
		}
	}
	if(cz1){
		ma += n;
		R(i,j.size()){
			if(j[i]!=-1){
				wyn *= z(n,j[i]);
				wyn%=P;
				wyn *= sil[j[i]];
				wyn%=P;
			}
		}
		
		return -1;
	}else{
		if(sum < n){
			ma += sum;
			return sum;
		}
		ma += min(sum,n);
		int znak = 1;
		/*printf("n= %d\n",n);
		R(i,j.size()){
			printf("%d ",j[i]);
		}
		puts("");*/
		LL ak = 0;
		FD(i,n+1){
			ak += znak * z(n,i) * licz(j,i)%P;
			ak %= P;
			znak*=-1;
		}
	//	printf("%lld\n",ak);
		wyn *= ak;
		wyn%=P;
		R(i,j.size()){
			wyn *= sil[j[i]];
			wyn%=P;
		}
		return -1;
	}
}
char s[101];
void test(){
	make(m);make(n);
	w* korz = 0;
	R(i,m){
		scanf(" %s",s);
		dod(korz,s);
	}
	ma = 0;wyn = 1;
	int pom = dfs(korz);
	
	if(pom!=-1){
		wyn *= z(n,pom);
		wyn %= P;
		wyn *= sil[pom];
		wyn %= P;
	}
	static int test_nr = 0;test_nr++;
	printf("Case #%d: ",test_nr);
	printf("%d %lld\n",ma,(wyn+P)%P);
	delete korz;
}
main(){
	pre();
	int _;make(_);
	//_=5;
	while(_--)test();
}
