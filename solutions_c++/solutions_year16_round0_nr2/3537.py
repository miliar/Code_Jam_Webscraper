#include <fstream>
#include <string.h>

using namespace std;

int count=0;

ifstream fin("input.txt");
ofstream fout("output.txt");

void check(char s[101],int index,char r)
{
    if(index<0)
        return;
    else
    {
        if(s[index] != r)
        {
            count++;

            if(r == '+')
                check(s,index-1,'-');
            else
                check(s,index-1,'+');
        }
        else
            check(s,index-1,r);
    }
}

int main()
{
    int t;
    fin>>t;

    for(int i=1;i<=t;i++)
    {
        char s[101];
        fin>>s;
        check(s,strlen(s)-1,'+');
        fout<<"Case #"<<i<<": "<<count<<endl;
        count=0;
    }

    return 0;
}
