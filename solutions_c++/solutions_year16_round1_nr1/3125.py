
// g++ --std=c++11 a.cpp -o a.bin && a.bin < test.in > test.out

#include <iostream>
#include <string>
#include <deque>

int main()
{
    int T;
    std::cin >> T;
    std::string line;

    std::getline( std::cin , line );
    for ( int t = 1 ; t <= T ; ++t ) {
        std::getline( std::cin , line );
        std::cerr<<"Line is "<<line<<" and line.length() is "<<line.length()<<std::endl;

        std::deque<char> result;
        result.push_front( line[0] );

        for ( int i = 1 ; i < line.length() ; ++i ) {
            if ( line[i] < result.front() )
                result.push_back( line[i] );
            else
                result.push_front( line[i] );
        }

        std::cout << "Case #" << t << ": ";
        for ( auto it = result.cbegin() ; it != result.cend() ; ++it )
            std::cout << *it;
        std::cout<<'\n';
    }

    return 0;
}
