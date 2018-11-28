//
//  main.cpp
//  Round1A1
//
//  Created by Oleksandr Loyko on 4/15/16.
//  Copyright © 2016 Oleksandr Loyko. All rights reserved.
//

#include <iostream>
#include <vector>
#include <stack>
#include <string>
#include <fstream>
#include <iterator>
#include <list>
using namespace std;

string win_word(string or_word);

int main(int argc, const char * argv[]) {
    
    ifstream input("input.in");
    ofstream output;
    output.open("output.out");
    int case_n;
    input >> case_n;
    string empty;
    getline(input, empty);
    string word;
    
    for(int i = 1; i <= case_n; i++)
    {
        getline(input,word);
        output << "Case #" << i << ": " << win_word(word) << endl;
        
        
    }
    
    input.close();
    output.close();
    return 0;
}

string win_word(string or_word)
{
    std::list <char> letters;
    letters.push_back(or_word[0]);
    
    for(int i = 1; i < or_word.length(); i++)
    {
        if(or_word[i] < *(letters.begin()))
            letters.push_back(or_word[i]);
        else
            letters.push_front(or_word[i]);
    }
    string winner;
    auto temp = letters.begin();
    while(temp!=letters.end())
    {
        winner = winner + *temp;
        ++temp;
    }
    return winner;
    
    

}

