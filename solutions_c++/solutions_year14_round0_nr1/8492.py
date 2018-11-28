/* 
 * File:   main.cpp
 * Author: Peter
 *
 * Created on 12 april 2014, 13:01
 */

#include <cstdlib>
#include <iostream>
#include <set>
using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    int number;
    std::cin >> number;
    
    for(int i=0; i<number; i++)
    {
        set<int> numbers;
        int row;
        std::cin >> row;
        for(int j=0; j<4; j++)
        {
            int card;
            for(int k=0; k<4; k++)
            {
                std::cin >> card;
                if(row-1==j)
                    numbers.insert(card);
            }
        }
        std::cin >> row;
        int answer;
        int nrofanswers=0;
        for(int j=0; j<4; j++)
        {
            int card;
            for(int k=0; k<4; k++)
            {
                std::cin >> card;
                if(row-1==j)
                {
                    if(numbers.find(card)!=numbers.end())
                    {
                        answer=card;
                        nrofanswers++;
                    }
                }
                    
            }
        }
        std::cout << "Case #" << i+1 << ": ";
        if(nrofanswers==0)
        {
            std::cout << "Volunteer cheated!" << std::endl;
        }
        else if(nrofanswers==1)
        {
            std::cout << answer << std::endl;
        }
        else
        {
            std::cout << "Bad magician!" << std::endl;
        }
    }
    return 0;
}

