#include<iostream>
#include<stdio.h>
#include<fstream>
using namespace std;
int gd=0;
int lstm(char st[]);
int chek(char st[])
{
    int i=0,chk=0;
    for(i=0; st[i]!='\0'; i++)
    {
        if(st[i]=='-')
        {
            chk=1;
        }
    }
    return chk;
}
int main()
{

    char st[101],tm[101];
    int i=0,lt=0,len=0,ltp=0,chk=0,tc=0,x=0;
    ifstream myfile;
    myfile.open("test2.in");
    myfile>>tc;
    ofstream fout;
    fout.open("out1.txt",ios::app);
    //scanf("%d\n",&tc);
    while(tc){
    myfile>>st;
    //gets(st);
    for(i=0; st[i]!='\0'; i++)
    {
        len++;
    }
    while(chek(st))
    {
        lt=lstm(st);

        if(st[0]=='+')
        {
            for(i=lt; st[i]=='-'; i--)
            {
            }
            ltp=i;
            for(i=ltp; i>=0; i--)
            {
                tm[ltp-i]=st[i];
            }
            for(i=0; i<=ltp; i++)
            {
                if(tm[i]=='+')
                {

                    st[i]='-';
                }
                else
                {
                    st[i]='+';
                }

            }
            gd++;
        }
        else
        {

            for(i=lt; i>=0; i--)
            {
                tm[lt-i]=st[i];
            }
            for(i=0; i<=lt; i++)
            {
                if(tm[i]=='+')
                {

                    st[i]='-';
                }
                else
                {
                    st[i]='+';
                }

            }
            gd++;
        }
    }
    fout<<"CASE #"<<(x+1)<<": "<<gd<<"\n";
    x++;
    tc--;
    gd=0;
    }
}
int lstm(char st[])
{
    int i=0,last=0;
    for(i=0; st[i]!='\0'; i++)
    {
        if(st[i]=='-')
        {
            last=i;
        }
    }
    return last;
}
