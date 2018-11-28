#include <iostream>
#include <stdlib.h>
#include <vector>
#include <algorithm>

void solve(){
    int N;
    int heights[2501];
    std::fill_n(heights,2501,0);
    std::cin >> N;
    for(int i=0;i<2*N-1;i++){
        for(int j=0;j<N;j++){
            int d;
            std::cin >> d;
            heights[d]++;
        }
    }
    for(int i=1;i<2500;i++){
        if(heights[i]%2) printf(" %d",i);
    }
    printf("\n");
}

int main(){
    int T;
    std::cin >> T;
    for(int i=1;i<=T;i++){
        printf("Case #%d:",i);
        solve();
    }
}