#include <iostream>
#include <string>
#include <cmath>
#include <fstream>
#include <vector>

using namespace std;

string get_next_possible_coinjam(string &coinjam){
    for(int i = coinjam.length()-2; i > 0; --i){
        if(coinjam[i] == '0'){
            coinjam[i] = '1';
            return coinjam;
        } else {
            coinjam[i] = '0';
        }
    }

    coinjam = "end";
    return coinjam;
}

bool is_prime(long long num, long long *divisor = NULL){
    double raiz = sqrt(num);
    for(int i = 2; i <= raiz; ++i){
        if(num % i == 0){
            if(divisor != NULL){
                *divisor = i;
            }
            return false;
        }
    }
    return true;
}

string generate_starting_posible_coinjam(int digitos){
    string coinjam = "1";
    for(int i = 0; i < digitos-2; ++i){
        coinjam.append("0");
    }
    coinjam.append("1");
    return coinjam;
}

int main()
{
    ofstream output;
    output.open("output.txt", ofstream::out);
    output << "Case #1:" << endl;

    string posible = generate_starting_posible_coinjam(16);

    int coinjams_pedidos = 50;
    int cant_coinjams = 0;

    while(cant_coinjams < coinjams_pedidos){
        bool coinjam = true;
        vector<long long> divisores;
        long long divisor;
        for(int base = 2; base <= 10; ++base){
            long long num = std::stoll(posible, nullptr, base);
            if(is_prime(num, &divisor)){
                coinjam = false;
                break;
            } else {
                divisores.push_back(divisor);
            }
        }
        if(coinjam){
            output << posible << " ";
            for(unsigned int i = 0; i < divisores.size(); ++i){
                output << divisores[i] << " ";
            }
            output << endl;
            ++cant_coinjams;
        }
        get_next_possible_coinjam(posible);
    }

    return 0;
}
