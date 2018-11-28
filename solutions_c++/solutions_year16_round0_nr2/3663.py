#include <iostream>
#include <fstream>

using namespace std;


int main()
{
    int t;
    string s;
    ifstream in("in.txt");
    ofstream out("out.txt");
    in>>t;
    int flips;
    flips=0;
    for(int p=1;p<=t;p++)
    {
in>>s;
for(int i=s.size()-1;i>=0;i--)
{

    if(s[i]=='-')
    {
        flips++;
        for(int k=0;k<=i;k++){if(s[k]=='-')s[k]='+';else s[k]='-';}
    }
}
out<<"Case #"<<p<<": "<<flips<<endl;
flips=0;
s.clear();
    }
    return 0;
}
