#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <iterator>

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

map<char, int> str2map(string S) {
    map<char, int> out;
    out['E'] = 0;
    out['F'] = 0;
    out['G'] = 0;
    out['H'] = 0;
    out['I'] = 0;
    out['N'] = 0;
    out['O'] = 0;
    out['R'] = 0;
    out['S'] = 0;
    out['T'] = 0;
    out['U'] = 0;
    out['V'] = 0;
    out['W'] = 0;
    out['X'] = 0;
    out['Z'] = 0;
    for (unsigned i = 0; i < S.size(); ++i)
    {
        out[S[i]]++;
    }

    return out;
}

void removeLetters(string S, map<char, int> &out, int n) {
    for (unsigned i = 0; i < S.size(); ++i)
    {
        out[S[i]] -= n;
    }
}

string getPhoneNumbers(string S) {
    map<char, int> str = str2map(S);
    vector<pair<char, string> > algo = {{'Z',"ZERO"},{'W',"TWO"},{'U',"FOUR"},{'X',"SIX"},{'G',"EIGHT"},{'S',"SEVEN"},{'F',"FIVE"},{'O',"ONE"},{'T',"THREE"},{'I',"NINE"}};
    vector<int> numbers = {0,0,0,0,0,0,0,0,0,0};
    vector<char> order = {0,7,1,8,2,6,3,5,4,9};
    string out = "";

    for (int i = 0; i < 10; i++)
    {
        numbers[i] = str[algo[i].first];
        removeLetters(algo[i].second, str, numbers[i]);
    }

    for (int i = 0; i < 10; i++)
    {
        for (int j = 0; j < numbers[order[i]]; ++j)
        {
            out += to_string(i);
        }
    }

    return out;
}

int main(int argc, char const *argv[])
{
    if (argc != 2)
    {
        cerr << "Usage : " << argv[0] << " <filename>" << endl;
        exit(1);
    }

    string filename = string(argv[1]);
    vector<string> input = fileToVectorString(filename);

    for (int i = 0; i < atoi(input[0].c_str()); ++i)
    {
        cout << "Case #" << (i+1) << ": " << getPhoneNumbers(input[i+1]) << endl;
    }

    exit(0);
}