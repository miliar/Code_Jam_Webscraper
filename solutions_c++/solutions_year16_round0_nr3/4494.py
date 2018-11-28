#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>
#include <utility>
#include <bitset>

using namespace std;

std::vector<std::vector<unsigned long long int> > bases;
std::vector <unsigned long long> sumOfBases;
std::vector<unsigned long long int > edges;

void buildBases()
{
    for (int base = 2; base < 11; base++)
    {
        vector<unsigned long long> v;
        for (int position = 0; position < 16; position++)
        {
            v.push_back(pow(base,position));
        }
        bases.push_back(v);
        edges.push_back(pow(base,15)+1);
    }
}

void buildEdges()
{
    for (int base = 2; base < 11; base++)
    {
        vector<unsigned long long> v;
        for (int position = 0; position < 14; position++)
        {
            cout << bases[base-2][position] << " ";
        }
        cout <<endl;
    }
}

void buildSumOfBases()
{
    for (int base = 2; base < 11; base++)
    {
        unsigned long long sumOfBase = 0;
        for (int position = 0; position < 16; position++)
        {
           sumOfBase += pow(base, position);


        }
        sumOfBases.push_back(sumOfBase);
        cout << "base: " << base << endl;
        cout << sumOfBase << " ";
        cout << endl;
    }
}

int main()
{
//    ifstream fin("input.in");
    ifstream fin("C-small-attempt1.in");
    //ifstream fin("C-large.in");
    ofstream fout("output.out");

    //-- check if the files were opened successfully
    if (!fin.is_open()) cout << "input.in was not opened successfully" << endl;
    if (!fout.is_open()) cout << "output.out was not open successfully" << endl;
    int numCase;
    fin >> numCase;

    int smax = 0;

    int N = 0;
    int J = 0;

    fin >> N;
    fin >>J;
    buildBases();
    buildEdges();
    buildSumOfBases();

    fout << "Case #1:" <<endl;
    int caseNr = 1;
    for (unsigned long long i = pow(2,15)+1; i < pow(2,16)-1; i+=2 )
    {
        vector<unsigned long long> currentNumbers;
        currentNumbers.push_back(i);
        cout << i << endl;
        for (int base = 3; base <= 10; base++)
        {
            unsigned long long currentNumber = 0;
            for (int position = 0; position < 16; position++)
            {
                //cout << "bases[0][position]: "<< bases[0][position] <<endl;
                //cout << "(i&bases[0][position]): " << (i&bases[0][position]) <<endl;
                if ((i&bases[0][position]) != 0)
                    currentNumber+=(bases[base-2][position]);
            }
            currentNumbers.push_back(currentNumber);
            cout << "base: " << base << " " << "currentNumber: " <<currentNumber << endl;
        }
        vector<unsigned long long> divisors;
        for(int base = 2; base <=10; base++)
        {
            unsigned long long currentN = currentNumbers[base-2];
            cout << "base: " << base << " " << "currentN: " <<currentN << endl;
            unsigned long long sqrtOfCurrent = sqrt(currentN);
            for (unsigned long long ch = 2; ch < sqrtOfCurrent; ++ch)
            {
                if ((currentN % ch) == 0)
                {
                    divisors.push_back(ch);
                    ch = sqrtOfCurrent +1;
                    //cout << "ch: " <<ch << endl;
                }
            }

        }

        cout << "divisors.size(): " << divisors.size() << endl;
        if (divisors.size() == 9)
        {
            cout << "found case: " << caseNr << endl;
            std::bitset<16> x(i);
            fout <<x << " ";
            for (auto d : divisors){
                fout << d << " ";
            }
            fout << endl;
            caseNr++;
        }

        divisors.clear();

        if (caseNr == J+1) break;
    }


    fin.close();
    fout.close();
    return 0;
}
