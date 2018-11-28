#include <iostream>
#include <cstring>
#include <string>
using namespace std;

bool check(long long, long long);
bool check1(long long, long long);

int ages=0;

long long convert (const char * input)
{
    long long output = 0;
    for (int i=0; input[i] != '\0'; i++)
    {
        output = output*10 + (input[i]-48);
    }
    return output;
}

int main()
{
    int cases, pos;
    long long p , q;
    string input, str1, str2;
    cin >> cases;
    int i = 0;
    while (++i <= cases)
    {
        ages = 0;
        cin >> input;
        pos = input.find('/');
        str1 = input.substr(0,pos);
        str2 = input.substr(pos+1);
        //cout << str1 << str2 << endl;
        p = convert(str1.c_str());
        q = convert(str2.c_str());
        //cout << atoi(str1.c_str()) << endl << atoi(str2.c_str()) << endl;
        //cout << p << endl << q << endl;
        //cin >> p >> q;
        //cout << p << endl << q << endl;
        
        cout << "Case #" << i << ": " ;
        if (check(p,q))
            cout << ages << endl;
        else
            cout << "impossible" << endl;
    }
    return 0;
}



bool check (long long p, long long q)
{
    if (p == q)
        return true;
    if (p > q)
    {
        return check1 (p-q, q);
    }
    else if (q % 2 == 0)
    {
        q = q / 2;
        ages++;
        return check (p, q);
    }
    else 
    {
        return false;
    }
}


bool check1 (long long p, long long q)
{
    if (p == q)
        return true;
    if (p > q)
    {
        return check1 (p-q, q);
    }
    else if (q % 2 == 0)
    {
        q = q / 2;
        return check1 (p, q);
    }
    else 
    {
        return false;
    }
}
