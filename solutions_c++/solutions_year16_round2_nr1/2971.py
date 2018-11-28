#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

bool vector_contains(vector<char> jumbled, char c){
    for(int i = 0; i < jumbled.size(); ++i){
        if(jumbled[i] == c){
            return true;
        }
    }
    return false;
}

void vector_contains_erase(vector<char> &jumbled, char c){
    for(int i = 0; i < jumbled.size(); ++i){
        if(jumbled[i] == c){
            jumbled.erase(jumbled.begin() + i);
            return;
        }
    }
}

int removeOcurrences(string word, vector<char> &jumbled, vector<int> &found, int f_index){

    vector<char> v_word;
    for(int i = 0; i < word.length(); ++i){
        v_word.push_back(word[i]);
    }


    bool contains = true;
    while(contains && jumbled.size() > 0){

        /*for(int i = 0; i < jumbled.size(); ++i){
            cout << jumbled[i];
        }
        cout << endl;*/

        for(int i = 0; i < v_word.size() && contains; ++i){
            contains &= vector_contains(jumbled, v_word[i]);
        }
        if(contains){
            found[f_index]++;
            //std::sort(indices.begin(), indices.end(), std::greater<int>());
            /*cout << "jumbled before eraseing " + word + " ";
            for(int j = 0; j < jumbled.size(); ++j){
                cout << jumbled[j];
            }
            cout << endl;*/
            for(int i = 0; i < v_word.size(); ++i){
                vector_contains_erase(jumbled, v_word[i]);
            }
            /*cout << "jumbled after eraseing " + word + " ";
            for(int j = 0; j < jumbled.size(); ++j){
                cout << jumbled[j];
            }
            cout << endl;*/
        }
    }
}

int main()
{
    ifstream input_file;
    input_file.open("A-large.in", ifstream::in);
    ofstream output_file;
    output_file.open("A-large-output.txt", ofstream::out);

    string temp;
    getline(input_file, temp);

    int caso = 1;
    while(getline(input_file, temp)){

        string phone = "";

        vector<char> jumbled;
        for(int i = 0; i < temp.length(); ++i){
            jumbled.push_back(temp[i]);
        }

        vector<int> found;
        for(int i = 0; i < 10; ++i){
            found.push_back(0);
        }

        removeOcurrences("ZERO", jumbled, found, 0);
        removeOcurrences("SIX", jumbled, found, 6);
        removeOcurrences("TWO", jumbled, found, 2);
        removeOcurrences("EIGHT", jumbled, found, 8);
        removeOcurrences("THREE", jumbled, found, 3);
        removeOcurrences("FOUR", jumbled, found, 4);
        removeOcurrences("ONE", jumbled, found, 1);
        removeOcurrences("SEVEN", jumbled, found, 7);
        removeOcurrences("FIVE", jumbled, found, 5);
        removeOcurrences("NINE", jumbled, found, 9);


        for(int i = 0; i < found.size(); ++i){
            for(int j = 0; j < found[i]; ++j){
                phone += std::to_string(i);
            }
        }

        output_file << "Case #" << caso << ": " << phone << endl;
        ++caso;
    }

    input_file.close();
    output_file.close();
    return 0;
}
