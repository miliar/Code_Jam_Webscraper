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
#define M 1000002013
int n,m;
struct q{
	int g;
	int il;
}t[MAX*2];
bool qq(q a, q b){
	if(a.g!=b.g)
		return a.g<b.g;
	return a.il>b.il;
}
LL kosz(int dl){
	//printf("kosz %d\n",dl);
	return LL(dl)*(dl+1)/2 % M;
}
stack<PI > st;
LL wyn;
int licz(){
	wyn=0;
	make(n);make(m);
	R(i,m){
		int a,b,il;
		make(a);
		make(b);
		make(il);
		t[i*2].g=a;
		t[i*2].il=il;
		t[i*2+1].g=b;
		t[i*2+1].il=-il;
		wyn+= il * kosz(b-a);
		//printf("%lld\n",wyn);
		wyn%=M;
	}
	sort(t,t+2*m,qq);
	R(i,2*m){
		if(t[i].il>=0){
			st.push(MP(t[i].g,t[i].il));
		}else{
			t[i].il*=-1;
			while(t[i].il!=0){
				int pom = min(t[i].il,st.top().SE);
				//printf("%d\n",pom);
				wyn -= pom * kosz(t[i].g - st.top().FI);
				wyn %= M;
				t[i].il -= pom;
				st.top().SE -= pom;
				if(st.top().SE==0)st.pop();
			}
		}
	}
	wyn*=-1;
	if(wyn<0)wyn+=M;
	return int(wyn);
}
main(){
	int _;
	make(_);
	R(t,_){
		printf("Case #%d: %d\n",t+1,licz());
	}
}