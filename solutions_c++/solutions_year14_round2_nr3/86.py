#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<queue>
#include<stack>
#include<cmath>
#include<map>
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
#define MAX 55
int n,m;
int nr[MAX];
bool t[MAX][MAX];
bool odw[MAX];
int ak[MAX];
vector<int> dos[MAX];
int mi;
void clr(){
	R(i,n){
		R(j,n)t[i][j] = 0;
		odw[i] = 0;
		ak[i] = 0;
		dos[i].clear();
	}
}

int f[MAX],naj[MAX];
int find(int nr){
	return f[nr]==nr?nr:f[nr]=find(f[nr]);
}
void Unoin(int a,int b){
	a = find(a);
	b = find(b);
	f[a] = b;
}
int ssdop(){
	R(i,n){
		f[i] = i;
		naj[i] = 1000;
	}
	
	R(i,n)R(j,n){
		if(!odw[i] && !odw[j] && t[i][j])
			Unoin(i,j);
	}
	
	R(i,n)R(j,n){
		if(!odw[i] && ak[j] && t[i][j]){
			naj[find(i)] = min(naj[find(i)],ak[j]);
		}
	}
	
	int ma = -1;
	R(i,n){
		if(f[i] == i && !odw[i]){
		//	printf("tu %d %d\n",i,naj[i]);
			ma = max(ma, naj[i]);
		}
	}
	return ma;
}

void dfs(int w,int gl){
	odw[w] = 1;
	ak[w] = gl;
	//printf("dfs %d\n",w);
	
	printf("%d",nr[w]);
	R(j,n)if(t[w][j])dos[j].PB(gl);
	
	mi = -1;
	int pom = ssdop();
	//printf("(%d) %d %d\n",pom,dos[1].size(),dos[1].back());
	R(i,n)if( !odw[i] && dos[i].size()>0 && dos[i].back() >= pom && ( mi == -1 || nr[mi] > nr[i])) mi = i;
	
	if(mi!=-1)while(t[w][mi])dfs(mi,gl+1);
	
	ak[w] = 0;
	R(j,n)if(t[w][j])dos[j].pop_back();
}
void test(){
	static int test_nr = 0;test_nr++;
	printf("Case #%d: ",test_nr);
	make(n);make(m);clr();
	R(i,n)make(nr[i]);
	R(i,m){
		int a,b;
		make(a);make(b);
		a--;b--;
		t[a][b] = 1;
		t[b][a] = 1;
	}
	
	int mi = 0;
	R(i,n)if(nr[mi] > nr[i])mi = i;
	dfs(mi,1);
	puts("");
}
main(){
	int _;make(_);while(_--)test();
}
