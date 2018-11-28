#include <iostream>
#include <string>

using namespace std;


bool isCorrect(char c,bool rev)
{
    if(c == '+' && rev == false)
        return true;
    else if(c == '+' && rev == true)
        return false;
    else if(c == '-' && rev == false)
        return false;
    else
        return true;
    
}

int getResult(const string &s)
{
    bool rev = false;
    int count = 0;
    for(int i = s.size()-1; i>=0 ; i--)
    {
        if(isCorrect(s[i],rev) == false)
        {
            rev = !rev;
            count ++;
        }
    }
    return count;
}

int main()
{
    int test;
    cin>>test;
    for(int i = 0;i<test;i++)
    {
        string s;
        cin>>s;
        cout<<"Case #"<<i+1<<": "<<getResult(s)<<endl;
    }
}
