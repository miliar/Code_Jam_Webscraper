#include <iostream>
#include <fstream>
#include <vector>

typedef std::vector<std::string> Strings;

struct Str {
    Str() : c(-1), count(0) {}
    Str(char ch, int cnt) : c(ch), count(cnt) {}

    char c;
    unsigned count;
};

typedef std::vector<std::vector<Str> > Strs;

bool Parse(const Strings& strs, Strs* strs_p)
{
    for (unsigned i = 0; i < strs.size(); ++i) {
        char c = 0;
        int index = -1;
        for (unsigned j = 0; j < strs[i].size(); ++j) {
            if (strs[i][j] != c) {
                c = strs[i][j];
                (*strs_p)[i].push_back(Str(c, 1));
                ++index;
            } else {
                ++(*strs_p)[i][index].count;
            }
        }
    }

    unsigned num_chars = (*strs_p)[0].size();

    for (unsigned n = 0; n < num_chars; ++n) {
        char c = (*strs_p)[0][n].c;
        for (unsigned i = 0; i < strs_p->size(); ++i) {
            if ((*strs_p)[i].size() != num_chars) {
                return false;
            }

            if ((*strs_p)[i][n].c != c) {
                return false;
            }
        }
    }
    return true;
}

void Repeater(const Strings& strs)
{
    Strs s(strs.size());;
    if (!Parse(strs, &s)) {
        std::cout << "Fegla Won\n";
        return;
    }

    unsigned num_chars = s[0].size();

    unsigned num_moves = 0;
    for (unsigned n = 0; n < num_chars; ++n) {
        unsigned count = 0;
        for (unsigned i = 0; i < s.size(); ++i) {
            count += s[i][n].count; 
        }
        unsigned avg = count/s.size();
        for (unsigned i = 0; i < s.size(); ++i) {
            if (avg == s[i][n].count) {
                // No moves.
            } else if (avg > s[i][n].count) {
                num_moves += avg - s[i][n].count;
            } else {
                num_moves += s[i][n].count-avg;
            }
        }
    }
    std::cout << num_moves << '\n';
}

int main(int argc, const char* argv[])
{
    if (argc != 2) {
        std::cout << "Missing file containing input\n";
        return -1;
    }

    std::ifstream istr(argv[1]);

    // Read in the number of test cases.
    unsigned T;
    istr >> T;

    for (unsigned i = 1; i <= T; ++ i) {
        unsigned N;
        istr >> N;
        Strings strs;
        for (unsigned j = 0; j < N; ++j) {
            std::string s;
            istr >> s;
            strs.push_back(s);
        }
            
        std::cout << "Case #" << i << ": ";
        Repeater(strs);
    }

    return 0;
}
