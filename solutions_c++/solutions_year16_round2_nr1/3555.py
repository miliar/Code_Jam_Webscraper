
// g++ --std=c++11 a.cpp -o a.bin -O2 && a.bin < test.in > test.out

#include <iostream>
#include <string>
#include <unordered_map>

namespace{
    std::string spellings[] = { "ZERO" , "ONE" , "TWO" , "THREE" , "FOUR" , "FIVE" , "SIX" , "SEVEN" , "EIGHT" , "NINE" };
}

bool takeOutLetters(std::unordered_map<int,int>& letters, int digit, int copies = 1)
{
    const std::string& str = spellings[ digit ];
    for ( int i = 0 ; i < str.length() ; ++i ) {
        int& count = letters[ str[i] - 'A' ];
        count -= copies;
        if ( count < 0 )
            return false;
    }
    return true;
}

bool recursiveSolve(std::unordered_map<int,int> letters, int nextDigit, std::string& out)
{
//    std::cerr<<__PRETTY_FUNCTION__<<std::endl;
    if ( nextDigit == 10 ) {
        // return true if letters is empty. Return false otherwise.
        for ( auto it = letters.cbegin() ; it != letters.cend() ; ++it )
            if ( it->second != 0 )
                return false;
        return true;
    }

    // how many copies of nextDigit are there?
    int copies = 0;

    // special cases (save time if nextDigit has a unique letter)
    {
        int slot;
        switch ( nextDigit ) {
            case 0:
                slot = 'Z' - 'A';
                copies = letters.count( slot ) ? letters[slot] : 0;
                break;
            case 2:
                slot = 'W' - 'A';
                copies = letters.count( slot ) ? letters[slot] : 0;
                break;
            case 6:
                slot = 'X' - 'A';
                copies = letters.count( slot ) ? letters[slot] : 0;
                break;
            default:
                ;
        }
    }

    if ( !takeOutLetters( letters , nextDigit , copies ) )
        return false;

    while( true ) {
        if ( recursiveSolve( letters , nextDigit+1 , out ) )
            break;
        ++copies;
        if ( !takeOutLetters( letters , nextDigit ) )
            return false;
    }

    // if we're here, then we were able to solve the rest of the problem.
    std::string current( copies , '0' + (char)nextDigit );
    out = current + out;
    return true;
}

int main()
{
    int T;
    std::cin >> T;
    std::string line;

    std::getline( std::cin , line );
    for ( int t = 1 ; t <= T ; ++t ) {
        std::getline( std::cin , line );
//        std::cerr<<"Line is "<<line<<" and line.length() is "<<line.length()<<std::endl;

        std::unordered_map<int,int> letters;
        for ( int i = 0 ; i < line.length() ; ++i ) {
            int slot = line[i] - 'A';
            if ( letters.count( slot ) )
                ++letters[ slot ];
            else
                letters[ slot ] = 1;
        }

        std::string result = "";
        recursiveSolve( letters , 0 , result );

        std::cout << "Case #" << t << ": " << result << '\n';
    }

    return 0;
}
