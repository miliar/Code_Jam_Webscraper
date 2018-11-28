#include<iostream>
#include<vector>
#include<fstream>
#include<string>
#include<algorithm>
#include<cstdlib>

using namespace std;

string getNumber(string s, ostream & fout); //returns actual phone number
void printVec(vector<int> vec);
bool contains(vector<int> &occur, string num); //returns true if numbers has at least one of each letter in num. also decrements the counts



int main()
{
    ifstream fin("A-large.in");
    int n = 0;
    fin >> n;
    cout << "There are " << n << " test cases" << endl;
    ofstream fout("output.txt");
    string number = "";
    for(int i = 0; i < n; i++)
    {
        fout << "Case #" << i + 1 << ": ";
        fin >> number;
        getNumber(number, fout);
    }
    return 0;
}

string getNumber(string s, ostream & fout)
{
    string actualDigits = "";
    vector<int> digits;
    vector<int> occur(26, 0);

    for(int i = 0; i < s.size(); i++)
    {
        occur[s[i] - 65]++; //increments the occurrence of some letter
    }
    vector<string> written = {"ZERO", "SIX", "TWO", "EIGHT", "SEVEN", "FIVE", "FOUR", "ONE", "THREE", "NINE"};
    vector<int> convert = {0, 6, 2, 8, 7, 5, 4, 1, 3, 9};
    for(int i = 0; i < 10; i++)
    {
        while(contains(occur, written[i]))
        {
            digits.push_back(convert[i]);
        }
    }
    //cout << "digits are: ";
    sort(digits.begin(), digits.end());
    //printVec(digits);
    vector<char> digs = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
    for(int i = 0; i < digits.size(); i++)
    {
        fout << digs[digits[i]];
    }
    fout << endl;
    return actualDigits;
}

void printVec(vector<int> vec)
{
    for(int i = 0; i < vec.size(); i++)
    {
        cout << vec[i] << " ";
    }
    cout << endl;
}

bool contains(vector<int> &occur, string num)
{
    vector<int> temp = occur;
    bool isIn = true;
    for(int i = 0; i < num.size(); i++)
    {
        if(temp[num[i] - 65] == 0)
        {
            return false;
        }
        temp[num[i] - 65] --;
    }
    for(int i = 0; i < num.size(); i++)
    {
        occur[num[i] - 65]--;
    }
}
