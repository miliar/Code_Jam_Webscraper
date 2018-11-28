#include<iostream>
#include<stdio.h>
#include<string.h>
#include<fstream>
using namespace std;
char str[1000000];
int i,j,k;
int isplus()
{

    for(i=0;i<strlen(str);i++)
        if(str[i]!='+')
        break;
    if (i==strlen(str))
    return 1;
    else return 0;
}
int main()
{
ifstream ip;
ofstream o;
ip.open("B-large.in");
o.open("outl.txt");
k=0;
int t;ip>>t;
int op[t];
while(t--)
{   cout<<t<<endl;
    unsigned long long int count=0;
    ip>>str;
    while(!(isplus()))
    {
        i=0;
        while(i<strlen(str))
        {
            if(str[i]=='-')
                break;
            i++;
        }

        while(str[i]!='+'&&i<strlen(str))
                i++;
        for(j=0;j<i;j++)
        {
            if(str[j]=='+')
                str[j]='-';
            else
                str[j]='+';
        }
        count++;
    }
    op[k]=count;
    k=k+1;
}
cout<<endl;
for(i=0;i<k;i++)
o<<"Case #"<<i+1<<": "<<op[i]<<'\n';
}
