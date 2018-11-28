#include <iostream>

#define _DBG(x) std::cout << #x << "=[" << x << "]" << std::endl
#define _SHOW(x) std::cout << x << std::endl

using std::cout;
using std::cin;
using std::endl;

int getInt()
{
    int k;
    cin >> k;
    return k;
}

bool digits[10];

bool isDone()
{
    for (int i = 0; i < 10; i++)
    {   
        if (!digits[i])
        {
            return false;
        }
    }   
    return true;
}

void parseN(int N)
{
    while (N >= 10) 
    {   
        digits[N%10] = true;
        N/=10;
    }   
    digits[N] = true;
}

void calc(const int id, const int N)
{
    if (N == 0)
    {   
        _SHOW("Case #" << id << ": " << "INSOMNIA");
        return;
    }   
    for (bool& b : digits)
    {   
        b = false;
    }   
    int itr = 0;
    int named;
    while (!isDone())
    {   
        itr++;
        named = N*itr;
        parseN(named);
    }   
    _SHOW("Case #" << id << ": " << named);
}

int main(int argc, char** argv)
{
    const int cases = getInt();
    for (int i = 0; i < cases; i++)
    {   
        calc(i+1, getInt());
    }   
    return 0;
}
