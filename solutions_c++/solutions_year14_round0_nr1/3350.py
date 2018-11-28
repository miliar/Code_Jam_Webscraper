#include <iostream>
#include <fstream>
#include <vector>
#include <iterator>
#include <algorithm>

int main()
{
    using namespace std;

    ofstream output("output.txt");
    ifstream input("input.txt");

    unsigned int case_count;
    input >> case_count;

    for(unsigned int i = 0; i < case_count; ++i)
    {
        output << "Case #" << i+1 << ": ";

        vector<unsigned int> possible_solutions(4);

        unsigned int row;
        input >> row;

        vector<unsigned int> cards(16);
        copy_n(istream_iterator<unsigned int>(input), 16, cards.begin());
        copy_n(cards.begin()+(row-1)*4, 4, possible_solutions.begin());

        input >> row;
        copy_n(istream_iterator<unsigned int>(input), 16, cards.begin());

        auto solution = find_first_of(cards.begin()+(row-1)*4, cards.begin()+row*4, possible_solutions.begin(), possible_solutions.end());

        if(solution == cards.begin()+row*4)
        {
            output << "Volunteer cheated!";
        }
        else if(find_first_of(solution+1, cards.begin()+row*4, possible_solutions.begin(), possible_solutions.end()) != cards.begin()+row*4)
        {
            output << "Bad magician!";
        }
        else
        {
            output << *solution;
        }

        output << endl;
    }
}
