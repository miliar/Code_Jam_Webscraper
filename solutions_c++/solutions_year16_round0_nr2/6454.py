#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

vector<string> ReadFile(string path);
void WriteFile(string path, vector<string> content);
bool HappyPancakes(string &pancakes);
int BlankLength(string &pancakes, int index);
void Flip(string &pancakes, int startIndex);

int main()
{
    vector<string> file = ReadFile("input.txt");

    vector<string> results;

    for(unsigned int i = 1; i < file.size(); i++)
    {
        string line = file.at(i);
            unsigned long count = line.length();
            int flipcounter = 0;
            for(int h = 0; h < count - 1; h++)
            {
                if(line[h] != line[h + 1])
                {
                    flipcounter++;
                }
            }
            if (line[count - 1] == '-')
                flipcounter++;
        string result = "Case #" + to_string(i) + ": " + to_string(flipcounter);
        results.push_back(result);
    }

    WriteFile("output.txt", results);

    return 0;
}


void Flip(string &pancakes)
{
    int startIndex = 0;
    int len = BlankLength(pancakes, startIndex);
    int count = 0;
    for (int i = startIndex; count < len; i++)
    {
        switch(pancakes[i])
        {
            case '-':
                pancakes[i] = '+';
                break;
            case '+':
                pancakes[i] = '-';
                break;
            default:
                break;
        }
        count++;
    }
}

int BlankLength(string &pancakes, int index)
{
    int len = pancakes.length();
    int count = 1;
    while (index < len)
    {
        if (pancakes[index] == '+')
            return count - 1;
        count++;
        index++;
    }
    return count;
}

bool HappyPancakes(string &pancakes)
{
    for(char c : pancakes)
    {
        if(c == '-')
            return false;
    }
    return true;
}

vector<string> ReadFile(string path)
{
    ifstream f(path);
    vector<string> file;
    string currentLine;

    while(f >> currentLine)
    {
       file.push_back(currentLine);
    }
    f.close();

    return file;
}

void WriteFile(string path, vector<string> content)
{
    ofstream f(path);
    if (f.is_open())
    {
        for (string line : content)
        {
            f << line << endl;
        }
        f.close();
    }
}

