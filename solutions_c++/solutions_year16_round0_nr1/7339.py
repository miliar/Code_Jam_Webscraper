#include <iostream>
#include <fstream>
#include <string>
#include <set>

void digits(std::set<int> &d, int n)
{
    do {
        d.insert(n%10);
        n /= 10;
    } while (n);
}

void solve(const int caseNum, const int num)
{
    std::set<int> d;
    int m = 1;
    bool done = false;
    
    while (!done) {
        int n = num * m;
        m += 1;
        int next = num * m;
        digits(d, n);
        if (n == next) {
            std::cout << "Case #" << caseNum << ": " << "INSOMNIA" << std::endl;
            done = true;
        } else if (d.size() == 10) {
            std::cout << "Case #" << caseNum << ": " << n << std::endl;
            done = true;
        }
    }
}

int main(const int argc, const char *argv[])
{
    if (argc < 2) {
        std::cout << "Missing filename" << std::endl;
        return 0;
    }
    
    std::ifstream fin(argv[1]);
    std::string line;
    for (int c = 0; std::getline(fin, line); ++c) {
        if (c > 0) {
            solve(c, std::stoi(line));
        }
    }
}