#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

const string digits[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
const string digChar[10] = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"};


// s = sorted string
bool lettersIn(int digit, string s)
{
    string d = digits[digit];
    sort(d.begin(), d.end());

    int j = 0;
    for(int i = 0 ; i < s.size() ; i++)
    {
        if(d[j] == s[i])
            j++;

        if(j == d.size())
            return true;
    }

    return false;
}

string removeDigit(int digit, string s)
{
    string d = digits[digit];
    sort(d.begin(), d.end());
    string newString = "";

    int j = 0;
    for(int i = 0 ; i < s.size() ; i++)
    {
        if(j != d.size() && d[j] == s[i])
            j++;
        else
            newString += s[i];
    }

    return newString;
}

std::pair<bool, string> findPhoneNb(string s, int minDigit)
{
    for(int i = minDigit ; i <= 9 ; i++)
    {
        if(lettersIn(i, s))
        {
            string newS = removeDigit(i, s);
            if(newS.empty())
                return std::pair<bool, string>(true, digChar[i]);

            pair<bool, string> p = findPhoneNb(removeDigit(i, s), i);
            if(p.first)
            {
                return pair<bool, string>(true, digChar[i] + p.second);
            }
        }
    }

    return pair<bool, string>(false, "");
}

int main(int argc, char** argv)
{
    ifstream file(argv[1]);
    ofstream output(argv[2]);

    if(!file)
        return -1;

    int T = 0;

    file >> T;

    for(int i = 0 ; i < T ; i++)
    {
        string S;
        file >> S;

        sort(S.begin(), S.end());
        
        output << "Case #" << i+1 << ": " << findPhoneNb(S, 0).second << endl;
    }

    file.close();
    output.close();

    return 0;
}