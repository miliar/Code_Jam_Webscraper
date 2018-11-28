#include <fstream>
#include <iostream>
#include <cmath>

size_t get_digit(size_t K, size_t idx)
{
    return ((K >> idx) & 0x1);
}

size_t get_ways(size_t A, size_t B, size_t K, size_t idigit = 32,
        size_t anow = 0,
        size_t bnow = 0)
{
    
    size_t dig = get_digit(K, idigit);
    size_t digval = (size_t)pow(2, idigit);
    bool admitA = (anow + digval) < A;
    bool admitB = (bnow + digval) < B;
    if (idigit == 0)
    {
        if (dig == 1) 
        {
            return (admitA && admitB) ? 1 : 0;
        }
        else
        {
            size_t count = 1;
            if (admitA) ++ count;
            if (admitB) ++ count;
            return count;
        }
    }

    if (dig == 1) {
        // 1 1
        if (admitA && admitB)
        {
            return get_ways(A, B, K, idigit - 1, anow + digval, bnow + digval);
        }
        return 0;
    } else {
        // 1 0, 0 1, 0 0
        size_t nways = get_ways(A, B, K, idigit - 1, anow, bnow);
        if (admitA) nways += get_ways(A, B, K, idigit - 1, anow + digval, bnow);
        if (admitB) nways += get_ways(A, B, K, idigit - 1, anow, bnow + digval);
        return nways;
    }
}

void solve_case(int icase, std::ifstream& ifile)
{
    size_t A, B, K;
    ifile >> A >> B >> K;
    size_t nways = 0;
    for (size_t ik = 0; ik < K; ++ ik)
        nways += get_ways(A, B, ik);

    std::cout << "Case #" << icase << ": " << nways << std::endl;
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
