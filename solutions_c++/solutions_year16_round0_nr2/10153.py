#include <iostream>
#include <fstream>
#include <string>
#include <iterator>
using namespace std;

bool done(string line);

int main()
{
    ifstream file("B-large.in");
    ofstream output("outB.txt");
    string line;
    int index = 0;
    int flips = 0;
    getline(file, line);
    int cases = atoi(line.c_str());
    for (int casen = 1; casen <= cases; casen++)
    {
        flips = 0;
        getline(file, line);
        while (!done(line))
        {
            index = 0;
            if (line[index] == '-')
            {
                while (line[index] == '-')
                {
                    auto p = line.begin();
                    advance(p, index);
                    line.erase(p);
                    line.insert(index, "+");
                    index++;
                }
                flips++;
                continue;
            }
            if (line[index] == '+')
            {
                auto start = line.begin();
                advance(start, index);
                while (line[index] == '+')
                {
                    index++;
                }
                auto finish = line.begin();
                advance(finish, index);
                int dist = distance(start, finish);
                line.erase(start, finish);
                line.insert(start, dist, '-');
                flips++;
            }
        }
        output << "Case #" << casen << ": " << flips << endl;
    }
}

bool done(string line)
{
    for (int i = 0; i < line.length(); i++)
    {
        if (line[i] != '+') return false;
    }
    return true;
}