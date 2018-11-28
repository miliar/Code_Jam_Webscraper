#include <bits/stdc++.h>

#define NMAX 201

double prb[NMAX];

void test(int t){
    int N, K;
    
    std::cin >> N >> K;
    
    for(int i=0; i<N; ++i) std::cin >> prb[i];
    
    double ans = 0;
    int MX = (1 << N);
    for(int i=0; i<MX; ++i){
        int cnt = 0;
        std::vector<int> vec;
        for(int j=0; j<N; ++j){
            if(i & (1 << j)){
                ++cnt;
                vec.push_back(j);
            }
        }
        
        if(cnt != K) continue;
        
        double sum = 0;
        int MX2 = (1 << K);
        for(int j=0; j<MX2; ++j){
            double tmp = 1;
            int cnt2 = 0;
            for(int k=0; k<K; ++k){
                if(j & (1 << k)) tmp *= prb[vec[k]], ++cnt2;
                else tmp *= (1-prb[vec[k]]);
            }
         
            if(cnt2 == K/2) sum += tmp;
        }
        
        ans = std::max(ans, sum);
    }
    
    std::cout << "Case #" << t << ": " << ans << std::endl;
}

int main(){
    int T;
    std::cin >> T;
    for(int i=1; i<=T; ++i) test(i);
}
