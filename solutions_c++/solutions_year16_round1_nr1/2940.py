#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

string S,aux;
int T,caso,a;

int main()
{
    freopen("i2.in","r",stdin);
    freopen("o2.out","w",stdout);
    cin>>T;
    caso=1;
    while (T--)
    {
        cin>>S;
        aux=S.at(0);
        for (a=1;a<S.size();a++)
        {
            if (aux.at(0)<=S.at(a)) aux=S.at(a)+aux;
            else aux+=S.at(a);
        }
        cout<<"Case #"<<caso++<<": "<<aux<<endl;
    }
    fclose(stdin);
    fclose(stdout);
}
