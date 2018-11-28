#include<iostream>
#include<bitset>
#include<cmath>
#include<string>
#include<deque>


std::deque<bool> parse(std::string input){
    std::deque<bool> res;
    for(char c : input){
        if(c=='+'){
            res.push_front(true);
        }else{
            res.push_front(false);
        }
    }
    return res;
}

void test(std::string input){
    auto data = parse(input);
    bool youjo = false;
    long count = 0;
    for(auto curr : data){
        if(curr == youjo){
            count += 1;
            youjo = !youjo;
        }
    }
    std::cout<<count;
}


int main(){
    int test_limit = 0;
    std::cin >> test_limit;
    for(int i=0;i<test_limit;++i){
        std::string input;
        std::cin >> input;
        std::cout << "Case #" << i + 1 << ": ";
        test(input);
        std::cout << std::endl;
    }
}
