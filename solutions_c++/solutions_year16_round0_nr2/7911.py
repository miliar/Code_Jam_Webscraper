#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
    int t,i,f=0,j=1;;
    string s;
    cin>>t;
    FILE *fp;
    fp=fopen("sss.txt","w");
    while(t--)
    {
        cin >>s;
        i=s.length();
        f=0;
           while(i>=0)
           {
            if(s[i]=='-')
            {
              f++;
              break;
            }
            i--;
           }
           while(i>0)
           {
               if(s[i]!=s[i-1])
               {
                   f++;
               }
               i--;
           }
           fprintf(fp,"Case #%d: %d\n",j,f);
           j++;

        }

    }

