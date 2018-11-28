#include <iostream>
#include <stdio.h>
using namespace std;

int solve() {
    int max_shyness = 0;
    std::cin>>max_shyness;
    int members = 0;
    int added = 0;
    std::string s;
    std::cin>>s;
    for(int i = 0; i<=max_shyness; i++) {
        if(members < i) {
            added++;
            members++;
        }
        members += (s[i]-'0');
    }
    return added;
}

int main() {

    int cases = 0;
    std::cin>>cases;
    for(int i = 0; i < cases; i++) {
        std::cout<<"Case #"<<i+1<<": "<<solve()<<endl;
    }
    return 0;
}
