#include <stdio.h>
#include <set>
#include <algorithm>
    
using namespace std;
int T;
int N;
int current = 0;
void run(){
    int in = 0;
    set<int> S;
    scanf(" %d", &N);
    for(int i = 0; i < 2*N - 1; i++){
        for(int j = 0; j < N; j++){
            scanf(" %d", &in);
            set<int>::iterator it = S.find(in);
            if(it != S.end()){
                S.erase(it);
            }else{
                S.insert(in);
            }
        }
    }
    for(set<int>::iterator it = S.begin(); it != S.end(); it++){
        printf("%d ", *it);
    }
    printf("\n");

}
int main(){
    scanf(" %d", &T);
    for(int i = 1; i <= T; i++){
        printf("Case #%d: ", i);
        run();
    }
}
