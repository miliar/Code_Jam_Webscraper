#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

#define debug cout

int lastMinus;
vector<bool> v;

void SetLastMinus()
{
    for (int i = lastMinus; i >= 0; --i)
    {
        if (!v[i])     
        {
            lastMinus = i;
            return;
        }
    }
    
    lastMinus = -1;
}

bool FlipFirstPositives()
{
    bool flipped = false;
    int i = 0;
    
    while (v[i])
    {
        v[i] = false;
        flipped = true;
        i++;
    }
    
    return flipped;
}

void Flip()
{
    reverse(v.begin(), v.begin() + lastMinus + 1);
    
    for (int i = 0; i <= lastMinus; i++)
        v[i] = !v[i];
}

void GenerateVector(string s)
{
    lastMinus = -1;
    v = vector<bool> (s.size(), false);
    
    for(int i = 0; i < s.size(); i++)
        if (s[i] == '+')
            v[i] = true;
        else
            lastMinus = i;
}

void RunInstance()
{
    int count = 0;
    
    string s;
    cin >> s;
    
    GenerateVector(s);
    
    while (lastMinus != -1)
    {
        if (FlipFirstPositives())
            count++;
        Flip();
        count++;
        SetLastMinus();
    }
    
    cout << count;
}

// ============================ Nothing to change here ============================ //

int main() 
{
    int num_of_instances = 0;
    cin >> num_of_instances;
    
    for (int i = 1; i <= num_of_instances; ++i) 
    {
        cout << "Case #" << i << ": ";
        RunInstance();
        cout << endl;
    }
}