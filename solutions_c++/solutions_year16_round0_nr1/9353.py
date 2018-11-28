#include <iostream>
#include<cstdio>
#include <string>
#include <sstream>

using namespace std;

int T=0;
long long  TOT=0;
char c;
int tab[10];
int mul=1;
int pos;

string line;

long long  temp;

bool ret()
{
    int res=0;
    for (int j=0;j<10;j++) res+=tab[j];
    if (res==0) return false;
    return true;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("resultok.txt","w",stdout);

    cin >> T;

    for (int i=0;i<T;i++)
    {
        cin  >> TOT;
        for (int j=0;j<10;j++) tab[j]=1;
        pos=1;

        if (TOT!=0)
        {
          while (ret())
        {
        stringstream oss;
     temp = pos * TOT;
    oss << temp;

     oss >> line;


            for (int j=0;j<line.length();j++) tab[line[j]-48]=0;
            pos++;
        }
        cout << "Case #" << (i+1) << ": " ;

            cout << temp ;


        cout << endl;
        }
        else cout << "Case #" << (i+1) << ": INSOMNIA" << endl;

    }

    return 0;
}


