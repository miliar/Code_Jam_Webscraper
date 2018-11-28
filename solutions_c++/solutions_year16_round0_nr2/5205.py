#include<iostream>
#include<string>
using namespace std;

int tab[100000],r[10000],l,t;
string s;

void clear(int k[])
{
    for(int i=0; i<=100000; i++) k[i]=0;
}

int main()
{
    cin>>t;
    for(int i=1; i<=t; i++)
    {
        clear(tab);
        cin>>s;
        l=s.length();
        for(int q=0; q<l; q++)
        {
            if(s[q]==45) tab[q]=1;
        }
        r[i]=tab[l-1];
        int k=1;
        while(k<l)
        {
            if(s[k]!=s[k-1]) r[i]+=1;
            k+=1;
        }
    }
    for(int i=1; i<=t; i++)
    {
        cout<<"Case #"<<i<<": "<<r[i]<<endl;
    }
}
