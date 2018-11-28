#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream in("read.txt");
    ofstream out("out.txt");
    int i;
    int t;
    //cin>>t;
    int T=1;
    in>>t;
    char ch;
    while(t--)
    {
        string s;
    string s1;

        //cin>>s;
        in>>s;
        s1+=s[0];
        int j=0;
        for(i=1;i<s.length();i++)
        {
            ch=s[i];
            if(ch>=s1[0])
            {
                s1=ch+s1;
            }
            else
            {
                s1=s1+ch;
            }
        }
        out<<"Case #"<<T++<<": "<<s1<<"\n";
    }
    return 0;
}
