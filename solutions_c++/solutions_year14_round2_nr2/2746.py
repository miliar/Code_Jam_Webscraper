#include <iostream>
#include <fstream>

int main(int argc, char * argv[]){
    if (argc != 2){
        return 1;
    }

    std::ifstream in(argv[1]);
    if (!in){
        return 2;
    }

    std::ofstream out("out");

    int N; in >> N;
    for(int i = 0; i < N; i++){
        int A, B, K; in >> A >> B >> K;

        int c = 0;
        for(int i = 0; i < A; i++){
            for(int j = 0; j < B; j++){
                if ((i & j) < K){
                    c++;
                }
            }
        }

        out << "Case #" << i + 1 << ": " << c << std::endl;
    }

    return 0;
}
