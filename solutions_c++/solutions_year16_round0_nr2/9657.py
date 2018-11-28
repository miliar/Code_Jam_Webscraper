#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>

using namespace std;

string s;
char c,aux;
int R,a,casos,caso;

int main()
{
    freopen("i2.in","r",stdin);
    freopen("o2.out","w",stdout);
    cin>>casos;
    caso=1;
    while (casos--)
    {
        cin>>s;
        cout<<"Case #"<<caso++<<": ";
        R=0;
        c=s.at(0);
        for (a=1;a<s.size();a++)
        {
            aux=s.at(a);
            if (aux!=c)
            {
                c=aux;
                R++;
            }
        }
        if (c=='-') R++;
        cout<<R<<endl;
    }
    fclose(stdin);
    fclose(stdout);
}
