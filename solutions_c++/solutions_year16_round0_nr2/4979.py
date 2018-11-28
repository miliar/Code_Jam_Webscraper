#include <iostream>
#include <fstream>
#include <string.h>

using namespace std;

int n,i,nr,j,l,ok,ok2;
char s[100];

int main()
{
    ifstream f("B-large.in");
    ofstream g("B-large.out");
    f>>n;
    for(i=1;i<=n;i++)
    {
        f>>s;
        l=strlen(s);
        ok=0;
        nr=0;
        for(j=0;j<l;j++)
        {
            ok2=0;
            if(s[j]=='+')ok=1;
            while(s[j]=='-')
            {
                j++;
                ok2=1;
            }
            if(ok2==1&&ok==0){nr+=1;j--;}
            else if(ok2==1&&ok==1){nr+=2;j--;}
        }
        g<<"Case #"<<i<<": "<<nr<<'\n';
    }
    f.close();
    g.close();
}
