//
//  main.cpp
//  magic_trick
//
//  Created by Vagelis Nonas on 4/12/14.
//
//

#include <iostream>
#include <vector>
#include <sstream>
#include <string>



#define SQUARE_SIZE 4


long read_square(long which_row,std::vector<long> &cards_in_row) {
    for (int i=0;i<SQUARE_SIZE;i++) {
        for (int j=0;j<SQUARE_SIZE;j++) {
            long card;
            std::cin >> card;
            if (i+1 == which_row)
                cards_in_row.push_back(card);
        }
    }
    return cards_in_row.size();
}


int main(int argc, const char * argv[])
{
    try {
        int test_cases=0;
        std::cin >> test_cases;
        for (int i=0;i<test_cases;i++) {
            long row1 = -1, row2 = -1;
            std::vector<long> choice1,choice2;
            std::cin >> row1;
            read_square(row1, choice1);
            std::cin >> row2;
            read_square(row2, choice2);
            long common=0, solution=0;
            for (std::vector<long>::iterator it1=choice1.begin();it1!=choice1.end();++it1)
                for (std::vector<long>::iterator it2=choice2.begin();it2!=choice2.end();++it2)
                    if (*it1 == *it2) {
                        common++;
                        solution = *it1;
                    }
            if (common == 1)
                std::cout << "Case #" << i+1 << ": " << solution << std::endl;
            else if (common == 0)
                std::cout << "Case #" << i+1 << ": Volunteer cheated!" << std::endl;
            else if (common>0)
                std::cout << "Case #" << i+1 << ": Bad magician!" << std::endl;
            else {
                //Invalid
            }
        }
    } catch (const char * e) {
        std::cout << e;
    } catch (std::exception& e) {
        std::cout << e.what();
    }
}

