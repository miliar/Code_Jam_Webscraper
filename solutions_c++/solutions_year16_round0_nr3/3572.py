#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <gmp.h>

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

int notPrimeInEveryBases(string s)
{
    mpz_t v;
    mpz_init(v);

    for (int i = 2; i <= 10; ++i)
    {
        mpz_set_str(v,s.c_str(),i);
        if (mpz_probab_prime_p(v,25))
        {
            return 0;
        }
    }
    mpz_clear(v);
    return 1;
}

void getListDivisor(string s) {
    mpz_t v;
    mpz_init(v);

    for (int i = 2; i <= 10; ++i)
    {
        mpz_set_str(v,s.c_str(),i);
        int j = 2;
        while (!mpz_divisible_ui_p(v,j)) 
        {
            j++;
        }
        cout << " " << j;
    }
    mpz_clear(v);
}

void nextJamCoin(mpz_t & val) {
    mpz_add_ui(val,val,2);
    char * str = mpz_get_str(NULL,2,val);
    while (!notPrimeInEveryBases(str))
    {
        mpz_add_ui(val,val,2);
        free(str);
        str = mpz_get_str(NULL,2,val);
    }
    cout << str;
    getListDivisor(str);
    cout << endl;
}

int main(int argc, char const *argv[])
{
    if (argc != 2)
    {
        exit(1);
    }

    string filename = string(argv[1]);
    vector<string> input = fileToVectorString(filename);

    istringstream iss(input[1]);
    vector<string> tokens{istream_iterator<string>{iss},
                          istream_iterator<string>{}};
    
    int N = stoi(tokens[0]);
    int J = stoi(tokens[1]);
    string init(N,'0');
    init[0] = '1';
    init[N-1] = '1';
    mpz_t current;
    mpz_init(current);
    mpz_set_str(current,init.c_str(),2);
    mpz_sub_ui(current,current,2);

    cout << "Case #1:" << endl;

    int i = 0;
    while (i < J)
    {
        nextJamCoin(current);
        i++;
    }

    exit(0);
}