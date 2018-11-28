#include <iostream>
#include <cstdlib>
#include <string>
#include <fstream>
#include <cmath>

using namespace std;

int main()
{
    ifstream fin;
    fin.open("A-large.in");
    if (!fin.is_open())
    {
        cout<<"error!"<<endl;
        return -1;
    }
    ofstream fout;
    fout.open("answer");
    int cases=0;
    fin>>cases;
    fin.get();
    string str[10];
    str[0]="ZERO";
    str[1]="ONE";
    str[2]="TWO";
    str[3]="THREE";
    str[4]="FOUR";
    str[5]="FIVE";
    str[6]="SIX";
    str[7]="SEVEN";
    str[8]="EIGHT";
    str[9]="NINE";
    for (int i=0;i<cases;i++)
    {
        cout<<"start";
        fout<<"Case #"<<i+1<<": ";
        string s;
        getline(fin,s);
        int a[26]={0};
        int l=s.length();
        for (int j=0;j<l;j++)
        {
            a[s[j]-'A']++;
        }
        int number[10]={0};
        for (int j=0;j<10;j++)
        {
            number[j]=-1;
        }
        if (a['Z'-'A']!=0)
        {
            int n=a['Z'-'A'];
            for (int j=0;j<str[0].length();j++)
            {
                a[str[0][j]-'A']-=n;
            }
            number[0]=n;
        }
        if (a['W'-'A']!=0)
        {
            int n=a['W'-'A'];
            for (int j=0;j<str[2].length();j++)
            {
                a[str[2][j]-'A']-=n;
            }
            number[2]=n;
        }
        if (a['U'-'A']!=0)
        {
            int n=a['U'-'A'];
            for (int j=0;j<str[4].length();j++)
            {
                a[str[4][j]-'A']-=n;
            }
            number[4]=n;
        }
        if (a['F'-'A']!=0)
        {
            int n=a['F'-'A'];
            for (int j=0;j<str[5].length();j++)
            {
                a[str[5][j]-'A']-=n;
            }
            number[5]=n;
        }
        if (a['X'-'A']!=0)
        {
            int n=a['X'-'A'];
            for (int j=0;j<str[6].length();j++)
            {
                a[str[6][j]-'A']-=n;
            }
            number[6]=n;
        }
        if (a['S'-'A']!=0)
        {
            int n=a['S'-'A'];
            for (int j=0;j<str[7].length();j++)
            {
                a[str[7][j]-'A']-=n;
            }
            number[7]=n;
        }
        if (a['G'-'A']!=0)
        {
            int n=a['G'-'A'];
            for (int j=0;j<str[8].length();j++)
            {
                a[str[8][j]-'A']-=n;
            }
            number[8]=n;
        }
        if (a['T'-'A']!=0)
        {
            int n=a['T'-'A'];
            for (int j=0;j<str[3].length();j++)
            {
                a[str[3][j]-'A']-=n;
            }
            number[3]=n;
        }
        if (a['O'-'A']!=0)
        {
            int n=a['O'-'A'];
            for (int j=0;j<str[1].length();j++)
            {
                a[str[1][j]-'A']-=n;
            }
            number[1]=n;
        }
        if (a['I'-'A']!=0)
        {
            int n=a['I'-'A'];
            for (int j=0;j<str[9].length();j++)
            {
                a[str[9][j]-'A']-=n;
            }
            number[9]=n;
        }
        for (int j=0;j<10;j++)
        {
            if (number[j]>0)
            {
                for (int k=0;k<number[j];k++)
                {
                    fout<<j;
                }
            }
        }
        fout<<endl;
    }
}
