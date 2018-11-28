
#include <cstdio>
#include <cstring>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <iostream>

using namespace std ; 

int con[22][1111] ;
int cp[22] ;

char ise[3333] ;
char isf[3333] ; 

int minv(int i1, int i2){
    return i1 < i2 ? i1 : i2 ; 
}

int main()
{
    int T ;
    scanf("%d", &T) ; 
    for(int time = 1 ; time <= T ; time++){
        printf("Case #%d: ", time) ; 
        int N ;
        scanf("%d", &N) ; 
        fprintf(stderr, "solving case %d, size %d\n", time, N) ; 
        getchar() ;
        int cnt = 0 ;
        map<string, int> M ;
        for(int i = 0 ; i != N ; i++){
            cp[i] = 0 ; 
            string line ;
            getline(cin, line) ; 
            istringstream in(line) ; 
            string str ;
            while(in >> str){
                auto it = M.find(str) ; 
                if(it == M.end()){
                    M[str] = cnt ;
                    con[i][cp[i]++] = cnt ;
                    cnt++ ;
                }
                else{
                    con[i][cp[i]++] = it->second ; 
                }
            }
        }   
        int wc = M.size() ; 
        int ts = N-2 ; 
        int ans = 999999999 ;
        for(int s = 0 ; s != (1<<ts) ; s++){
            memset(ise, 0, sizeof(ise)) ;
            memset(isf, 0, sizeof(isf)) ; 
            for(int i = 0 ; i != cp[0] ; i++){
                ise[con[0][i]] = true ; 
            }
            for(int i = 0 ; i != cp[1] ; i++){
                isf[con[1][i]] = true ;
            }
            for(int i = 0 ; i != ts ; i++){
                if((s>>i)&1){
                    for(int j = 0 ; j != cp[i+2] ; j++)
                        isf[con[i+2][j]] = true ;
                }
                else{
                    for(int j = 0 ; j != cp[i+2] ; j++)
                        ise[con[i+2][j]] = true ;
                }
            }
            int now = 0 ; 
            for(int i = 0 ; i != wc ; i++){
                if(isf[i] && ise[i])
                    now++ ;
            }
            ans = minv(ans, now) ;
        }
        printf("%d\n", ans) ; 
    }
    return 0 ; 
}
