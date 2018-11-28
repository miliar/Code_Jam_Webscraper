
#include <iostream>
#include <vector>
#include <string>

int main()
{
    int T;
    std::cin >> T;
    std::string line;

    std::getline( std::cin , line );
    for ( int t = 1 ; t <= T ; ++t ) {
        std::getline( std::cin , line );
        std::cerr<<"Line is "<<line<<" and line.length() is "<<line.length()<<std::endl;

        int result = 0;

        for ( int i = 0 ; i < line.length() - 1 ; ++i ) {
            if ( line[i] != line[i+1] )
                ++result;
        }
        if ( line[ line.length() - 1 ] == '-' )
            ++result;

        std::cout << "Case #" << t << ": " << result << '\n';
    }

    return 0;
}
