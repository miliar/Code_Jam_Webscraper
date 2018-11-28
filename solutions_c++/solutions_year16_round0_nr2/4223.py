#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

vector<string> fileToVectorString(string filename) {
    std::vector<string> v;
    char *buf = (char*)malloc(1024*sizeof(char));
    size_t n;
    if (FILE *fp = fopen(filename.c_str(), "r"))
    {
        while (getline(&buf, &n, fp) > 0) {
            v.push_back(string(buf));
            v[v.size()-1].pop_back();
        }
        fclose(fp);
    }
    return v;
}

int flips(string s)
{
    int out = 0;
    for (unsigned i = 1; i < s.size(); ++i)
    {
        if (s[i-1] != s[i])
        {
            out++;
        }
    }
    if (s[s.size()-1] == '-')
    {
        out++;
    }
    return out;
}

int main(int argc, char const *argv[])
{
    if (argc != 2)
    {
        exit(1);
    }

    string filename = string(argv[1]);
    vector<string> input = fileToVectorString(filename);

    for (int i = 0; i < stoi(input[0]); ++i)
    {
        int r = flips(input[i+1]);
        if (r == -1)
        {
            cout << "Case #" << (i+1) << ": " << "IMPOSSIBLE" << endl;
        }
        else
        {
            cout << "Case #" << (i+1) << ": " << r << endl;
        }
    }

    exit(0);
}