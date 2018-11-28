#include <iostream>
#include <string>

int main(int argc, char *argv[])
{
    int input;
    std::cin >> input;

    for( int index(0); index < input; ++index )
    {
        std::string data;
        std::cin >> data;


        if( 1 == data.size() )
        {
            int result(0);
            if( '-' == data[0] )
            {
                result++;
            }

            std::cout << "Case #" << index+1 << ": " << result << std::endl;
            continue;
        }

        int increment(0);
        char previous = data[0];

        int totalSize(data.size());
        for( int inner(1); inner < totalSize; ++inner )
        {
            if( previous != data[inner]  )
            {
                increment++;
            }
            previous = data[inner];

            if ( inner == (totalSize-1) && '-' == data[inner]  )
            {
                increment++;
            }
        }

        std::cout << "Case #" << index+1 << ": " << increment << std::endl;
    }

    std::cin >>input;
}
