#include<iostream>
#include<string.h>
#include<stdio.h>
using namespace std;
int count=0;
void plak(char ch[],int i)
{   
    for(int k=0;k<=i;k++)
    {   
        if(ch[k]=='+')
        {   
            ch[k]='-';
        }
        else
        {
           
            ch[k]='+';
        }
       
    }
    count++;
}
main()
{
    int T,size,i,k=1;
    char ch[1000];
    cin>>T;
    while(T--)
    {
         cin>>ch;
         count=0;
         size=strlen(ch);            
         for(i=size-1;i>=0;i--)
         {
            if(ch[i]=='-')
            {
                plak(ch,i);
             
            }
           
         }
         cout<<"Case #"<<k<<": "<< count<<"\n";
            k++;
    }
}
