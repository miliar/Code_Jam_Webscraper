#include<iostream>
#include<string.h>
using namespace std;

void invert(char a[],int n)    
{
    int i=0;
    while(i<=n)
   {    
        if(a[i]=='+') a[i]='-';
        else a[i]='+';
        i++;
   }
}

int main()
{
    char st[100];
    int X, c,j;
    cin>>X;
    for(int i=1; i<=X; i++)
    {
        cin>>st;
        j=0;
        c=0;
        while(st[j+1]!='\0')
        {
            j=0;
            while(st[j]==st[j+1])j++;
            if(!((st[j+1]=='\0')&&st[j]=='+'))
            {
            invert(st,j);
            c++;}
        }
        if(st[0]=='+')
        {
           cout<<"Case #"<<i<<": "<<c<<endl;
        }
        else
        {
            cout<<"Case #"<<i<<": "<<c+1<<endl;
        }

    }
return 0;
}