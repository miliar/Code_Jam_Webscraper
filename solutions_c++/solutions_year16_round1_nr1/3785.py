#include <iostream>
#include <fstream>
#include <string>
#include <vector>


using namespace std;

int main()
{
    int t;
    ifstream in("in.txt");
    ofstream out("out.txt");
    in>>t;
    string s,ats;
    char z;
    for(int i=0;i<t;i++)
    {
        in>>s;
        ats.push_back(s[0]);
        for(int k=1;k<s.size();k++)
        {
            z=s[k];
            if(s[k]<ats[0])ats.push_back(s[k]);
            else ats.insert(0,1,z);
        }
        out<<"Case #"<<i+1<<": "<<ats<<endl;
        ats.clear();

    }


    return 0;
}
