#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

#define FORIT( it,v ) for( typeof((v).begin()) it=(v).begin(); it!=(v).end(); ++it )

const int max_n2=(1<<21), max_val=205, max_n=25;

struct order{
	int El[max_n], nr_el;
	order(){
		for( int i=0; i<max_n; ++i )
			El[i]=0;
		nr_el=0;
	}
 	bool operator < ( const order other ) const{
		for( int i=0; i<max_n; ++i )
			if( El[i] != other.El[i] )
				return El[i] < other.El[i];
		return 1;
	}
} empty;

bool Viz[max_n2];
int FromSt[max_n2], From, st;
int T, t;
int n, k, i, j, nr;
int x, el, nod;
int Start[max_val], Add[max_n][max_val];
order Ord[max_n2];
int Req[max_n];

vector<int> Rez;

int log( int el ){
	for( int i=0; ; i++ )
		if( el&(1<<i) )
			return i;
}

void make_empty(){
	for( i=0; i<(1<<n); ++i ){
		(Viz[i])=0;
		(FromSt[i])=0;
		Ord[i]=empty;
	}
	for( i=0; i<max_n; ++i ){
		Req[i]=0;
		
		for( j=0; j<max_val; ++j ){
			Add[i][j]=0;
			Start[j]=0;
		}
	}
}

int main(){
	freopen("date.in","r",stdin);
	freopen("date.out","w",stdout);
 	scanf("%d", &T );
	for( t=1; t<=T; ++t ){
		scanf("%d %d", &k, &n );
		make_empty();
 		for( i=1; i<=k; ++i ){
			scanf("%d", &el );
			Start[el]++;
		}
		for( i=0; i<n; ++i ){
			scanf("%d %d", &Req[i], &x );
			while( x-- ){
				scanf("%d", &el );
				Add[i][el]++;
			}
		}
		Viz[0]=1;
 		for( st=1; st<(1<<n); ++st ){
			for( i=0; i<n; ++i )
				if( st&(1<<i) ){
					From = st^(1<<i);
 					if( !Viz[From] )
						continue;
 					nr = Start[ Req[i] ];
					for( j=0; j<n; ++j )
						if( From & ( 1<<j ) ){
							nr += Add[j][ Req[i] ];
							if( Req[i] == Req[j] )
								nr--;
						}
					if( nr>0 ){
						if( Viz[st] ){
							if( Ord[From] < Ord[st] ){
								FromSt[st]=From;
								Ord[st]=Ord[From];
								Ord[st].El[ Ord[st].nr_el ]=i+1;
								Ord[st].nr_el++;
							}
						}else{
							FromSt[st] = From;
							Viz[st] = true;
							Ord[st]=Ord[From];
							Ord[st].El[ Ord[st].nr_el ]=i+1;
							Ord[st].nr_el++;
						}
					}
				}
		}
		if( Viz[(1<<n)-1] ){
			printf("Case #%d:", t);
			for( i=0; i<n; ++i )
				printf(" %d", Ord[(1<<n)-1].El[i]);
			printf("\n");
		}else
			printf("Case #%d: IMPOSSIBLE\n", t);
	}
	return 0;
}
