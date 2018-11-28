#include <iostream>
using namespace std;

#define fori(a,b) for(a=0;(a)<(b);a++)
int N,M;

int val[100][100];
int maxH[100];
int maxV[100];

bool isPossible() {
    int i,j;
    
    fori(i,N){
        fori(j,M) {
            if( val[i][j] < maxH[i] ){
                if( val[i][j] < maxV[j] )
                    return false;
            }
        }
    }
    return true;
        
}

int main() {
    int i,j,t,T;
    
    cin>>T;
    fori(t,T){
        cin>>N>>M;
        fori(i,N) fori(j,M) cin>>val[i][j];
        
        fori(i,N){
            maxH[i] = val[i][0];
            for(j=1; j<M; j++ ) {
                if( val[i][j] > maxH[i] )
                    maxH[i] = val[i][j];
            }
        }
        fori(j,M){
            maxV[j] = val[0][j];
            for (i=1; i<N; i++) {
                if( val[i][j] > maxV[j] )
                    maxV[j] = val[i][j];   
            }
        }
        
        if( isPossible() )
            cout<<"Case #"<<t+1<<": YES"<<endl;
        else
            cout<<"Case #"<<t+1<<": NO"<<endl;
    }
    
    return 0;
}
