#include <fstream>
#include <iostream>
#include <vector>
#include <limits>
#include <algorithm>
#include <string>
#include <sstream>

typedef std::vector<std::vector<size_t>> VecCharCount;

bool update_charcount(VecCharCount& vecs, std::string& standard, const std::string& instr, bool bFirst)
{
    std::string newstr = instr;
    auto it = std::unique(newstr.begin(), newstr.end());
    newstr = newstr.substr(0, (size_t)std::distance(newstr.begin(), it));
    if (bFirst) standard = newstr;
    else if (standard != newstr) return false;


    std::vector<size_t> vec(standard.length(), 0);
    for (size_t idx = 0, jdx = 0; idx < instr.size(); ++ idx)
    {
        if (idx == 0 || instr[idx] == instr[idx-1])
        {
            ++ vec[jdx];
        } else {
            ++ jdx;
            ++ vec[jdx];
        }
    }
    vecs.push_back(vec);
    return true;
}

size_t mincount(const std::vector<size_t>& cvec)
{
    //std::vector<size_t> uvec(cvec);
    //auto it = std::unique(uvec.begin(), uvec.end());
    //uvec.resize((size_t)std::distance(uvec.begin(), it));
    size_t minval = std::numeric_limits<size_t>::max();
    size_t maxval = 0;
    for (auto ival : cvec)
    {
        if (ival > maxval)
            maxval = ival;
        if (ival < minval)
            minval = ival;
    }
    //auto mm = std::minmax(cvec.begin(), cvec.end());
    //std::cout << *mm.first << " " << *mm.second << std::endl;
    //TODO Why didn't this work?
    size_t minchanges = std::numeric_limits<size_t>::max();
    for (size_t splitval = minval; splitval <= maxval; ++ splitval)
    {
        size_t nchanges = 0;
        for (auto ival : cvec)
            nchanges += (size_t)fabs((double)splitval - (double)ival);
        if (nchanges < minchanges)
            minchanges = nchanges;
    }
    return minchanges;
}

size_t get_best_count(std::vector<std::vector<size_t>>& charcounts)
{
    size_t bestcount = 0;
    size_t nchars = charcounts[0].size();
    for (size_t ichar = 0; ichar < nchars; ++ ichar)
    {
        std::vector<size_t> vec;
        // walk through all strings, 
        for (size_t istr = 0, jstr = charcounts.size(); istr < jstr; ++ istr)
        {
            vec.push_back(charcounts[istr][ichar]);
        }
        bestcount += mincount(vec);
    }
    return bestcount;
}

void solve_case(int icase, std::ifstream& ifile)
{
    size_t nstrs;
    ifile >> nstrs;
    std::vector<std::string> strings;
    std::string standard;
    std::vector<std::vector<size_t>> charcount;
    bool failed = false;
    for (size_t istr = 0; istr < nstrs; ++ istr)
    {
        std::string tmpstr;
        ifile >> tmpstr;
        if (!update_charcount(charcount, standard, tmpstr, istr == 0))
        {
            failed = true;
            break;
        }
    }

    size_t tbest = failed ? 0 : get_best_count(charcount);

    std::stringstream res;
    if (failed) res << "Fegla Won";
    else res << tbest;
    std::cout << "Case #" << icase << ": " << res.str() << std::endl;
}

void all_cases(std::ifstream& ifile)
{
    int ncases;
    ifile >> ncases;
    for (int i = 0; i < ncases; ++ i)
    {
	solve_case(i+1, ifile);
    }
}

int main(int argv, char** argc)
{
    if (argv < 2)
    {
	std::cerr << "Usage: " << std::string(argc[0]) << " inputfile\n";
	return -1;
    }
    std::ifstream infile(argc[1]);
    all_cases(infile);
}
