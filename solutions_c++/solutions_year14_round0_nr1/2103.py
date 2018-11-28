
#include <iostream>
#include <string>
#include <vector>

#include <stdlib.h>

char CASE[] = "CASE #";
char BAD_STR[] = "Bad magician!";
char CHEET_STR[] = "Volunteer cheated!";

std::vector<int> read_line()
{
    int index = 0;
    int prev  = 0;

    std::string line;
    std::vector<int> values;
    std::getline( std::cin, line );

    while( std::string::npos != index )
    {
        int size = 0;
        index = line.find( " ", prev );
        if( std::string::npos != index ) {
            size = index - prev;
        }
        else {
            size = index;
        }
        std::string tmp_string = line.substr( prev, size );
        values.push_back( atoi( tmp_string.c_str() ) );
        if( std::string::npos == index )
        {
            break;
        }
        prev = index+1;
    }

    return values;
}

int main()
{
    std::vector<int> tmp;
    int case_num = 0;

    tmp = read_line();
    case_num = tmp[0];

    for( int i = 0; i < case_num; i++ )//SET Any
    {
        int answer[2];
        int result = 0;
        std::vector< std::vector< std::vector<int> > > cards;
        for( int j = 0; j < 2; j++ )
        {
            std::vector< std::vector<int> > tmp_card;
            tmp = read_line();
            answer[j] = tmp[0] - 1;

            for( int k = 0; k < 4; k++ )
            {
                tmp = read_line();
                tmp_card.push_back(tmp);
            }
            cards.push_back( tmp_card );
        }

        std::vector<int>::iterator it;
        std::vector<int>::iterator rit;

        for( it = cards[0][answer[0]].begin(); it != cards[0][answer[0]].end(); ++it ) {
            for( rit = cards[1][answer[1]].begin(); rit != cards[1][answer[1]].end(); ++rit ) {
                if( *rit == *it )
                {
                    if( 0 == result )
                    {
                        result = *it;
                    }
                    else
                    {
                        goto BAD;
                    }
                    break;
                }
            }
        }

        if( 0 == result ){
            std::cout << CASE << (i+1) << ": " << CHEET_STR << std::endl;
        }
        else {
            std::cout << CASE << (i+1) << ": " << result << std::endl;
        }

        continue;
BAD:
        std::cout << CASE << (i+1) << ": " << BAD_STR << std::endl;

    }
   

}

