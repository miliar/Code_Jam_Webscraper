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
#define MAX 4000 // sprawdzic dla n= MAX
int n,x,y;
D s[MAX][MAX];
D test(){
	make(n);
	make(x);if(x<0)x*=-1;
	make(y);
	int w=0,dod=1;
	while(n>=dod){
		w++;
		n-=dod;
		dod+=4;
	}
	
	//printf("%d\n",w);
	if(w>(x+y)/2)return 1.;
	if(w<(x+y)/2)return 0.;
	s[0][0]=1;
	w=dod;
	//printf("%d\n",w);
	F(i,1,n+1){
		D sum=0.;
		R(j,i+1){
			s[i][j]=0;
			if(j>w/2 || i-j > w/2)continue;
			
			if(j!=0)
			if(i-j == w/2)
				s[i][j] += s[i-1][j-1];
			else
				s[i][j] += s[i-1][j-1]/2;
			
			if(i!=j)
			if(j == w/2)
				s[i][j] += s[i-1][j];
			else
				s[i][j] += s[i-1][j]/2;
		//	printf("%d %d %lf\n",i,j,s[i][j]);
			sum+=s[i][j];
		}
	//	printf("sum:  %lf\n",sum);
		
	}
	
	D wyn=0.;
	F(i,y+1,w/2+1)
		wyn+=s[n][i];
	return wyn; 
}
main(){
	int _;
	make(_);
	R(i,_)printf("Case #%d: %.8f\n",i+1,test());
}
