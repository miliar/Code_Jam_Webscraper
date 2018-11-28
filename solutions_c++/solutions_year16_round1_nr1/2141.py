#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <deque>

using namespace std;

bool shouldPlaceFront(char letter, const std::deque<char>& word)
{
    for (auto l : word) {
        if (l == letter)
            continue;
        return l < letter;
    }
    
    return false;
}

void solveLoop(std::string letters, std::deque<char>& prevWord)
{
    if (letters.empty())
        return;
    else {
        auto letter = letters[0];
        if (shouldPlaceFront(letter, prevWord)) {
            prevWord.push_front(letter);
        } else {
            prevWord.push_back(letter);
        }
        solveLoop(letters.substr(1), prevWord);
    }
}

std::string solve(const std::string& letters)
{
    std::deque<char> word;
    solveLoop(letters, word);
    return std::string(begin(word), end(word));
}

int solveCases(std::istream& is)
{
    std::string line;
    std::getline(is, line);
    std::istringstream iss(line);
    
    int cases;
    iss >> cases;
    
    for (auto i = 0; i < cases; ++i) {
        std::string line;
        std::getline(is, line);
        std::istringstream iss(line);
        
        std::string letters;
        iss >> letters;
        
        std::cout << "Case #" << i + 1 << ": " << solve(letters) << "\n";
    }
    
    return 0;
}

int main(int argc, const char * argv[]) {
    if (argc < 2)
        return solveCases(std::cin);
    else {
        std::ifstream ifs(argv[1]);
        return solveCases(ifs);
    }
}
