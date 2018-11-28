#include <algorithm>
#include <iostream>
#include <set>

int main() {

    std::istream& input(std::cin);
    std::ostream& output(std::cout);

    /*
     * Read the amount of test cases.
     */
    unsigned testCount;
    input >> testCount;

    /**
     * Read each test case:
     * - correct line
     * - 4 lines of 4 cards
     * - correct line
     * - 4 lines of 4 cards
     */
    for (unsigned testCase = 1; testCase <= testCount; ++testCase) {
        std::set<unsigned> cards[2];
        for (unsigned turn = 0; turn < 2; ++turn) {
            unsigned correctLine;
            input >> correctLine;
            for (unsigned line = 1; line <= 4; ++line) {
                for (unsigned column = 1; column <= 4; ++column) {
                    unsigned card;
                    input >> card;
                    if (line == correctLine) {
                        cards[turn].insert(card);
                    }
                }
            }
        }
        std::set<unsigned> answers;
        std::set_intersection(
                cards[0].begin(),
                cards[0].end(),
                cards[1].begin(),
                cards[1].end(),
                std::inserter(answers, answers.end())
        );
        output << "Case #" << testCase << ": ";
        switch (answers.size()) {
            case 0:
                output << "Volunteer cheated!";
                break;
            case 1:
                output << *answers.begin();
                break;
            default:
                output << "Bad magician!";
                break;
        }
        output << std::endl;
    }
}
