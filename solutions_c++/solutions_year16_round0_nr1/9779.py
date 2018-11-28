#include <stdio.h>
#include <iostream>
#include <sstream>
#include <string>
#include <set>

int main(int argc, char *argv[])
{
    int input;
    std::cin >> input;

    for( int index(0); index < input; ++index )
    {
        int data;
        std::cin >> data;

        if( 0 == data || data >= 1000000 )
        {
            std::cout << "Case #" << index+1 << ": INSOMNIA" << std::endl;
            continue;
        }

        int increment(1);

        std::set<char> shipset;

        do
        {
            int local( data * increment );
            std::stringstream stream;
            stream << local;
            std::string str( stream.str() );

            shipset.insert(str.begin(), str.end());

            std::set<char>::iterator itr = shipset.begin();

            if( 10 ==  shipset.size() )
            {
                std::cout << "Case #" << index+1 << ": " << local << std::endl;
            }
            std::cout.flush();
            ++increment;
        }while( shipset.size() != 10 );

    }
}
