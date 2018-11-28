#include<iostream>
#include<fstream>
#define cout fout
#define cin fin

using namespace std;

int main()
{
    ifstream fin("input02l.txt");
    ofstream fout("output02.txt");
    int T,lc=0,l=0;
    char str[104];
    cin>>T;
    for (int test=1;test<=T;test++)
    {
        cin>>str;
        lc=0;
        l=0;
        int i=0;
        for (i=0;str[i];i++)
        {
            if (str[i]=='-')
            {
                if (lc!=1)
                    l++;
                lc=1;
            }
            else
            if (str[i]=='+')
            {
                if (lc!=2)
                    l++;
                lc=2;
            }
        }
        if (str[i-1]=='+')
            cout<<"Case #"<<test<<": "<<l-1<<endl;
        else
            cout<<"Case #"<<test<<": "<<l<<endl;
    }
    return 0;
}
