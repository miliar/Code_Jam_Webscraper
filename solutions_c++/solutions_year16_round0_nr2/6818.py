#include<iostream>
#include<fstream>
#include<string.h>

using namespace std;

int main()
{
    ifstream fin("input.txt",ios::in);
    int t;
    fin>>t;
    cout<<"testcases"<<t<<endl;
    fstream fout("output.txt",ios::out);
    for(int i=1;i<=t;i++)
    {
        char ch[101];
        int turns = 0;
        fin>>ch;
        cout<<"array found"<<ch;
        int length = strlen(ch);
        cout<<"of length"<<length<<endl;
        for(int i=length -1; i >=0; i--)
        {
            if(ch[i] == '+')
            {
                continue;
            }
            else
            {
                turns++;
                for(int j=0; j<=i ; j++)
                {
                    if (ch[j]=='+')
                    {
                        ch[j]= '-';
                        continue;
                    }
                    if (ch[j]=='-')
                    {
                        ch[j]= '+';
                        continue;
                    }
                }
            }
        }
        cout<<"turns "<<turns<<endl;
        fout<<"Case #"<<i<<": "<<turns<<endl;
    }
    return 0;
}
