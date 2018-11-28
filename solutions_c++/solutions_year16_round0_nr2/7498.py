#include <iostream>
#include <stack>
#include <vector>


bool areHappy(std::stack<char> pancakes){
    while (!pancakes.empty()){
        if(pancakes.top()=='-')
            return false;
        else
            pancakes.pop();
    }
    return true;
}

int makeHappy(std::stack<char> pancakes){
    
    char p;
    int flips = 0;
    
    while (!pancakes.empty()){
        
        if(areHappy(pancakes))
            return flips;
        
        int toBeFlipped = 0;
        p = pancakes.top();
        
        if(p=='-'){ // pick top i blank pancakes and make them happy
            toBeFlipped++;
            pancakes.pop();
            while(!pancakes.empty() && pancakes.top()=='-'){
                toBeFlipped++;
                pancakes.pop();
            }
            // now we have top blank pancakes from stack, flip!
            flips++;
            while(--toBeFlipped)
                pancakes.push('+');
        }
        else{ // pick top i happy pancakes and make them sad, we'll make them happy with others
            toBeFlipped++; 
            pancakes.pop();
            while(!pancakes.empty() && pancakes.top()=='+'){
                toBeFlipped++;
                pancakes.pop();
            }
            // now we have top happy pancakes from stack, flip!
            flips++;
            while(--toBeFlipped)
                pancakes.push('-');
        }
    }
    return flips;
}

void printMinExec(std::string s){
    std::stack<char> pancakes;
    for(int i=s.length()-1;i>-1;i--)
        pancakes.push(s[i]);
    std::cout<<makeHappy(pancakes);
}

int main(){
    int T,I=0;
    std::string s;
    std::cin >> T;
    while(I++ != T){
        std::cin >> s;
        std::cout <<"Case #"<<I<<":  ";
        printMinExec(s);
        std::cout<<std::endl;
    }
}