// Example program
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;
int main()
{
    ifstream input;
    input.open("lastWord-input.txt");
    ofstream output;
    output.open("last-word-output.txt");
    vector<string> wordsProduced,toPush;
    string word,dummy_front,dummy_back,currentWord;
    int cases,currentCases = 1;
    input>>cases;
    while(currentCases <= cases){
        input >> word;
        wordsProduced.clear();
        wordsProduced.push_back(word);
        wordsProduced[0] = word[0];
        for(int i = 1; i < word.length(); i++){
                int j = 0;
            for(; j < wordsProduced.size(); j++){    
                   currentWord = wordsProduced[j];    
                   //wordsProduced.erase(wordsProduced.begin(),wordsProduced.begin() + j);
                   //cout<<"Current: " << currentWord<<endl;             
                   dummy_front = currentWord + word[i];
                   dummy_back = word[i] + currentWord;
                   toPush.push_back(dummy_front);
                   toPush.push_back(dummy_back);
                   
            }
            wordsProduced.erase(wordsProduced.begin(),wordsProduced.begin() + j);
            for(int j = 0; j < toPush.size(); j++){
                wordsProduced.push_back(toPush[j]);   
            }
            toPush.clear();
        }
        sort(wordsProduced.begin(),wordsProduced.end());
        output<<"Case #"<<currentCases<<": "<<wordsProduced[wordsProduced.size()-1]<<endl;
        /*
        for(int i = 0;i<wordsProduced.size();i++){
           cout<<wordsProduced[i]<<endl;   
        }
        */
        currentCases++;
    }
}