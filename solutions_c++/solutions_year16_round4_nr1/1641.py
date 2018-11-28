#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <iterator>

using namespace std;

#ifndef max
#define max(a,b) (a<b?b:a)
#endif

#ifndef min
#define min(a,b) (a>b?b:a)
#endif

vector<vector<int> > fileToVectorVectorInt(string filename) {
    std::vector<vector<int> > v;
    char *buf = (char*)malloc(1024*sizeof(char));
    size_t n;
    if (FILE *fp = fopen(filename.c_str(), "r")) {
        while (getline(&buf, &n, fp) > 0) {
            istringstream iss(buf);
            vector<string> tokens{istream_iterator<string>{iss},
                                  istream_iterator<string>{}};
            vector<int> x(tokens.size());
            transform(tokens.begin(), tokens.end(), x.begin(), [](string a) {return stoi(a);});
            v.push_back(x);
        }
        fclose(fp);
    }
    return v;
}

vector<string> genPossibleCombinaison(int R, int P, int S) {
    vector<string> out;
    if (R+P+S == 1) {
             if (R == 1) { out.push_back("R"); }
        else if (P == 1) { out.push_back("P"); }
        else if (S == 1) { out.push_back("S"); }
    }
    else {
        for (int i = 0; i < P+R+S; ++i) {
            if (P>0) {
                vector<string> sub = genPossibleCombinaison(R,P-1,S);
                for (std::vector<string>::iterator j = sub.begin(); j != sub.end(); ++j) {
                    out.push_back(string("P") + *j);
                }
            }
            if (R>0) {
                vector<string> sub = genPossibleCombinaison(R-1,P,S);
                for (std::vector<string>::iterator j = sub.begin(); j != sub.end(); ++j) {
                    out.push_back(string("R") + *j);
                }
            }
            if (S>0) {
                vector<string> sub = genPossibleCombinaison(R,P,S-1);
                for (std::vector<string>::iterator j = sub.begin(); j != sub.end(); ++j) {
                    out.push_back(string("S") + *j);
                }
            }
        }
    }

    return out;
}

char match(char J1, char J2) {
    switch(J1) {
        case 'P':
            switch(J2) {
                case 'P': return 'T';
                case 'R': return 'P';
                case 'S': return 'S';
                default : return 'T';
            }
        case 'R':
            switch(J2) {
                case 'P': return 'P';
                case 'R': return 'T';
                case 'S': return 'R';
                default : return 'T';
            }
        case 'S':
            switch(J2) {
                case 'P': return 'S';
                case 'R': return 'R';
                case 'S': return 'T';
                default : return 'T';
            }
                default : return 'T';
    }
}

bool isOk(string comb) {
    while(comb.size() > 0) {
        string next("");
        for (int i = 0; i < comb.size()/2; ++i) {
            next += match(comb[2*i],comb[2*i+1]);
            if (next[i] == 'T') {
                return false;
            }
        }
        comb = next;
    }
    return comb[0] != 'T';
}

string findFirstWay(vector<int> x) {
    if ((1<<x[0]) != x[1] + x[2] + x[3]) {
        return string("IMPOSSIBLE");
    }

    vector<string> possibilities = genPossibleCombinaison(x[1],x[2],x[3]);
    vector<string>::iterator it;
    it = std::unique (possibilities.begin(), possibilities.end());
    possibilities.resize( std::distance(possibilities.begin(),it) );

    for (vector<string>::iterator i = possibilities.begin(); i != possibilities.end(); ++i) {
        if (isOk((*i))) {
            return (*i);
        }
    }

    return string("IMPOSSIBLE");
}

int main(int argc, char const *argv[])
{
    if (argc != 2)
    {
        cerr << "Usage : " << argv[0] << " <filename>" << endl;
        exit(1);
    }

    string filename = string(argv[1]);
    vector<vector<int> > input = fileToVectorVectorInt(filename);

    for (int i = 0; i < input[0][0]; ++i)
    {
        cout << "Case #" << (i+1) << ": " << findFirstWay(input[i+1]) << endl;
    }

    exit(0);
}