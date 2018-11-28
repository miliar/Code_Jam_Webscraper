#include <iostream>
#include <sstream>
#include <string>
#include <fstream>
#include <set>

int count(int n){
    if(n == 0) return -1;
    std::set<int> found;
    int i = 0;
    while(found.size() < 10){
        ++i;
        int x = i * n;
        while(x >= 10){
            if(found.find(x%10)== found.end()) found.insert(x%10);
            x /= 10;
        }
        if(found.find(x%10)== found.end()) found.insert(x%10);
    }
    return i*n;
}
int main(){
    std::ifstream in("input.txt");
    std::string s;
    std::ofstream out("out.txt");
    in >> s;
    int n = std::stoi(s);
    for(int i = 0; i < n; ++i){
        in >> s;
        int x = count(std::stoi(s)); 
        out << "Case #" << i+1 << ": " << (x == -1 ? "INSOMNIA" : std::to_string(x))  << std::endl;
    }
    return 0;
}
