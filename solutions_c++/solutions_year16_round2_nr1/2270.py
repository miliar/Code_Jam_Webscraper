#include <iostream>
#include <string>
#include <fstream>

int main()
{
    std::ifstream in("in");
    std::ofstream out("out");

    int T(0);

    in >> T;

    for(int i(0); i < T; i++)
    {
        std::string tmp;

        in >> tmp;

        out << "Case #" << i+1 << ": ";

        int zero(0);
        int two(0);
        int six(0);
        int eight(0);
        int seven(0);
        int five(0);
        int four(0);
        int three(0);
        int one(0);
        int nine(0);

        std::cout << tmp.find_first_of('Z');
        std::cout << tmp.find_first_of('E');
        std::cout << tmp.find_first_of('R');
        std::cout << tmp.find_first_of('O');

        while(tmp.find_first_of('Z') != -1)
        {
            zero++;
            tmp.erase(tmp.find_first_of('Z'), 1);
            tmp.erase(tmp.find_first_of('E'), 1);
            tmp.erase(tmp.find_first_of('R'), 1);
            tmp.erase(tmp.find_first_of('O'), 1);
        }

        while(tmp.find_first_of('W') != -1)
        {
            two++;
            tmp.erase(tmp.find_first_of('T'), 1);
            tmp.erase(tmp.find_first_of('W'), 1);
            tmp.erase(tmp.find_first_of('O'), 1);
        }

        while(tmp.find_first_of('X') != -1)
        {
            six++;
            tmp.erase(tmp.find_first_of('S'), 1);
            tmp.erase(tmp.find_first_of('I'), 1);
            tmp.erase(tmp.find_first_of('X'), 1);
        }

        while(tmp.find_first_of('G') != -1)
        {
            eight++;
            tmp.erase(tmp.find_first_of('E'), 1);
            tmp.erase(tmp.find_first_of('I'), 1);
            tmp.erase(tmp.find_first_of('G'), 1);
            tmp.erase(tmp.find_first_of('H'), 1);
            tmp.erase(tmp.find_first_of('T'), 1);
        }

        while(tmp.find_first_of('S') != -1)
        {
            seven++;
            tmp.erase(tmp.find_first_of('S'), 1);
            tmp.erase(tmp.find_first_of('E'), 1);
            tmp.erase(tmp.find_first_of('V'), 1);
            tmp.erase(tmp.find_first_of('E'), 1);
            tmp.erase(tmp.find_first_of('N'), 1);
        }

        while(tmp.find_first_of('V') != -1)
        {
            five++;
            tmp.erase(tmp.find_first_of('F'), 1);
            tmp.erase(tmp.find_first_of('I'), 1);
            tmp.erase(tmp.find_first_of('V'), 1);
            tmp.erase(tmp.find_first_of('E'), 1);
        }

        while(tmp.find_first_of('F') != -1)
        {
            four++;
            tmp.erase(tmp.find_first_of('F'), 1);
            tmp.erase(tmp.find_first_of('O'), 1);
            tmp.erase(tmp.find_first_of('U'), 1);
            tmp.erase(tmp.find_first_of('R'), 1);
        }

        while(tmp.find_first_of('H') != -1)
        {
            three++;
            tmp.erase(tmp.find_first_of('T'), 1);
            tmp.erase(tmp.find_first_of('H'), 1);
            tmp.erase(tmp.find_first_of('R'), 1);
            tmp.erase(tmp.find_first_of('E'), 1);
            tmp.erase(tmp.find_first_of('E'), 1);
        }

        while(tmp.find_first_of('O') != -1)
        {
            one++;
            tmp.erase(tmp.find_first_of('O'), 1);
            tmp.erase(tmp.find_first_of('N'), 1);
            tmp.erase(tmp.find_first_of('E'), 1);
        }

        while(tmp.find_first_of('I') != -1)
        {
            nine++;
            tmp.erase(tmp.find_first_of('N'), 1);
            tmp.erase(tmp.find_first_of('I'), 1);
            tmp.erase(tmp.find_first_of('N'), 1);
            tmp.erase(tmp.find_first_of('E'), 1);
        }

        for(int j(0); j < zero; j++)
            out << "0";
        for(int j(0); j < one; j++)
            out << "1";
        for(int j(0); j < two; j++)
            out << "2";
        for(int j(0); j < three; j++)
            out << "3";
        for(int j(0); j < four; j++)
            out << "4";
        for(int j(0); j < five; j++)
            out << "5";
        for(int j(0); j < six; j++)
            out << "6";
        for(int j(0); j < seven; j++)
            out << "7";
        for(int j(0); j < eight; j++)
            out << "8";
        for(int j(0); j < nine; j++)
            out << "9";
        out << std::endl;
    }

    return 0;
}
