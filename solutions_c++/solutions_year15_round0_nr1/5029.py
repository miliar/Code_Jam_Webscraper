#include <fstream>

using namespace std;

const char InFile[]="input.in";
const char OutFile[]="output.out";
const int MAXS=1024;

ifstream fin(InFile);
ofstream fout(OutFile);

int T,Smax;
char str[MAXS];

int main()
{
    fin>>T;
    for(int test=1;test<=T;++test)
    {
        int sol=0;
        fin>>Smax;
        fin>>str;
        int curr=0;
        for(int i=0;i<=Smax;++i)
        {
            if(i<=curr)
            {
                curr+=str[i]-'0';
            }
            else if(str[i]!='0')
            {
                sol+=i-curr;
                curr=i;
                curr+=str[i]-'0';
            }
        }
        fout<<"Case #"<<test<<": "<<sol<<"\n";
    }
    fin.close();
    fout.close();
    return 0;
}
