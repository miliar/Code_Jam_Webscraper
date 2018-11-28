#include <iostream>
#include <fstream>
#include <string>

using namespace std;

string solve(string word)
{
    string last_word, tmp;

    last_word.append(word, 0, 1);

    for(string::size_type i = 1; i < word.length(); i++)
    {
        if(word[i] < last_word[0]) last_word.append(word, i, 1);
        else last_word.insert(last_word.begin(), word[i]);
    }

    return last_word;
}

int main(int argc, char *argv[])
{
    ifstream file_input("A-large.in", ios::in);
    ofstream file_output("A-large(answer).in", ios::trunc | ios::out);

    if(!file_input || !file_output)
    {
        cerr << "Error : Cannot open the files !" << endl;
        return -1;
    }

    int cases, test;
    string word;
    file_input >> cases;

    for(test = 1; test <= cases; test++)
    {
        file_input >> word;
        file_output << "Case #" << test << ": " << solve(word) << "\n";
    }

    file_input.close();
    file_output.close();

    return 0;
}
