#include<iostream>
#include<cstdio>
#include<cstring>
#include<map>

const int N = 4;

using namespace std;

int s;
int table[N+2][N+2];

int main(){
    
    int T; scanf( "%d", &T );
    
    for(int t=1;t<=T;t++){
            
            map<int,int> Q;
            int ans = 0, counter = 0;
            
            scanf( "%d", &s );
            for(int i=1;i<=N;i++)
                    for(int j=1;j<=N;j++)
                            scanf( "%d", &table[i][j] );
            for(int i=1;i<=N;i++){
                    int pos = table[s][i];
                    Q[pos]++;
                    }
            
            scanf( "%d", &s );
            for(int i=1;i<=N;i++)
                    for(int j=1;j<=N;j++)
                            scanf( "%d", &table[i][j] );
            for(int i=1;i<=N;i++){
                    int pos = table[s][i];
                    Q[pos]++;
                    if( Q[pos] == 2 ){
                        counter++;
                        ans = pos;
                        }
                    }
            
            if( counter == 1 )
                printf( "Case #%d: %d\n", t, ans );
            else if( counter > 1 )
                 printf( "Case #%d: Bad magician!\n", t );
            else
                printf( "Case #%d: Volunteer cheated!\n", t );
                }
    
    return 0;
}
