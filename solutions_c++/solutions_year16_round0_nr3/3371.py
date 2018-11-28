#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <set>
#include <fstream>
#include <bitset>
#include <cmath>

long long first_div(long long x){
    for(int i = 2; i < sqrt(x); ++i) if(!(x%i)) return i;
    return -1;
}
int main(){
    std::ifstream in("input.txt");
    std::string s;
    std::ofstream out("out.txt");
    in >> s;
    int n = std::stoi(s);
    for(int i = 1; i <= n; ++i){
        int n, j, count = 0;
        in >> n;
        in >> j;
        out << "Case #" << i << ": " << std::endl;
        for(long long x = 0; x < pow(2,n); ++x){
            std::bitset<32> b(x);
            if(b.test(0) && b.test(n-1)){
                std::vector<long long> divisors;
                //std::cout << b.to_string()<<"\n";
                for(int i = 2; i <= 10; ++i)
                {
                    long long p = std::stoll(b.to_string(), 0, i);
                    long long d = first_div(p); 
                    if(d != -1)
                        divisors.push_back(d);
                    else break;
                }
                if(divisors.size() == 9){
                    out << b.to_string().substr(b.to_string().size() - n);
                    for(long long d : divisors)
                        out << " " << d;
                    out << std::endl;
                    ++count;
                    if(count == j) break;
                }
            }
        }
    }
    return 0;
}
