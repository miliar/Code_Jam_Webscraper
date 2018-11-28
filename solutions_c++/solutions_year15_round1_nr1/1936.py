#ifndef BASIC_H
#define BASIC_H

#include <algorithm>
#include <iostream>
#include <iterator>
#include <set>
#include <sstream>
#include <string>

template<typename T>
T parse(std::string const& str)
{
    T value;
    std::istringstream iss(str);
    iss >> value;
    return value;
}

template<typename T>
void readTokens(std::vector<T> & tokens)
{
    std::string line;
    std::getline(std::cin, line);
    std::istringstream iss(line);
    T token;
    while (iss >> token)
    {
        tokens.push_back(token);
    }
}

template<typename T>
void readTokens(std::vector<T> & tokens, char delim)
{
    std::string line;
    std::getline(std::cin, line);
    std::istringstream iss(line);
    std::string tokenStr;
    while (std::getline(iss, tokenStr, delim))
    {
        tokens.push_back(parse<T>(tokenStr));
    }
}

template<typename T>
void readTokens(std::vector<T> & tokens, size_t n)
{
    T token;
    for (int i = 0; i != n; ++i)
    {
        std::cin >> token;
        tokens.push_back(token);
    }
}

template<typename T>
std::ostream & operator<<(std::ostream & os, std::vector<T> const& v)
{
    std::copy(v.begin(), v.end(), std::ostream_iterator<T>(os, " "));
    return os;
}


#endif /* end of include guard: BASIC_H */

int main(int argc, char * argv[])
{
    int T;
    std::cin >> T;

    for (size_t t = 0; t != T; ++t)
    {
        std::cout << "Case #" << t + 1 << ": ";

        size_t N;
        std::cin >> N;

        std::vector<int> M;
        readTokens(M, N);

        int maxD = 0;
        int minA = 0;
        for (size_t i = 0; i != N - 1; ++i)
        {
            int D = M[i] - M[i+1];
            if (D > maxD)
            {
                maxD = D;
            }

            if (D > 0)
            {
                minA += D;
            }
        }

        //std::cout << maxD << std::endl;
        int minB = 0;
        for (size_t i = 0; i != N - 1; ++i)
        {
            if (M[i+1] > 0)
            {
                if (M[i] > maxD)
                {
                    minB += maxD;
                }
                else
                {
                    minB += M[i];
                }
            }
            else
            {
                minB += std::min(M[i], maxD);
            }
        }
        std::cout << minA << " " << minB << std::endl;
    }
    return 0;
}

