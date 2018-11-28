#include <iostream>
#include <string>

using namespace std;

string lastWord(string& input)
{
    int len = input.length();
    string output;
    output.push_back(input[0]);
    for(int i = 1; i < len; i++)
    {
        if(input[i] >= output[0])
            output.insert(output.begin(), input[i]);
        else
            output.push_back(input[i]);
    }

    return output;
}

int main()
{
    int t;
    string s;
    cin>>t;
    for(int i = 1; i <= t; i++)
    {
        cin>>s;
        cout<<"Case #"<<i<<": "<<lastWord(s)<<endl;
    }

    return 0;
}
