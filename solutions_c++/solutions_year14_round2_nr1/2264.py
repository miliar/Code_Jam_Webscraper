#include <iostream>
#include <algorithm>
#include <cmath>
#include <fstream>
#include <string>
#include <iomanip>
#include <map>
using namespace std;
typedef long long int LL;

//#define fin cin
//#define fout cout
int main()
{
    ios_base::sync_with_stdio(0);
    ifstream fin("A-small-attempt2.in");
    ofstream fout("A-small-attempt2.out");
    int t;
    fin>>t;
    for(int n=1; n<=t; ++n)
    {
        int l;
        string s1,s2;
        fin>>l;
        fin>>s1>>s2;
        int id1=0,id2=0;
        bool chk=true,chk2=true;
        char ch;
        int ans=0;
        while(id1<s1.size()||id2<s2.size())
        {
            if(s1[id1]==s2[id2])
            {
                ch=s1[id1];
                id1++;
                id2++;
                chk=false;
            }
            else if(!chk&&s1[id1]==ch)
            {
                while(s1[id1]==ch)
                {
                    ans++;
                    id1++;
                }
                chk=true;
            }
            else if(!chk&&s2[id2]==ch)
            {
                while(s2[id2]==ch)
                {
                    ans++;
                    id2++;
                }
                chk=true;
            }
            else
            {
                chk2=false;
                break;
            }
            //fout<<s1[id1]<<" "<<s2[id2]<<" "<<ch<<endl;
        }

        if(!chk2)fout<<"Case #"<<n<<": Fegla Won"<<endl;
        else fout<<"Case #"<<n<<": "<<ans<<endl;
    }
    return 0;
}
