#include <iostream>
#include <string>

using namespace std;

int findMinFlips(string& input)
{
    int len = input.length();
    char c = input[0];
    int flips = 0;
    for(int i = 1; i < len; i++)
    {
        if(input[i] != c)
        {
            c = input[i];
            flips++;
        }
    }

    if(input[len - 1] == '-')
        flips++;

    return flips;
}

int main()
{
    int t;
    string input;
    cin>>t;
    for(int i = 1; i <= t; i++)
    {
        cin>>input;
        cout<<"Case #"<<i<<": "<<findMinFlips(input)<<endl;
    }
    return 0;
}
