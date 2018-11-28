#include<iostream>
#include<fstream>
#include<algorithm>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<list>
#include<cstdio>
#include<cstring>
#include<string>
#include<cmath>
#include<cstdlib>
#include<vector>
#include<climits>
#include<ctime>
#include<sstream>
#define mp       	make_pair
#define pb       	push_back
#define st       	first
#define nd       	second
#define wait     	getchar();getchar();
#define lint     	long long
#define KARE(a)	 	( (a)*(a) )
#define MAX(a,b) 	( (a)>(b) ? (a) : (b) )
#define MIN(a,b) 	( (a)<(b) ? (a) : (b) )
#define MAX3(a,b,c)	( MAX( a,MAX(b,c) ) )
#define MIN3(a,b,c)	( MIN( a,MIN(b,c) ) )
#define FILL(ar,a)	memset( ar,a,sizeof ar )
#define oo	 		1e9
#define pii       	pair<int,int>
#define pll			pair<lint,lint>
#define pdd			pair<double,double>
#define y1			yy1
#define eps      	(1e-9)
#define esit(a,b)  	( abs( (a)-(b) ) < eps )
#define sol(a)		( (a)<<1 )
#define sag(a)		( sol(a)|1 )
#define orta(a,b)	( ( (a)+(b) )>>1 )
#define mxn       	1005
using namespace std;

lint test,n;


void solve(){

    int ar[10];
    lint N,k;

    cin>>test;

    for(lint i=1;i<=test;i++){

        cin>>n;

        if(n==0){
            printf("Case #%lld: INSOMNIA\n",i);
            continue;
        }

        memset(ar,0,sizeof ar);
        N = n;

        while(1){

            lint t = N;

            while(t){
                ar[t%10] = 1;
                t /= 10;
            }

            for(k=0;k<10;k++)
                if(ar[k]==0)
                    break;

            if(k==10)
                break;

            N += n;

        }

        printf("Case #%lld: %lld\n",i,N);

    }

}

int main(){

    freopen( "A-large.in" , "r" , stdin );
    freopen( "output.out" , "w" , stdout );

	solve();
	return 0;
}
