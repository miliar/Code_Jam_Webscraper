#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <set>
#include <fstream>

int flip(std::string s){
    int count = 0;
    while(s.find("-") != std::string::npos){
        int first = s.find("+");
        if(first == std::string::npos) first = s.size();
        if(first == 0) first = s.find("-");

        for(int i = 0; i < first; ++i){
           s[i] = (s[i] == '+' ? '-' : '+'); 
        }
        ++count;
    }
    return count;
}

int main(){
    std::ifstream in("input.txt");
    std::string s;
    std::ofstream out("out.txt");
    in >> s;
    int n = std::stoi(s);
    for(int i = 1; i <= n; ++i){
        in >> s;
        out << "Case #" << i << ": " << flip(s) << std::endl;
    }
    return 0;
}
