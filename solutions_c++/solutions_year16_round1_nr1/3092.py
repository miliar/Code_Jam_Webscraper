#include <iostream>
#include <string>
using namespace std;

int main()
{
    int test;
    cin>>test;
    for(int i=1;i<=test;i++)
    {
        string s;
        cin>>s;
        string output;
        for(int j = 0;j<s.size();j++)
        {
            string tmp;
            tmp.push_back(s[j]);
            if(output[0] <= tmp[0])
            {
                output = tmp + output;
            }
            else
            {
                output = output +tmp;
            }
        }
        cout<<"Case #"<<i<<": "<<output<<endl;
    }
    return 0;
}
