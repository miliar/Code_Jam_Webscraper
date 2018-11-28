#include <iostream>
#include <stdlib.h>

int main(){
int unsigned tCase = 0, quantity = 0;
int long long unsigned total = 0, minimum = 0;
char allah[1200];
char caseT;

std::cin >> tCase;

    for(int i = 0; i < tCase; i++){
    total = 0;
    minimum = 0;

    std::cin >> quantity >> allah;

        for(int i = 0; i <= quantity; i++){
            if(total < i){
            minimum += i - total;
            total = i;
            }
        caseT = allah[i];
        total += atoi(&caseT);
        }

    std::cout << "Case #" << i + 1 << ": "<< minimum << std::endl;
    }
return 0;
}
