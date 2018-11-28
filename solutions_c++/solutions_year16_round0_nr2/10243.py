#include <stdio.h>
#include <iostream>
#include <string.h>
using namespace std;
void reverse1(char b[100],int l)
    {
        int i,j,temp;
        for(i=0;i<=l;i++)
            if(b[i]=='+')
                b[i]='-';
            else
                b[i]='+';
        for(i=0,j=l;i<=l/2;i++,j--)
         {
            temp=b[i];
            b[i]=b[j];
            b[j]=temp;
         }
        /*for(i=0;i<=l;i++)*/
           // cout<<b[0]<<" ";

    }
int main()
{

    int test,i,j;
    cin>>test;
    int time[test];
    for(int i=0;i<test;i++)
    {   time[i]=0;
        char pan[100];
        cin>>pan;
        int l=strlen(pan);
        if(l==1)
        {   if(pan[0]=='-')
            time[i]++;
        }
        else
        for(j=0;;)
        {
            if(pan[0]==pan[j])
            {
                    if(j<l)
                   j++;

            }
            if(j<l)
            if(pan[j]!=pan[0])
            {
                reverse1(pan,j-1);
                time[i]++;
                j=0;
            }

            if(j==l&&pan[j-1]=='+')
              break;
            else if(j==l&&pan[j-1]=='-')
                   {
                       time[i]++;
                       break;
                   }
        }
    }
    for(int i=0;i<test;i++)
        cout<<"Case #"<<i+1<<": "<<time[i]<<"\n";
    return 0;
}
