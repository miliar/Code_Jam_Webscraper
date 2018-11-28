#include <iostream>
#include<string>
#include<fstream>
#include<vector>
using namespace std;

ifstream in;
ofstream out;
int main()
{
    in.open("A-large (1).in");
    int cases;
    in>>cases;
    vector<string> ins;
    vector<string> outs;
    for(int i=0;i<cases;i++)
    {
        string str;
        in>>str;
        ins.push_back(str);
    }
    in.close();
    for(int i=0;i<cases;i++)
    {
        string temp=ins[i];
        string s;
        s=temp[0];
        for(int j=1;j<temp.size();j++)
        {
            if(temp[j]>=s[0])
            {
                s=temp[j]+s;
            }
            else
            {
                s+=temp[j];
            }

        }
        outs.push_back(s);
    }
    out.open("out.txt");
    for(int i=0;i<cases;i++)
    {
        out<<"Case #"<<i+1<<": "<<outs[i]<<endl;
    }

    out.close();
    return 0;
}
