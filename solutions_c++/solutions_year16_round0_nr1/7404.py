#include <iostream>
#include <set>

int addSeen(int N,std::set<int>& seen){
    int digit,copy=N;
    while(N){
        digit = N % 10;
        N /= 10;
        seen.insert(digit);
    }
    return copy;
}

void printLastNumber(int N){
    std::set<int> seen;
    int last,i=0;
    if(N==0){
        std::cout<<"INSOMNIA";
        return;
    }
    while(seen.size()!=10)
        last = addSeen(++i*N,seen);
    std::cout<<last;
}

int main(){
    int T,N,I=0;
    std::cin >> T;
    while(I++ != T){
        std::cin >> N;
        std::cout <<"Case #"<<I<<":  ";
        printLastNumber(N);
        std::cout<<std::endl;
    }
}