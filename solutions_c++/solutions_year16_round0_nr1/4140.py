#include "readline.hpp"
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

vector<int> fileToVectorInt(string filename) {
    std::vector<int> v;
    char *buf = (char*)malloc(1024*sizeof(char));
    size_t n;
    if (FILE *fp = fopen(filename.c_str(), "r"))
    {
        while (getline(&buf, &n, fp) > 0)
            v.push_back(atoi(buf));
        fclose(fp);
    }
    return v;
}

void updateMap(int val, map<char, int> & m)
{
    string s = std::to_string(val);
    for (unsigned i = 0; i < s.size(); ++i)
    {
        m[s[i]] = 1;
    }
}

int tryUpTo(int N, int max)
{
    int i = 0;
    int current = 0;
    map<char, int> list;

    while (list.size() < 10 && i <= max)
    {
        current+=N;
        i++;
        updateMap(current, list);
    }

    return i>max?-1:current;
}

int main(int argc, char const *argv[])
{
    if (argc != 2)
    {
        exit(1);
    }

    string filename = string(argv[1]);
    vector<int> input = fileToVectorInt(filename);

    for (int i = 0; i < input[0]; ++i)
    {
        int r = tryUpTo(input[i+1],1000000);
        if (r == -1)
        {
            cout << "Case #" << (i+1) << ": " << "INSOMNIA" << endl;
        }
        else
        {
            cout << "Case #" << (i+1) << ": " << r << endl;
        }
    }

    exit(0);
}