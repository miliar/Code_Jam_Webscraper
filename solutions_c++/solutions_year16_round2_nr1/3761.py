#include <iostream>
#include <vector>
#include <string> 
#include <algorithm>
using namespace std;

string phoneNumber(vector<int>& letterCounts, int digitToCheck, vector<vector<int> >& digitCountsInWords)
{
    if(digitToCheck == 10)
    {
        for(int i = 0; i < 26; i++)
        {
            if(letterCounts[i])
                return "ERROR";
        }
        return "";
    }
    string output;
    bool digitExists = true;
    for(int i = 0; i < 26; i++)
    {
        if(letterCounts[i] < digitCountsInWords[digitToCheck][i])
        {
            digitExists = false;
            break;
        }
    }

    if(!digitExists)
        return phoneNumber(letterCounts, digitToCheck + 1, digitCountsInWords);

    for(int i = 0; i < 26; i++)
    {
        letterCounts[i] -= digitCountsInWords[digitToCheck][i];
    }

    output = phoneNumber(letterCounts, digitToCheck, digitCountsInWords);
    if(output != "ERROR")
    {
        output.push_back(digitToCheck + '0');
        return output;
    }

    for(int i = 0; i < 26; i++)
    {
        letterCounts[i] += digitCountsInWords[digitToCheck][i];
    }
    
    return phoneNumber(letterCounts, digitToCheck + 1, digitCountsInWords);
}

int main()
{
    string digitToWordMap[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
    vector<vector<int> > digitCountsInWords(10);
    for(int i = 0; i < 10; i++)
    {
        digitCountsInWords[i].resize(26);
        string word = digitToWordMap[i];

        for(int j = 0; j < word.length(); j++)
        {
            digitCountsInWords[i][word[j] - 'A']++;
        }
    }

    int t;
    cin>>t;
    for(int i = 1; i <= t; i++)
    {
        string input;
        cin>>input;

        vector<int> letterCounts(26);
        for(int j = 0; j < input.length(); j++)
        {
            letterCounts[input[j] - 'A']++;
        }

        string output = phoneNumber(letterCounts, 0, digitCountsInWords);
        reverse(output.begin(), output.end());
        cout<<"Case #"<<i<<": "<<output<<endl;
    }

    return 0;
}
