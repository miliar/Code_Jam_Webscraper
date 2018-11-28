#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

vector<string> ReadTasks(istream& is)
{
    size_t taskCount;
    is >> taskCount;
    vector<string> tasks;
    while (taskCount-- > 0)
    {
        string pancakes;
        is >> pancakes;
        tasks.push_back(pancakes);
    }
    return move(tasks);
}

void FlipSequence(size_t finalPosition, string& pancakes)
{
    char newValue = static_cast<char>(88 - pancakes[0]);
    for (size_t i = 0; i < finalPosition; ++i)
    {
        pancakes[i] = newValue;
    }
}

size_t GetFlipCount(string& pancakes)
{
    size_t flipCount = 0;
    size_t pos;
    size_t length = pancakes.size();
    for (pos = 0; pos < length && pancakes[pos] == '+'; ++pos);
    // early exit
    if (pos == length)
    {
        return 0;
    }
    if (pos > 0)
    {
        // make the initial sequence '-'
        FlipSequence(pos, pancakes);
        ++flipCount;
    }
    while (pos < length)
    {
        for (; pos < length && pancakes[pos] == '-'; ++pos);
        FlipSequence(pos, pancakes);
        ++flipCount;
        for (; pos < length && pancakes[pos] == '+'; ++pos);
        if (pos == length)
        {
            return flipCount;
        }
        FlipSequence(pos, pancakes);
        ++flipCount;
    }
    // include last flip
    return flipCount + 1;
}

int main()
{
    std::ifstream is("input.txt");
    std::ofstream out("output.txt");
    vector<string> tasks = ReadTasks(is);
    for (size_t i = 0; i < tasks.size(); ++i)
    {
        out << "Case #" << i + 1 << ": " << GetFlipCount(tasks[i]) << std::endl;
    }
}