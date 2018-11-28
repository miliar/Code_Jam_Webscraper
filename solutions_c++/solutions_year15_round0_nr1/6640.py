#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <queue>
#include <string>
#include <sstream>
#include <cstdlib>

using namespace std;

std::vector<int> S_a;

std::vector<int> readCase( char* line ){
    std::vector<int> a;
    int n;
    std::stringstream l(line);

    l >> n;

    char c;
    l.read(&c, 1);
    for (int i = 0; i < n+1; i++) {
        l.read(&c, 1);
        a.push_back( std::atoi(&c) );
    }

    //for (int i = 0; i < n+1; i++) {
    //    std::cout << a[i];
    //}
    //std::cout << " ";

    return a;
}

void calcCase( std::vector<int> c ){
    int n = 0;
    int standing = 0;
    for (int i = 0; i < c.size(); i++) {
        if( (n+standing) >= i ){
            standing += c[i];
        } else {
            n += i - (standing+n);
            standing += c[i];
        }
    }
    std::cout << n;
}

int main(int argc, const char *argv[])
{
    std::fstream fin( argv[1] );

    int cases;
    fin >> cases;
    char line[1100];
    fin.getline(line, 1100);
    for( int i = 1; i <= cases; i++ ){
        std::cout << "Case #" << i << ": ";

        fin.getline(line, 1100);
        auto c = readCase(line);

        calcCase(c);


        std::cout << endl;
    }


    return 0;
}
