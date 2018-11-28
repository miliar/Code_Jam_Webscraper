#include <map>
#include <string>
#include <cstdio>
#include <cstdlib>

using namespace std;
char st[100][105], pa[10000][105];

int main(void){
    
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int cas, cc=0, N, tol;
    bool go;
    
    scanf("%d", &cas);
    while( cas-- ){
        scanf("%d", &N);
        memset(st, 0, sizeof(st));
        memset(pa, 0, sizeof(pa));
        tol = 0;
        go = true;
        
        for(int i=0; i<N; ++i)
        	scanf("%s", st[i]);
        
        for(int i=0; i<N&&go; ++i) for(int j=i+1; j<N&&go; ++j){
        	
        	int a=0, b=0, index=0;
        	while( a<strlen(st[i]) && b<strlen(st[j]) && go ){
        		if( st[i][a] != st[j][b] ){
        			go = false;
        			break;
        		}
        		
        		char record = st[i][a], t1=0, t2=0;
        		while( st[i][a]==record ){ ++a; ++t1; }
        		while( st[j][b]==record ){ ++b; ++t2; }
        		while( t1>0 && t2>0 ){ pa[tol][index++]=record; --t1; --t2; }
        	}
        	if( a<strlen(st[i]) || b<strlen(st[j])  )	go = false;
        	++tol;
        }
        
        int tmp, ans=1000000000;
        for(int i=0; i<tol; ++i){
        	tmp = 0;
        	for(int j=0; j<N; ++j){
        		
        		int a=0, b=0;
        		while( a<strlen(pa[i]) && b<strlen(st[j]) ){
        			char record = pa[i][a];
					int t1=0, t2=0;
        			while( pa[i][a]==record ){ ++a; ++t1; }
        			while( st[j][b]==record ){ ++b; ++t2; }
        			int t = t1-t2;
        			if( t>0 )	tmp += t;
        			else		tmp -= t;
        		}
        	}
        	if( tmp < ans )	ans = tmp;
        }
        if( !go )	printf("Case #%d: Fegla Won\n", ++cc);
        else		printf("Case #%d: %d\n", ++cc, ans);
        
    }
    
    return 0;
}
