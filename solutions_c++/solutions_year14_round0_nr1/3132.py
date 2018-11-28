#include <iostream>

using namespace std;

int main()
{
    uint64_t T;
    cin >> T;

    uint64_t first_answer;
    uint64_t second_answer;

    uint64_t first_pattern[4][4];
    uint64_t second_pattern[4][4];

    for(uint64_t i=0; i<T; ++i)
    {
        cin >> first_answer;
        for(uint64_t j=0;j<4;++j)
        {
            for(uint64_t k=0;k<4;++k)
            {
                cin >> first_pattern[j][k];
            }
        }
        cin >> second_answer;
        for(uint64_t j=0;j<4;++j)
        {
            for(uint64_t k=0;k<4;++k)
            {
                cin >> second_pattern[j][k];
            }
        }

        // Check if one of the cards present in the row of first_pattern denoted by
        // first_answer is present in the row of second_pattern denoted by second_row

        uint64_t num_matching = 0;
        uint64_t matching_num = 0;

        for(uint64_t j=0;j<4;++j)
        {
            for(uint64_t k=0;k<4;++k)
            {
                if(first_pattern[first_answer-1][j] == second_pattern[second_answer-1][k])
                {
                    num_matching++;
                    matching_num = first_pattern[first_answer-1][j];
                    break;
                }
            }
        }

        if(num_matching == 1)
        {
            cout << "Case #" << (i+1) << ": " << matching_num << "\n";
        }
        else if(num_matching > 1)
        {
            cout << "Case #" << (i+1) << ": " << "Bad magician!\n";
        }
        else
        {
            cout << "Case #" << (i+1) << ": " << "Volunteer cheated!\n";
        }
    }

    return 0;
}
