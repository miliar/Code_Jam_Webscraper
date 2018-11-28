#include <cstdio>
int T,P,Q;
int gcd(int m,int n);
int main(){
	scanf("%d",&T);
	for(int ii=1;ii<=T;ii++){
		scanf("%d%*c%d",&P,&Q);
		int PQ=gcd(P,Q);
		P=P/PQ;
		Q=Q/PQ;
		if( !(Q & (Q-1)) ){
			double i=1,PQw=double(P)/double(Q);
			int j=0;
			while(1){
				i=i/2;
				j++;
				if(PQw>=i){printf("Case #%d: %d\n",ii,j);break;}
			}
		}
		else{
			printf("Case #%d: impossible\n",ii);
		}
	}
	return 0;
}
int gcd( int m, int n ){
	if ( ( 0 == m ) || ( 0 == n ) )return 0;
	while( m != n ){
		if ( m > n ) m = m - n;
		else         n = n - m;
	}
	return m;
}
