#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <set>
#include <utility>
#include <cmath>
#include <sstream>

using namespace std;

int main()
{
    ifstream in("in.txt");
    ofstream out("out.txt");

    int t;

    string line;
    getline (in, line);
    stringstream ss(line);
    ss >> t;

    cout << t << endl;

    for(unsigned tnum = 0; tnum < t; ++tnum)
    {
        int n;

        string line;
        getline (in, line);
        stringstream ss(line);

        ss >> n;
        cout << n << endl;

        vector<vector<pair<char, int > > > words;
        int len0 = -1;
        bool impossible = false;

        for(int i = 0; i < n; ++i)
        {
            string s;
            getline(in, s);

            vector<pair<char, int> > word;

            for(unsigned j = 0; j < s.size(); ++j)
            {
                char ch = s[j];
                if(j==0 || ch != s[j-1])
                {
                    word.push_back(make_pair(ch, 1));
                }
                else
                {
                    word.back().second++;
                }
            }

            if(len0 != -1)
            {
                if(len0 != word.size())
                {
                    impossible = true;
                    break;
                }

                for(unsigned j = 0; j < word.size(); ++j)
                {
                    if(word[j].first != words[i-1][j].first)
                    {
                        impossible = true;
                        break;
                    }
                }

                if(impossible) break;
            }

            len0 = word.size();
            words.push_back(word);
        }

        if(impossible)
        {
            out << "Case #" << tnum+1 << ": Fegla Won" << endl;
            continue;
        }

        unsigned actions = 0;

        for(unsigned i = 0; i < len0; ++i)
        {
            unsigned sum = 0;

            for(unsigned j=0; j<words.size(); ++j)
                sum+=words[j][i].second;

            unsigned avg = floor(0.5 + sum / words.size());


            for(unsigned j=0; j<words.size(); ++j)
                actions += (words[j][i].second > avg ? words[j][i].second - avg : avg - words[j][i].second);
        }

        out << "Case #" << tnum+1 << ": " << actions << endl;
    }

    return 0;
}
