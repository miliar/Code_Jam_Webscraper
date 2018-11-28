#!/usr/bin/env cppsh
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

int solve(int shyness, const std::string& seats)
{
    int friends = 0;
    int total = seats[0] - '0';
    for (int i = 1; i < seats.size(); ++i)
    {
        if (total < i)
        {
            int additionalFriends = i - total;
            friends += additionalFriends;
            total += additionalFriends;
        }
        total += (seats[i] - '0');
    }

    return friends;
}

int main(int argc, char* argv[])
{
    std::vector<int> res;
    std::string str;
    std::getline(std::cin, str);
    const int N = atoi(str.c_str());
    for (int i = 0; i < N; ++i)
    {
        std::getline(std::cin, str);
        std::stringstream ss(str);
        int shy;
        std::string seats;
        ss >> shy >> seats;
        //std::cout << shy << " " << seats << std::endl;
        res.push_back(solve(shy, seats));
    }

    for (int i = 0; i < res.size(); ++i)
    {
        std::cout << "Case #" << (i+1) << ": " << res[i] << std::endl;
    }

    return 0;
}
