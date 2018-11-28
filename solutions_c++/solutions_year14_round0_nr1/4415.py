#include <vector>
#include <map>
#include <iostream>
#include <string>
/* Obtain Boost Libraries at www.boost.org 
 * You can also install boost on Debian systems using:
 * apt-get install libboost-dev */
#include <boost/tokenizer.hpp>

class TestCase
{
    public:
        
        TestCase(int index, int a1, int a2);
        ~TestCase() { }       
        
        void PopulateGrid(int grid_num, std::vector<std::string>& four_lines);
        void FindSolution();

    private:
        int index_;
        int a1_;
        int a2_;
        int magic_card_num_;
        std::map<int, std::vector<int> > grid1_;
        std::map<int, std::vector<int> > grid2_;
};

inline TestCase::TestCase(int index, int a1, int a2)
{
    index_ = index;
    a1_ = a1-1;
    a2_ = a2-1;
}

inline void TestCase::PopulateGrid(int grid_num, std::vector<std::string>& four_lines)
{
    boost::char_separator<char> sep(" ");
    for (int i=0; i<4; i++)
    {
        if (grid_num == 1)
            grid1_[i] = std::vector<int>();
        else
            grid2_[i] = std::vector<int>();

        boost::tokenizer<boost::char_separator<char>> tokens(four_lines[i], sep);
        int val;
        
        for (const auto& tok: tokens)
        {
            val = atoi(tok.c_str());
            if (grid_num == 1)
                grid1_[i].push_back(val);
            else 
                grid2_[i].push_back(val);
        }
    }
}

/* Naive Solution */
inline void TestCase::FindSolution()
{
    int num_common = 0, card1, card2;
    for (int i=0; i<4; i++)
    {
        card1 = grid1_[a1_][i];
        for (int j=0; j<4; j++)
        {
            card2 = grid2_[a2_][j];
            if (card1 == card2)
            {
                ++num_common;
                magic_card_num_ = card1;
            }
        }
    }

    if (num_common == 1)
    {
       printf("Case #%d: %d\n", index_, magic_card_num_); 
    }else if(num_common == 0)
    {
       printf("Case #%d: Volunteer cheated!\n", index_); 
    }else
    {
       printf("Case #%d: Bad magician!\n", index_); 
    }
}
