#include "../input/gcj-input.h"
#include <vector>
#include <string>
#include <iostream>
#include <set>

using namespace std;

int main(int argc, char const *argv[])
{
    const string filename = argv[1];
    GcjInput in(filename);
    int T = in.read_line_of_ints(1).at(0);

    for (int i=0; i < T; i++){
        size_t guess = in.read_line_of_ints(1)[0];
        set<int> possibilities1;
        set<int> possibilities2;
        vector<vector<int> > layout(4);
        for (int j=0; j< 4; j++)
            layout[j] = in.read_line_of_ints(4);

        for(int card : layout.at(guess-1)){
            possibilities1.insert(card);
        }

        guess = in.read_line_of_ints(1)[0];
        for (int j=0; j< 4; j++)
            layout[j] = in.read_line_of_ints(4);

        for(int card : layout.at(guess-1)){
            possibilities2.insert(card);
        }

        for(int card : possibilities1){
            if(possibilities2.count(card) ==0)
                possibilities1.erase(card);
        }

        cout << "Case #" << i+1 << ": "; 
        if(possibilities1.size() == 0)
            cout << "Volunteer Cheated!" << endl;
        if(possibilities1.size() == 1)
            cout << *possibilities1.begin() << endl;
        if(possibilities1.size() > 1)
            cout << "Bad Magician!" << endl;
    }
    return 0;
}
