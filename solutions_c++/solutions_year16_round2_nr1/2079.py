#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <fstream>
using namespace std;

string getNumber(vector<int> letters)
{
    vector<char> ans;
    if(letters['Z'-'A']>=1)
    {
        while(letters['Z'-'A']>=1)
        {
        ans.push_back('0');
            letters['Z'-'A']--;
            letters['E'-'A']--;
            letters['R'-'A']--;
            letters['O'-'A']--;
        }

    }
    if(letters['X'-'A']>=1)
    {
    while(letters['X'-'A']>=1)
        {
        ans.push_back('6');
            letters['S'-'A']--;
            letters['I'-'A']--;
            letters['X'-'A']--;
        }

    }
    if(letters['G'-'A']>=1)
    {
        while(letters['G'-'A']>=1)
        {
        ans.push_back('8');
            letters['E'-'A']--;
            letters['I'-'A']--;
            letters['G'-'A']--;
            letters['H'-'A']--;
            letters['T'-'A']--;
        }

    }
    if(letters['U'-'A']>=1)
    {
        while(letters['U'-'A']>=1)
        {
        ans.push_back('4');
            letters['F'-'A']--;
            letters['O'-'A']--;
            letters['U'-'A']--;
            letters['R'-'A']--;
        }

    }
    if(letters['F'-'A']>=1)
    {
        while(letters['F'-'A']>=1)
        {
        ans.push_back('5');
            letters['F'-'A']--;
            letters['I'-'A']--;
            letters['V'-'A']--;
            letters['E'-'A']--;
        }

    }
    if(letters['W'-'A']>=1)
    {
        while(letters['W'-'A']>=1)
        {
        ans.push_back('2');
            letters['T'-'A']--;
            letters['W'-'A']--;
            letters['O'-'A']--;
        }

    }
    if(letters['V'-'A']>=1)
    {
        while(letters['V'-'A']>=1)
        {
        ans.push_back('7');
            letters['S'-'A']--;
            letters['V'-'A']--;
            letters['E'-'A']--;
            letters['E'-'A']--;
            letters['N'-'A']--;
        }

    }
    if(letters['I'-'A']>=1)
    {
        while(letters['I'-'A']>=1)
        {
        ans.push_back('9');
            letters['N'-'A']--;
            letters['I'-'A']--;
            letters['N'-'A']--;
            letters['E'-'A']--;
        }

    }
    if(letters['N'-'A']>=1)
    {
        while(letters['N'-'A']>=1)
        {
        ans.push_back('1');
            letters['O'-'A']--;
            letters['N'-'A']--;
            letters['E'-'A']--;

        }

    }
    if(letters['T'-'A']>=1)
    {
        while(letters['T'-'A']>=1)
        {
        ans.push_back('3');
            letters['T'-'A']--;
            letters['H'-'A']--;
            letters['R'-'A']--;
            letters['E'-'A']--;
            letters['E'-'A']--;
        }

    }
    string s;
    sort(ans.begin(),ans.end());
    for(int i=0;i<ans.size();i++)
    {
        s+=ans[i];
    }
    return s;
}

int main()
{
string line;
  ifstream myfile ("input.txt");
ofstream cout;
  cout.open ("output.txt");
int test;
    myfile>>test;
    string s;
    for(int i=1;i<=test;i++)
    {
        vector<int > letters(26,0);
        myfile>>s;
        for(int j=0;j<s.length();j++)
        {
            letters[s[j]-'A']++;
        }
        cout<<"Case #"<<i<<": "<<getNumber(letters)<<endl;
    }
    cout.close();
    return 0;
}
