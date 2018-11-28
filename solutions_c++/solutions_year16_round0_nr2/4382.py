#include <iostream>
#include <string>

#define _DBG(x) std::cout << #x << "=[" << x << "]" << std::endl
#define _SHOW(x) std::cout << x << std::endl
#define _FLAG(NAME) std::cout << "FLAG " << #NAME << std::endl

using std::cout;
using std::cin;
using std::endl;
using std::string;

int getInt()
{
    int k;
    cin >> k;
    return k;
}

string getStr()
{
    string  s;  
    cin >> s;
    return s;
}

int getHighestUnhapyID(const string& str)
{
    for (int i = str.size() - 1; i >= 0; i--)
    {   
        if (str.at(i) == '-')
        {
            return i;
        }
    }   
    return -1; 
}

void swapSubStr(string& str, const int maxid)
{
    for (int i = maxid; i >= 0; i--)
    {   
        str[i] = (str.at(i) == '-') ? '+' : '-';
    }   
}

void calc(const int id, const string& str)
{
    int try_count = 0;
    string stack(str);

    int maxid = getHighestUnhapyID(stack);
    while (maxid >= 0)
    {   
        try_count++;
        swapSubStr(stack, maxid);
        maxid = getHighestUnhapyID(stack);
    }   

    cout << "Case #" << id << ": " << try_count << endl;
}

int main(int argc, char** argv)
{
    const int cases = getInt();
    for (int i = 0; i < cases; i++)
    {   
        calc(i+1, getStr());
    }   
    return 0;
}