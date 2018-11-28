#include <bits/stdc++.h>

using namespace std;

void flip(char str[200], int first, int last)
{
    char temp;
    for(int i=first;i<=last/2;i++)
    {
        if(str[i]=='-')
            temp='+';
        else
            temp='-';
        if(str[last-i]=='-')
            str[i]='+';
        else
            str[i]='-';
        str[last-i]=temp;
    }
}

int func(char str[200], int n)
{
    bool complete=false;
    int val=0;
    while(1)
    {
        int index=0;
        if(str[0]=='-')
        {
            while(str[index]!='+')
            {
                if(index==n-1)
                {
                    index++;
                    break;
                }
                index++;
            }
            flip(str,0,index-1);
        }
        else
        {
            while(str[index]!='-')
            {
                if(index==n-1)
                {
                    complete=true;
                    return val;
                }
                index++;
            }
            flip(str,0,index-1);
        }
        val++;
    }
}

int main()
{
    fstream fin,fout;
    fin.open("B-large.in",ios::in);
    fout.open("B-large.out",ios::out);
    int t;
    char str[200];
    fin>>t;
    for(int i=0;i<t;i++)
    {
        fin>>str;
        fout<<"Case #"<<i+1<<": "<<func(str,strlen(str))<<"\n";
    }
    fin.close();
    fout.close();
}
