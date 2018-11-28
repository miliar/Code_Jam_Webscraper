#include <iostream>
#include <fstream>
#include <deque>
using namespace std;

int main()
{
    ifstream input;
    input.open("A-large.in");
    ofstream output;
    output.open("out.txt");
    int n;
    input>>n;
    for(int i=1;i<=n;i++)
    {
        string s;
        input>>s;

        deque<char> m;
        m.push_front(s[0]);
        for(int j=1;j<(int)s.length();j++)
        {
            //cout<<"I="<<i<<"---"<<"s[i]"<<s[j]<<endl;
            if(s[j] >= m.front())
                m.push_front(s[j]);
            else
                m.push_back(s[j]);

        }
        output<<"Case #"<<i<<": ";
        for(auto it = m.begin() ; it!=m.end() ; ++it)
            output<<*it;
        output<<endl;

    }
    return 0;
}
