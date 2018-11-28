#include <iostream>
#include <cmath>
#include <vector>
#include <iomanip>
#include <string>
#include <climits>

using namespace std;

void formatStr(string & in)
{
    char last = '0';
    for(int i = 0; i  < in.size(); i++)
    {
        if(last == in.at(i))
        {
            in.erase(i,1);
            i--;
        }
        last = in.at(i);
    }
    while(in.back() == '+')
    {
        in.pop_back();
    }

}

int main()
{
    long long times;
    cin >> times;
    string in;
    for(long long i = 1; i <= times; i++)
    {
        cin >> in;
        formatStr(in);
        cout << "Case #" << i << ": " << in.size() << endl;
    }

}
