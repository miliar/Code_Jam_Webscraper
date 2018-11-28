#include <iostream>
#include <cstring>
#include <fstream>
#define filein "A-large.in"
#define fileout "output.txt"
using namespace std;

int s1[4][4],s2[4][4];
char s[4][4];
bool is ();
bool is()
{
    int n;
    for (int i=0;i<4;i++)
    {
        n=0;
        for (int o=0;o<4;o++)
        {
            if (s1[i][o]==1)
            n++;
        }
        if (n==4)
        return true ;
    }
    for (int i=0;i<4;i++)
    {
        n=0;
        for (int o=0;o<4;o++)
        {
            if (s1[o][i]==1)
            n++;
        }
        if (n==4)
        return true ;
    }
    if (s1[0][0]==1&&s1[1][1]==1&&s1[2][2]==1&&s1[3][3]==1)
        return true ;
    if (s1[0][3]==1&&s1[1][2]==1&&s1[2][1]==1&&s1[3][0]==1)
        return true ;
        return false ;
}
int main ()
{
    ifstream input;
    ofstream output;
    input.open(filein);
    output.open(fileout);
    int a=0;
    int t;
    input>>t;
    while (t--)
    {
        a++;
        memset (s1,0,sizeof (s1));
        for (int i=0;i<4;i++)
            input>>s[i];
        output<<"Case #"<<a<<": ";
        for (int i=0;i<4;i++)
            for (int o=0;o<4;o++)
            {
                if (s[i][o]=='X'||s[i][o]=='T')
                s1[i][o]=1;
            }
            if (is())
            {output<<"X won\n";continue ;}
            memset (s1,0,sizeof (s1));
            for (int i=0;i<4;i++)
            for (int o=0;o<4;o++)
            {
                if (s[i][o]=='O'||s[i][o]=='T')
                s1[i][o]=1;
            }
            if (is())
            {output<<"O won\n";continue ;}
            int pd=0;
            for (int i=0;i<4;i++)
            {
                for (int o=0;o<4;o++)
                {
                    if (s[i][o]=='.')
                    {pd=1;break ;}
                }
                if (pd==1)
                break ;
            }
            if (pd==1)
            output<<"Game has not completed\n";
            else
            output<<"Draw\n";

    }
    output<<"\n";
    input.close();
    output.close();

    return 0;
}
