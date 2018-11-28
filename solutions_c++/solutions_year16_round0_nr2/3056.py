#include<bits/stdc++.h>
using namespace std;
string flip(string str,long long x)
{
    string k=str.substr(0,x);
    for(int i=0;i<x;i++)
    {
        if(k[i]=='+')
            k[i]='-';
        else k[i]='+';
    }
    str.replace(0,x,k);
    //cout<<str<<endl;
    return str;
}
int main()
{
    ifstream fin;
    ofstream fout("ans.txt");
    fin.open ("input.txt");

    if(!fin.is_open())
    {
        cout<<"file error";
    }
    else
    {
        long long t,s,cou,x;
        string str,str1;
        fin>>t;
        s=t;
        while(t--)
        {
            cou=0;
            fin>>str;
            str1=str;
            for(int i=0;i<str1.length();i++)
            {
                if(str1[i]=='-')
                    str1[i]='+';
            }
            //cout<<str1;
            x=str.length();
            while(str!=str1)
            {
                while(str[x-1]=='+')
                    x=x-1;
                str=flip(str,x--);
                cou++;
            }
            fout<<"Case #"<<s-t<<": "<<cou<<endl;
        }
        fin.close();
        fout.close();
    }
}
