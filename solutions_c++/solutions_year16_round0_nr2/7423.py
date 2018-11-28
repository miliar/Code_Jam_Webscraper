#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int main()
{
    long long int i,j,d,n,k,c=0,mnus=0,pls=0,flag=0,l;
    char temp;
    string s;
    ifstream fin;
    fin.open("input.in");
    ofstream fout;
    fout.open("output.txt");
    fin>>n;
    for(int h=0; h<n; h++)
    {
        fin>>s;
        d=s.length();
        for(i=(d-1); i>=0; i--)
        {

            for(int u=0; u<d; u++)
            {
                if(s[u]=='+')
                    pls++;
                else
                    mnus++;
            }

            if(mnus==0)
            {
                break;
            }
            pls=0;
            mnus=0;
            if(s[i]=='-' && s[0]=='-')
            {
                k=0;
                j=i;
                c++;
                while(k<j)
                {
                    temp=s[k];
                    s[k]=s[j];
                    s[j]=temp;
                    k++;
                    j--;
                }
                for(int q=0; q<=i; q++)
                {
                    if(s[q]=='+')
                        s[q]='-';
                    else
                        s[q]='+';
                }
            }
            else if(s[0]=='+' && s[i]=='-')
            {
                flag=1;
                l=i+1;
            }
            else if(s[0]=='+' && s[i]=='+' && flag==1)
            {
                c++;
                k=0;
                j=i;
                while(k<j)
                {
                    temp=s[k];
                    s[k]=s[j];
                    s[j]=temp;
                    k++;
                    j--;
                }
                for(int q=0; q<=i; q++)
                {
                    if(s[q]=='+')
                        s[q]='-';
                    else
                        s[q]='+';
                }
                flag=0;
                i=l;
            }
        }
        if(h==0){
            fout<<"Case #"<<(h+1)<<": "<<c;}
            else
              fout<<"\nCase #"<<(h+1)<<": "<<c;
           c=0;
    }
}
