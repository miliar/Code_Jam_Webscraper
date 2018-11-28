//
//  b.cpp
//
//

#include <cstdlib>
#include <stdint.h>
#include <iostream>
#include <iomanip>
#include <utility>
#include <functional>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <math.h>

//#include <boost/multi_array.hpp>


// function prototypes

// utility functions

// read vector from text file
template <typename T>
void rd
(
    std::ifstream & inFile,
    std::vector<T> & v,
    int const N // number of elements
)
{
    v.resize(N);
    for (int i=0; i<N; i++)
        inFile >> v[i];
}

// read set from text file
template <typename T>
void rd
(
    std::ifstream & inFile,
    std::set<T> & s,
    int const N // number of elements
)
{
    for (int i=0; i<N; i++) {
        T elt;
        inFile >> elt;
        s.insert(elt);
    }
}

// prints vector to std::cout
template <typename T>
void pr(std::vector<T> const & v)
{
    for (int i=0; i<(int)v.size(); i++)
    {
        if (i>0)
            std::cout << " ";
        std::cout << v[i];
    }
    std::cout << "\n";
}

// prints set to std::cout
template <typename T>
void pr(std::set<T> const & s)
{
    for (typename std::set<T>::const_iterator it=s.begin(); it!=s.end(); ++it)
    {
        if (it!=s.begin())
            std::cout << " ";
        std::cout << *it;
    }
    std::cout << "\n";
}

// prints map to std::cout
template <typename T, typename S>
void pr(std::map<T,S> const & m)
{
    for (typename std::map<T,S>::const_iterator it=m.begin(); it!=m.end(); ++it)
    {
        std::cout << it->first << " " << it->second << "\n";
    }
}




// globals

std::ifstream inFile;

// functions

void setup()
{
}


void processCase()
{

    int N;
    inFile >> N;
    
    std::vector <int> A(N);
    rd(inFile,A,N);

    int c=0;
    while (A.size()>1) {
        std::vector <int>::iterator mit = std::min_element(A.begin(),A.end());
        int p=mit-A.begin();
        c += std::min(p,(int)A.size()-1-p);
        A.erase(mit);
    }

    std::cout << c << "\n";
}


// main

int main(int argc, char const * argv[])
{

    int T;
    
    // make sure filename is provided
    if (argc != 2)
    {
        std::cout << "Expected one argument\n";
        std::exit(0);
    }
    
    // open input file
    inFile.open(argv[1]);
    
    inFile >> T;
    
    
    setup();
    
    std::cout << std::setprecision(9);
    
    for (int caseIndex=1; caseIndex<=T; caseIndex++)
    {
        std::cout << "Case #" << caseIndex << ": ";
        processCase();
    }
    
    return 0;
}
