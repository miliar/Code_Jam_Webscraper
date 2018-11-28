#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>

using namespace std;

int storer[33];
vector<int> result;

void two()
{
    while(storer['W'-'A'])
    {
        storer['W'-'A']--;
        storer['T'-'A']--;
        storer['O'-'A']--;
        
        result.push_back(2);
    }
}

void six()
{
    while(storer['X'-'A'])
    {
        storer['X'-'A']--;
        storer['S'-'A']--;
        storer['I'-'A']--;
        
        result.push_back(6);
    }
}

void eight()
{
    while(storer['G'-'A'])
    {
        storer['G'-'A']--;
        storer['E'-'A']--;
        storer['I'-'A']--;
        storer['H'-'A']--;
        storer['T'-'A']--;
        
        result.push_back(8);
    }
}

void zero()
{
    while(storer['Z'-'A'])
    {
        storer['Z'-'A']--;
        storer['E'-'A']--;
        storer['R'-'A']--;
        storer['O'-'A']--;
        
        result.push_back(0);
    }
}

void three()
{
    while(storer['H'-'A'])
    {
        storer['H'-'A']--;
        storer['T'-'A']--;
        storer['R'-'A']--;
        storer['E'-'A']-= 2;
        
        result.push_back(3);
    }
}

void four()
{
    while(storer['R'-'A'])
    {
        storer['R'-'A']--;
        storer['F'-'A']--;
        storer['O'-'A']--;
        storer['U'-'A']--;
        
        result.push_back(4);
    }
}

void one()
{
    string h = "ONE";
    while(storer['O'-'A'])
    {
        for(int i=0; i<h.size(); i++)
        {
            storer[h[i] - 'A']--;
        }
        
        result.push_back(1);
    }
}

void five()
{
    string h = "FIVE";
    while(storer['F'-'A'])
    {
        for(int i=0; i<h.size(); i++)
        {
            storer[h[i] - 'A']--;
        }
        
        result.push_back(5);
    }
}

void seven()
{
    string h = "SEVEN";
    while(storer['V'-'A'])
    {
        for(int i=0; i<h.size(); i++)
        {
            storer[h[i] - 'A']--;
        }
        
        result.push_back(7);
    }
}

void nine()
{
    string h = "NINE";
    while(storer['N'-'A'])
    {
        for(int i=0; i<h.size(); i++)
        {
            storer[h[i] - 'A']--;
        }
        
        result.push_back(9);
    }
}

void klir()
{
    result.clear();
    memset(storer, 0, sizeof(storer) );
}

int main()
{
    int testy;
    cin>>testy;
    
    for(int x = 1; x <= testy; x++)
    {
        string s;
        cin>>s;
        
        klir();
        
        for(int i=0; i<s.size(); i++)
        {
            storer[s[i]-'A']++;
        }
        
        two();
        six();
        eight();
        zero();
        three();
        four();
        one();
        five();
        seven();
        nine();
        
        sort(result.begin(), result.end() );
        cout<<"Case #"<<x<<": ";
        for(int i=0; i<result.size(); i++)
        {
            cout<<result[i];
        }
        cout<<"\n";
    }
    
    return 0;
}