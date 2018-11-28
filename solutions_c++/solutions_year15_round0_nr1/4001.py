#include <iostream>

int main(){
    std::cin.tie(0);
    std::ios::sync_with_stdio(false);
    
    int T;
    std::cin >> T;

    for(int t=1;t<=T;t++){
        int N;
        std::string S;

        std::cin >> N >> S;
        // printf("[%d\n", N);

        for(int i=0;i<=N;i++){
            int sum = i + S[0] - '0';

            int j;
            for(j=1;j<=N;j++){
                if(sum < j){
                    // printf("(%d, %d, %d\n", i, j, sum);
                    break;
                }
                sum += S[j] - '0';
            }

            if(j <= N){continue;}
        
            std::cout << "Case #" << t << ": " << i << std::endl;
            break;
        }
    }
}
