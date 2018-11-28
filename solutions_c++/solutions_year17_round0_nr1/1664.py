#include <iostream>

void flip(char *str, int K){
    for (int i = 0; i < K; i++){
        if (str[i] == '+')
            str[i] = '-';
        else if (str[i] == '-')
            str[i] = '+';
    }
}

int main(){
    std::string S;
    unsigned int K;
    int T;
    int result;

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    std::cin >> T;
    for (int t = 1; t <= T; t++){
        std::cin >> S >> K;
        result = 0;
        for (unsigned int i = 0; i < S.size(); i++){
            if (S[i] == '-'){
                if (i + K > S.size()){
                    result = -1;
                    break;
                }
                flip(&S[i], K);
                result++;
            }
        }
        if (result == -1)
            std::cout << "Case #" << t << ": IMPOSSIBLE" << std::endl;
        else
            std::cout << "Case #" << t << ": " << result << std::endl;
    }
    return 0;
}
