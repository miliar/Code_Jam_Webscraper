#include <string>
#include <iostream>
#include <vector>


inline char 
flip(char c)
{
    return c == '-' ? '+' : '-';
}

int
calculate(const std::string& s)
{
    int counter = 0;
    char current = s[0];
    char toSearch = flip(current);
    size_t nextPos = s.find(toSearch);
    
    while (nextPos != std::string::npos) {
        // we found the one we are looking for, we flip all others
        counter++;
        // now we start searching from this position the other one
        current = toSearch;
        toSearch = flip(current);
        nextPos = s.find(toSearch, nextPos);        
    }
    
    if (current == '-') {
        // last flip
        counter++;
    }
    return counter;
}


int main(void)
{
    int T;
    std::cin >> T;
    for (int i = 0; i < T; ++i) {
        std::string caseStr;
        std::cin >> caseStr;
        const int numFlips = calculate(caseStr);
        std::cout << "Case #" << (i+1) << ": " << numFlips << "\n";
    }

    return 0;
}
