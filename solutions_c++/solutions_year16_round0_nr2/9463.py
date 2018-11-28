#include <iostream>
#include<cstdio>

using namespace std;

int T=0;
int TOT=0;
char c;


string line;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("resultok.txt","w",stdout);

    cin >> T; getline (cin,line);

    for (int i=0;i<T;i++)
    {
        getline (cin,line);
        TOT=1;
        c=line[0];

        for (unsigned int j=1;j<line.length();j++)
        {
            if (line[j]!=c)
            {
                c=line[j];
                TOT++;
            }
        }
        cout << "Case #" << (i+1) << ": " ;
        if (line[line.length()-1]!=43)
            cout << TOT ;
        else
            cout << TOT-1;

        cout << endl;
    }

    return 0;
}
