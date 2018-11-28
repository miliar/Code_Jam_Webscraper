
#include <iostream>
#include <unordered_set>
#include <string>

template<class T>
void dumpset(std::unordered_set<T> set)
{
    for ( auto it = set.cbegin() ; it != set.cend() ; ++it )
        std::cerr<<*it<<" ";
    std::cerr<<std::endl;
}

int main()
{
    int T;
    std::cin >> T;

    for ( int t = 1 ; t <= T ; ++t ) {
        std::cout << "Case #" << t << ": ";
        int N;
        std::cin >> N;

        if ( N == 0 ) {
            std::cout << "INSOMNIA" << '\n';
            continue;
        }

        std::unordered_set<int> digits;
        for ( int i = 0 ; i < 10 ; ++i )
            digits.insert( i );

        int curr = 0;

        while ( !digits.empty() ) {
            curr += N;
            std::string str = std::to_string( (long long)curr );
            auto it = digits.cbegin();
            while ( it != digits.cend() ) {
//                char currchar = *it - '0';
//                std::cout<<"currchar = "<<currchar<<std::endl;
                if ( str.find( (char)(*it + '0') ) != -1 )
                    it = digits.erase( it );
                else
                    ++it;
            }
//            std::cerr<<"curr = "<<curr << std::endl;
//            dumpset( digits );
//            if ( curr > 10 )
//                exit(1);
        }

        std::cout << curr << '\n';
    }

    return 0;
}
