#include <iostream>
#include <string>

using namespace std;


///////////////////////////////////////////////////////////////////////////////////////////////////

void result()
{

    string s, s1;
    char ch;

    cin >> s;

    ch = s[0];

    s1 = s[0];

    for(int i=1; i < s.length(); i++)
    {
        if(s[i] >= s1[0])
            s1 = s[i] + s1;
        else
            s1 = s1 + s[i];

       // ch = s[i];
    }

    cout << s1;



}

///////////////////////////////////////////////////////////////////////////////////////////////////

int main()
{
    int test, i = 1;

    cin >> test;

    while(test--)
    {
        cout << "case #"<< i++ <<": ";

        result();

        cout << endl;
    }

return 0;
}

